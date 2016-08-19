__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'
__version__ = '0.1'

import logging
from pyEOM.sources import *
from pyEOM import processing
from datetime import datetime
import os, re, sys
import subprocess
import sqlite3
from pyspatialite import dbapi2 as db
from datetime import datetime
import shutil

from pyEOM import log
LOGGER = log.LOGGER


class Tiles(object):
    database = os.path.dirname(os.path.abspath(processing.__file__))+'/data/modis_tiles.sqlite'

    def __init__(self):
        self.dbcon = db.connect(self.database)
        # self.dbcon.row_factory = sqlite3.Row
        self.dbcur = self.dbcon.cursor()

    def getTilesFromGeometry(self, geom):
        tiles = []

        sel = self.dbcur.execute("SELECT 'h'||substr('00'||cast(h as int), -2,2 )||'v'||substr('00'||cast(v as int),-2,2) as tile FROM modis_tiles WHERE Intersects(GEOMETRY, GeomFromText('%s'))==1" % (geom)).fetchall()
        if len(sel) > 0:
            for tile in sel:
                tiles.append(tile[0])
        return tiles


class GEE(GEESource):
    dataset = None
    start = '1900-01-01'
    end = '2100-01-01'
    epsg = 'SR-ORG:6974'

    def __init__(self, task):
        self.task = task
        if 'dataset' not in task:
            raise Exception('No dataset found in task')
            sys.exit(1)
        self.dataset = task['dataset']
        if 'geom' not in task:
            raise Exception('No geometry found in task')
            sys.exit(1)
        if 'start' in task:
            self.start = start
        if 'end' in task:
            self.end = end
        if 'publishPath' not in task:
            self.publishPath = os.getcwd()
        else:
            self.publishPath = task['publishPath']

        self.connect()

        self.geom = self.processGeometry(task['geom'])

    def setPublishPath(self, path):
        self.publishPath = path

    def run(self):
        #                   dataset     bands   geom        start       end     epsg        scale   crsTransform
        data = self.getData(self.dataset, None, self.geom, self.start, self.end, self.epsg, None, True)
        return data

    def ingest(self, format=None):
        return self.run()


def TestDatasetLPDAAC():
    dataset = Dataset()
    dataset.getProduct('MOD13Q1')
    dataset.source.download('', ['h12v08'])

class LPDAACHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

class LPDAAC(HTTPSource):
    url = 'http://e4ftl01.cr.usgs.gov'
    userpwd = None
    listDirectoriesIndex = 3

    def setUserPwd(self, login):
        self.userpwd = login
        from base64 import b64encode
        userAndPass = b64encode(str.encode(self.userpwd)).decode("ascii")
        self.http_header = {'Authorization': 'Basic %s' % userAndPass}
        cookieprocessor = urllib2.HTTPCookieProcessor()
        opener = urllib2.build_opener(LPDAACHTTPRedirectHandler, cookieprocessor)
        urllib2.install_opener(opener)

    def __init__(self):
        super(LPDAAC, self).__init__(self.url)


class NSIDC(FTPSource):
    url = 'n5eil01u.ecs.nsidc.org'
    host = 'n5eil01u.ecs.nsidc.org'
    user = 'anonymous'
    password = 'anon'

    def __init__(self):
        super(NSIDC, self).__init__(self.host)
        self.connect()


class MODISHDF(object):
    source = None
    product = dict() #downloadInfo

    taskStart = datetime.strptime('1900-01-01', '%Y-%m-%d')
    taskEnd = datetime.strptime('3000-12-31', '%Y-%m-%d')
    geom = None
    geomType = None

    directories = [] #dates
    tiles = None
    dataset = None
    bands = None

    downloadPath = None
    publishPath = os.getcwd()
    outputs = dict()

    def addTask(self, dataset, geom, publishPath, start=None, end=None, qualityValue=None, qualityBand=None, epsg=None, resample=None, source=None, format=None):
        pass

    def __init__(self, task, dataset, source):
        LOGGER.debug('LPDAAC init')
        self.dataset = dataset
        self.source = source
        if 'start' in task != "":
            self.taskStart = datetime.strptime(task['start'], '%Y-%m-%d')
        if 'end' in task != "":
            self.taskEnd = datetime.strptime(task['end'], '%Y-%m-%d')
        if not 'geom' in task:
            LOGGER.error('No Geometry given!')
            raise Exception('No Geometry given!')
            sys.exit(1)
        if not 'dataset' in task:
            LOGGER.error('No Dataset given!')
            raise Exception('No Dataset given!')
            sys.exit(1)
        if 'publishPath' not in task:
            task['publishPath'] = os.getcwd()
        self.setPublishPath(task['publishPath'])

        self.geom = task['geom']
        if 'POINT' in self.geom:
            self.geomType = 'POINT'
        else:
            self.geomType = 'POLYGON'
        self.product = task['dataset']
        self.task = task
        self.bands = dataset.getBands()

        self.prepare()

    def setPublishPath(self, path):
        self.publishPath = path
        if not os.path.exists(path): os.makedirs(path)
        if not os.path.exists(path+'/data'): os.makedirs(path+'/data')

    def setDownloadPath(self, path):
        self.downloadPath = path
        if not os.path.exists(path): os.makedirs(path)

    def prepare(self):
        tilesObj = Tiles()
        self.task['tiles'] = tilesObj.getTilesFromGeometry(self.task['geom'])
        self.tiles = '('+'|'.join(self.task['tiles'])+')'
        dates = self.source.listDirectories(self.product['directory'])
        self.directories = []
        self.dates = []
        for date in dates:
            dt = datetime.strptime(date, '%Y.%m.%d')
            if dt >= self.taskStart and dt <= self.taskEnd:
                self.directories.append(date)
                self.dates.append(dt)

        return dict(tiles=self.task['tiles'], dates=self.dates)

    def process(self, files, format, epsg=None, resample=None, compress=False):
        #extract dataset
        LOGGER.info('extract bands')
        raster = processing.MODISHDFProcessor(None, self.bands, self.dataset.rastertype, self.publishPath)
        for file in files:
            raster.extractBands(file)

        #merge, clip, reproject, compress based on geometry
        LOGGER.info('merge, clip, reproject, compress')
        if self.geomType == 'POINT':
            outputs = raster.clipPoint(self.geom)
            if 'qualityBand' in self.task and 'qualityValue' in self.task:
                qaValue = outputs[self.task['qualityBand']]
                result = raster.processQualityPoint(qaValue, self.task['qualityBand'], self.task['qualityValue'])
                if result == 0:
                    for key, band in self.bands:
                        if band['imagetype'] == 'qualityInformation':
                            continue
                        outputs[key] = self.dataset.nodata

        elif self.geomType == 'POLYGON':
            outputs = raster.clipPolygon(self.geom, format, epsg, resample)
            if 'qualityBand' in self.task and 'qualityValue' in self.task:
                qualityOutputs = raster.processQuality(self.task['qualityBand'], self.task['qualityValue'])
                for key in qualityOutputs:
                    outputs[key] = qualityOutputs[key]
        else:
            LOGGER.error('No valid geometry found -> no clipping!')
            #raise Exception('No valid geometry found!')

        return outputs

    def setOutputs(self, files, date):
        if self.geomType == 'POINT':
            for key in files:
                self.outputs[key].addEntry(date, files[key])
        else:
            if not os.path.exists(self.publishPath+'/data/files'): os.makedirs(self.publishPath+'/data/files')
            for key in files:
                LOGGER.info('move file '+files[key]+' to '+self.publishPath+'/data/files/')
                shutil.move(files[key], self.publishPath+'/data/files/')
                self.outputs[key].addEntry(date, self.publishPath+'/data/files/'+os.path.basename(files[key]))

    def download(self, date, path=""):
        if path == "":
            if self.downloadPath != None:
                downloadPath = self.downloadPath+'/'+self.dataset.product+'/'+date
            else:
                downloadPath = self.publishPath+'/raw/'+date
        else:
            downloadPath = path
        if not os.path.exists(downloadPath): os.makedirs(downloadPath)

        self.source.listFiles(self.product['directory']+'/'+date)
        self.source.filterFiles('.*\.'+self.tiles+'\..*\.hdf$')
        localFiles = self.source.downloadFiles(downloadPath)
        return localFiles

    def mergeOutputs(self, format="VRT", fileformat="HDF4Image"):
        datapath = self.publishPath+'/data/'
        extension = processing.GDAL().getFileExtension(format)
        for key, band in self.bands.items():
            datafilter = datapath+'files/'+self.dataset.shortname+'.*.'+key+'.*'+processing.GDAL().getFileExtension(fileformat)
            output = datapath+self.dataset.shortname+'.'+key+extension
            if format == 'VRT':
                processing.GDAL().gdalbuildvrt(datafilter, output, True)
            else:
                processing.GDAL().gdal_merge(datafilter, output, format)
            self.outputs[key].setMergedFile(output)

    def buildTSRasterOutput(self):
        LOGGER.info('TODO: build time-series raster output')
        pass

    def ingest(self, format):
        # set output objects
        if self.geomType == 'POINT':
            from pyEOM.outputs import sensor
            for key, band in self.bands.items():
                self.outputs[key] = sensor.Sensor(key, self.dataset.shortname, self.publishPath, dict(geom=self.geom, nodata=band['nodata'], scale=band['scale'], offset=band['offset']))
        else:
            from pyEOM.outputs import raster
            for key, band in self.bands.items():
                self.outputs[key] = raster.TSRaster(key, self.dataset.shortname, self.publishPath, dict(geom=self.geom, nodata=band['nodata'], scale=band['scale'], offset=band['offset']))

        for date in self.directories:
            files = self.download(date)
            outputs = self.process(files, format)
            self.setOutputs(outputs, date)

        if self.geomType == 'POLYGON':
            self.mergeOutputs('VRT', format)

        return self.outputs


