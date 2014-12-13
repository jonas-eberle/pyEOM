__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD13A2'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P16D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLA/MYD13A2.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['EVI'], self.bands['NDVI']]

    def getQualityBands(self):
        return []

    bands = dict(NDVI={
            'name': 'MODIS_Grid_16DAY_1km_VI:1 km 16 days NDVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MYD13_A2_NDVI_Series',
            'title': '16-daily Normalized Difference Vegetation Index from MODIS Aqua',
            'abstract': 'Time-series of 16-daily Aqua MODIS Normalized Difference Vegetation Index (NDVI) at 1 km spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,NDVI,Normalized Difference Vegetation Index,Vegetation,Index,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Normalized Difference Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd13a2_ndvi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua NDVI 16-daily',
            'wms_description': 'MODIS Aqua NDVI 16-daily',
            'colormap': 'ndvi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },EVI={
            'name': 'MODIS_Grid_16DAY_1km_VI:1 km 16 days EVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MYD13_A2_EVI_Series',
            'title': '16-daily Enhanced Vegetation Index from MODIS Aqua',
            'abstract': 'Time-series of 16-daily Aqua MODIS Enhanced Vegetation Index (EVI) at 1 km spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,EVI,Enhanced Vegetation Index,Vegetation,Index,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Enhanced Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd13a2_evi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua EVI 16-daily',
            'wms_description': 'MODIS Aqua EVI 16-daily',
            'colormap': 'evi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )