__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'

import subprocess
import os
import osr
import ogr
import numpy as np
from osgeo import gdal, gdalconst, gdalnumeric, gdal_array
import shutil

from pyEOM import log
LOGGER = log.LOGGER


def TestMODISHDFProcessor():
    geom = 'POLYGON((7.807615733070551 26.259757466002124,7.434080576820532 25.607681923751194,8.510740733070508 25.09140328282509,9.082029795570381 25.884760600666922,7.807615733070551 26.259757466002124))'

    from pyEOM.datasets.predefined.MODIS import MOD13Q1
    dataset = MOD13Q1.Dataset()
    bands = dataset.getBands()

    raster = MODISHDFProcessor(None, bands)
    files = ['MOD13Q1.A2001001.h18v06.005.2008270055643.hdf', 'MOD13Q1.A2001001.h18v07.005.2008270012522.hdf']

    for file in files:
        raster.extractBands(file)

    epsg = None #modis sinusoidal
    raster.clipPolygon(geom, epsg, None)
    raster.processQuality('PR', '0')


class MODISHDFProcessor(object):
    file = None
    filename = None
    fileparts = []
    fileext = []
    dirname = None
    bands = []
    gdal = None
    bandfiles = dict()

    def __init__(self, file, bands, rastertype, publishPath):
        if file != None: self.setFile(file)
        self.bands = bands
        self.publishPath = publishPath
        if not os.path.exists(publishPath+'/data'): os.makedirs(publishPath+'/data')
        if not os.path.exists(publishPath+'/data/tmp'): os.makedirs(publishPath+'/data/tmp')
        self.gdal = GDAL()

        self.wgs84 = osr.SpatialReference()
        self.wgs84.ImportFromEPSG(4326)
        self.modis_sinu = osr.SpatialReference()
        self.modis_sinu.ImportFromProj4 ("+proj=sinu +R=6371007.181 +nadgrids=@null +wktext")
        if rastertype == 'CMG':
            self.modis_sinu = self.wgs84 #for MODIS CMG files

    def setFile(self, file):
        self.file = file
        self.filename = os.path.basename(file)
        self.fileparts = self.filename.split('.')
        self.fileext = os.path.splitext(self.filename)
        self.dirname = os.path.dirname(file)

    def extractBands(self, file=None):
        if file != None: self.setFile(file)
        for key, band in self.bands.items():
            dataset = 'HDF4_EOS:EOS_GRID:"'+self.file+'":"'+band['name']+'"'
            output = self.dirname+'/'+self.fileext[0]+'.'+key+self.fileext[1]
            output = self.gdal.gdal_translate(dataset, output, 'HDF4Image')
            if isinstance(output, basestring):
                if 'files' not in self.bands[key]: self.bands[key]['files'] = []
                self.bands[key]['files'].append(output)
            else:
                LOGGER.error('Error in extractBands')
                raise Exception('Error in extractBands')
                sys.exit(1)

    def clipPoint(self, geom):
        point = ogr.CreateGeometryFromWkt(geom)
        values = dict()
        for key, band in self.bands.items():
            value = self.gdal.gdallocationinfo(band['files'][0], point.GetX(), point.GetY())
            values[key] = value
        return values

    def clipPolygon(self, geom, format, epsg=None, resample=None):
        poly = ogr.CreateGeometryFromWkt(geom)
        srs = self.wgs84
        if epsg == None:
            srs = self.modis_sinu
            tx = osr.CoordinateTransformation(self.wgs84, self.modis_sinu)
            poly.Transform(tx)
            geom = poly.ExportToWkt()
        elif epsg != 4326:
            srs = osr.SpatialReference().ImportFromEPSG(epsg)
            tx = osr.CoordinateTransformation(self.wgs84, srs)
            poly.Transform(tx)
            geom = poly.ExportToWkt()

        self.exportWktToShape(poly, srs)

        for key, band in self.bands.items():
            #merge
            if len(band['files']) > 1:
                merge = self.publishPath+'/data/tmp/'+self.fileparts[0]+'.'+self.fileparts[1]+'.'+key+'.merge'+self.fileext[1]
                merge = self.gdal.gdal_merge(band['files'], merge, format="HDF4Image", nodata=band['nodata'])
            else:
                merge = band['files'][0]
            #clip
            outfile = self.publishPath+'/data/tmp/'+self.fileparts[0]+'.'+self.fileparts[1]+'.'+key+'.clipped'+self.gdal.getFileExtension(format)
            self.bandfiles[key] = self.gdal.gdalwarp(merge, outfile, format, band['nodata'], epsg, resample, 'polygon.kml')
        return self.bandfiles

    def splitBinaryQualityInfo(self, values):
        valuesAr = []
        for limit in values:
            if '<=' in limit:
                splitstr = '<='
                comparefct = np.less_equal
            elif '>=' in limit:
                splitstr = '>='
                comparefct = np.greater_equal
            elif '>' in limit:
                splitstr = '>'
                comparefct = np.greater
            elif '<' in limit:
                splitstr = '<'
                comparefct = np.less
            elif '==' in limit:
                splitstr = '=='
                comparefct = np.equal
            elif '=' in limit:
                splitstr = '='
                comparefct = np.equal
            else:
                LOGGER.error('Relation condition wrong!')
                raise Exception('Relation condition wrong!')
            LOGGER.info('Split string: '+splitstr)
            key, value = limit.split(splitstr)
            LOGGER.info('Key: '+str(key))
            LOGGER.info('Val: '+str(value))
            if '-' in key:
                start, end = key.split('-')
            else:
                start = end = int(key)+1
            valuesAr.append({'start':int(start),'end':int(end)+1,'value':int(value),'fct':comparefct})
        return valuesAr

    def checkQualityBinary(self, val, qualityChecks):
        qualityFullfilled = []
        for item in qualityChecks:
            if item['fct'](int(val[item['start']:item['end']]), item['value']):
                qualityFullfilled.append(True)

        if len(qualityFullfilled) == len(qualityChecks):
            return True
        else:
            return False

    def processQualityPoint(self, qaValue, bandlayer, qualityInfo):
        if bandlayer not in self.bandfiles:
            raise Exception('Given quality band is not available!')

        qualityBand = self.bands[bandlayer]

        finalfiles = dict()
        if qualityBand['quality_datatype'] == 'int':
            values = qualityInfo.split(';')   #0;1 (e.g., good data and marginal data for MOD13Q1)
            if str(qaValue) not in values:
                return 0
            else:
                return 1
        elif qualityBand['quality_datatype'] == 'bit':
            values = qualityInfo.split(';')  #2-5=0000;6-7<10
            valuesAr = self.splitBinaryQualityInfo(values)
            val = np.binary_repr(qaValue).zfill(16)[::-1]   #flipped
            result = self.checkQualityBinary(val, valuesAr)
            if result:
                return 1
            else:
                return 0

    def processQuality(self, bandlayer, qualityInfo):
        if bandlayer not in self.bandfiles:
            raise Exception('Given quality band is not available!')
        qualityFile = self.bandfiles[bandlayer]
        LOGGER.info('QualityFile '+str(qualityFile))
        qualityArray = gdalnumeric.LoadFile(qualityFile)
        qualityValues = np.unique(qualityArray)
        qualityBand = self.bands[bandlayer]

        if not os.path.exists(self.publishPath+'/data/mask'):
            os.makedirs(self.publishPath+'/data/mask')
        if not os.path.exists(self.publishPath+'/data/output'):
            os.makedirs(self.publishPath+'/data/output')

        finalfiles = dict()
        for key, band in self.bands.items():
            if band['imagetype'] == 'qualityInformation':
                continue

            dataFile = self.bandfiles[key]
            maskFile = self.publishPath+'/data/mask/'+os.path.basename(dataFile)
            dataFile = self.publishPath+'/data/output/'+os.path.basename(dataFile)

            dataDS = gdal.Open(self.bandfiles[key])
            dataBand = dataDS.GetRasterBand(1)
            dataArray = dataBand.ReadAsArray(0, 0, dataDS.RasterXSize, dataDS.RasterYSize)
            dataNoData = dataBand.GetNoDataValue()

            maskArray = np.copy(dataArray)
            maskArray[:] = dataNoData

            if qualityBand['quality_datatype'] == 'int':
                values = qualityInfo.split(';')   #0;1 (e.g., good data and marginal data for MOD13Q1)
                for quality in qualityValues:
                    if str(quality) not in values:
                        dataArray[qualityArray==quality] = dataNoData
                        maskArray[qualityArray==quality] = 0
                    else:
                        maskArray[qualityArray==quality] = 1
            elif qualityBand['quality_datatype'] == 'bit':
                values = qualityInfo.split(';')  #2-5=0000;6-7<10
                valuesAr = self.splitBinaryQualityInfo(values)
                for quality in qualityValues:
                    val = np.binary_repr(quality).zfill(16)[::-1]   #flipped
                    result = self.checkQualityBinary(val, valuesAr)
                    LOGGER.info('Quality value '+val+' set to '+str(result))

                    if result:
                        maskArray[qualityArray==quality] = 1
                    else:
                        maskArray[qualityArray==quality] = 0
                        dataArray[qualityArray==quality] = dataNoData
            else:
                LOGGER.error('No quality info')
                raise Exception('No quality info')

            dataDSMasked = gdal_array.SaveArray(dataArray, dataFile, 'HDF4Image')
            gdal_array.CopyDatasetInfo(dataDS, dataDSMasked)

            maskDSMasked = gdal_array.SaveArray(maskArray, maskFile, 'HDF4Image')
            gdal_array.CopyDatasetInfo(dataDSMasked, maskDSMasked)
            finalfiles[key] = dataFile

            maskDS, maskDSMasked, dataDS, dataDSMasked = [None]*4
            del maskDS, maskDSMasked, dataDS, dataDSMasked
        return finalfiles

    def exportWktToShape(self, wkt, srs):
        outDriver = ogr.GetDriverByName('KML')
        outDataSource = outDriver.CreateDataSource('polygon.kml')
        outLayer = outDataSource.CreateLayer('polygon', geom_type=ogr.wkbPolygon, srs=srs)
        featureDefn = outLayer.GetLayerDefn()
        outFeature = ogr.Feature(featureDefn)
        outFeature.SetGeometry(wkt)
        outLayer.CreateFeature(outFeature)
        outFeature.Destroy
        outDataSource.Destroy()


class RasterProcessing(object):
    file = None
    filename = None
    outputformat = "GTiff"
    outputfilext = {'GTiff': '.tif', 'netCDF': '.nc'}

    def __init__(self, file=None, outputformat=None):
        if file != None:
            self.file = file
            self.filename = os.path.basename(file)
        if outputformat != None:
            self.outputformat = outputformat

    def setFile(self, file):
        self.file = file
        self.filename = os.path.basename(file)

    def setOptions(self):
        pass

    def extract(self, dataset, datasetext, outputformat, datatype=""):
        if outputformat not in self.outputfilext:
            raise Exception('Output format is not available in class!')
        if datatype == 'MODISHDF':
            dataset = 'HDF4_EOS:EOS_GRID:"'+self.file+'":"'+dataset+'"'
        output = os.path.splitext(self.file)[0]+datasetext+self.outputfilext[outputformat]
        process = GDAL().gdal_translate(dataset, output, format=outputformat)
        LOGGER.debug('Process: '+process)
        if isinstance(process, basestring):
            return process
        else:
            return False

    def merge(self, files, outfile, outputformat="GTiff"):
        if len(files) <= 1:
            raise Exception('More than 1 file needed to merge')
        return GDAL().gdal_merge(files, outfile+self.outputfilext[outputformat], outputformat)

    def reproject(self):
        pass

    def clip(self, geom, dstnodata, epsg, resample):
        outfile = os.path.splitext(self.file)[0]+'_clipped'+os.path.splitext(self.file)[1]
        f=open('cutline.csv', 'w')
        f.write("id,WKT\n")
        f.write(',"'+geom+'"')
        f.close()

        return GDAL().gdalwarp(self.file, outfile, dstnodata, epsg, resample, 'cutline.csv')

    def compress(self, type):

        pass


class GDAL(object):
    outputfilext = {'GTiff': '.tif', 'netCDF': '.nc', 'HDF4Image': '.hdf','VRT': '.vrt', 'KEA': '.kea', }
    path = '' # with a training slash

    resample_methods = ['near', 'bilinear', 'cubic', 'cubicspline', 'lanczos']

    def __init__(self):
        pass

    def getFileExtension(self, format):
        if format not in self.outputfilext:
            LOGGER.error('Format '+format+' not available!')
            raise Exception('Format '+format+' not available!')
        return self.outputfilext[format]

    def execute(self, cmd, output):
        if isinstance(cmd, list):
            cmd = ' '.join(cmd)
        LOGGER.info(cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if output != None and os.path.isfile(output):
            return output
        elif stderr == '':
            return stdout.strip()
        else:
            LOGGER.error(stderr)
            return False

    def gdal_translate(self, input, output, format="GTiff"):
        #if not os.path.isfile(input):
        #    raise Exception('Input file not found!')
        return self.execute([self.path+'gdal_translate', '-of', format, input, output], output)


    def gdal_merge(self, inputfiles, output, format="GTiff", nodata=""):
        if isinstance(inputfiles, list):
            inputfiles = ' '.join(inputfiles)
        #if len(inputfiles) <= 1:
        #    raise Exception('Inputfiles needs more than 1 file!')

        return self.execute([self.path+'gdal_merge.py', '-o', output, '-of', format, inputfiles], output)


    def gdalwarp(self, inputfile, output, format, dstnodata, epsg, resample, cutline):
        if dstnodata != None:
            srcnodata = '-srcnodata '+str(dstnodata)
            dstnodata = '-dstnodata '+str(dstnodata)
        else:
            dstnodata = ''
            srcnodata = ''
        if epsg != None and epsg > 0:
            reproject = '-t_srs EPSG:'+str(epsg)
            if resample != None and resample in self.resample_methods:
                reproject = reproject + ' -r '+resample
        else:
            reproject = ''
        if cutline != None:
            cutline = '-cutline '+cutline+' -crop_to_cutline'
        if format != None:
            format = '-of '+format
        else:
            format = ''

        return self.execute([self.path+'gdalwarp', format, srcnodata, dstnodata, reproject, cutline, inputfile, output], output)


    def gdal_compress(self, inputfile, output, type):
        return self.execute([self.path+'gdal_translate', '-co COMPRESS='+type, inputfile, output], output)

    def gdallocationinfo(self, inputfile, x, y):
        return self.execute([self.path+'gdallocationinfo', '-valonly', '-geoloc', '-wgs84', inputfile, str(x), str(y)], None)

    def gdalbuildvrt(self, inputs, output, separate=True):
        inputfilelist = ''
        if os.path.isfile(inputs):
            inputfilelist = '-input_file_list '+inputs
            inputs = ''
        if separate:
            separate = '-separate'
        else:
            separate = ''

        return self.execute([self.path+'gdalbuildvrt', separate, inputfilelist, output, inputs], output)