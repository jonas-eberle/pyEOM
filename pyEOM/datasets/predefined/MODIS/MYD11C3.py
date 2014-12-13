__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD11C3'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1M'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLA/MYD11C3.005'
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
            'name': 'MODIS_MONTHLY_0.05DEG_CMG_LST:LST_Night_CMG',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_C3_LST_Night_Series',
            'title': 'Monthly Nighttime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of monthly Aqua MODIS nighttime land surface temperature in Kelvin at 0.05 deg spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Monthly,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'myd11c3_lst_night',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night Monthly',
            'wms_description': 'MODIS Aqua LST Night Monthly',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'deg',
            'unit': 'None'
        },Daytime={
            'name': 'MODIS_MONTHLY_0.05DEG_CMG_LST:LST_Day_CMG',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_C3_LST_Day_Series',
            'title': 'Monthly Daytime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of monthly Aqua MODIS daytime land surface temperature in Kelvin at 0.05 deg spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Monthly,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'myd11c3_lst_day',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day Monthly',
            'wms_description': 'MODIS Aqua LST Day Monthly',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'deg',
            'unit': 'None'
        }
    )