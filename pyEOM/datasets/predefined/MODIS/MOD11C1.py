__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD11C1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Dailies_F/MOLT/MOD11C1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Daytime'], self.bands['Nighttime']]

    def getQualityBands(self):
        return []

    bands = dict(Nighttime={
            'name': 'MODIS_CMG_3MIN_LST:LST_Night_CMG',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_C1_LST_Night_Series',
            'title': 'Daily Nighttime Land Surface Temperature from MODIS Terra',
            'abstract': 'Time-series of daily Terra MODIS nighttime land surface temperature in Kelvin at 0.05 deg spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'mod11c1_lst_night',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night Daily',
            'wms_description': 'MODIS Terra LST Night Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'deg',
            'unit': 'Kelvin'
        },Daytime={
            'name': 'MODIS_CMG_3MIN_LST:LST_Day_CMG',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_C1_LST_Day_Series',
            'title': 'Daily Daytime Land Surface Temperature from MODIS Terra',
            'abstract': 'Time-series of daily Terra MODIS daytime land surface temperature in Kelvin at 0.05 deg spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'mod11c1_lst_day',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Day Daily',
            'wms_description': 'MODIS Terra LST Day Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'deg',
            'unit': 'Kelvin'
        }
    )