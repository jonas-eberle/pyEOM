__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD09Q1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P8D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD09Q1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Band1'], self.bands['Band2']]

    def getQualityBands(self):
        return [self.bands['BandQuality']]

    bands = dict(Band1={
            'name': 'MOD_Grid_250m_Surface_Reflectance:sur_refl_b01',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_Q1_Refl_Band1_Series',
            'title': '8-Daily Surface Reflectance Band 1',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 1 at 250 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band1',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod09q1_band1',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band1 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band1 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band2={
            'name': 'MOD_Grid_250m_Surface_Reflectance:sur_refl_b02',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_Q1_Refl_Band2_Series',
            'title': '8-Daily Surface Reflectance Band 2',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 2 at 250 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band2',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod09q1_band2',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band2 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band2 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },BandQuality={
            'name': 'MOD_Grid_250m_Surface_Reflectance:sur_refl_qc_250m',
            'nodata': None,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD09_Q1_Refl_BandQuality_Series',
            'title': '8-Daily Surface Reflectance Band Quality',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band quality at 250 m spatial resolution.  Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance Quality',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod09q1_quality',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band Quality 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band Quality 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )