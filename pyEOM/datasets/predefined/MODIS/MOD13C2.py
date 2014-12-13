__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD13C2'
    platform = 'Terra'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1M'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD13C2.005'
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
            'name': 'MOD_Grid_monthly_CMG_VI:CMG 0.05 Deg Monthly NDVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD13_C2_NDVI_Series',
            'title': 'Monthly Normalized Difference Vegetation Index from MODIS Terra',
            'abstract': 'Time-series of monthly Terra MODIS Normalized Difference Vegetation Index (NDVI) at 0.05 deg spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,NDVI,Normalized Difference Vegetation Index,Vegetation,Index,Global,Monthly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Normalized Difference Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'mod13c2_ndvi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra NDVI Monthly',
            'wms_description': 'MODIS Terra NDVI Monthly',
            'colormap': 'ndvi_colorbar.map',
            'resolution_unit': 'deg',
            'unit': 'Index'
        },EVI={
            'name': 'MOD_Grid_monthly_CMG_VI:CMG 0.05 Deg Monthly EVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD13_C2_EVI_Series',
            'title': 'Monthly Enhanced Vegetation Index from MODIS Terra',
            'abstract': 'Time-series of monthly Terra MODIS Enhanced Vegetation Index (EVI) at 0.05 deg spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,EVI,Enhanced Vegetation Index,Vegetation,Index,Global,Monthly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Enhanced Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'mod13c2_evi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra EVI Monthly',
            'wms_description': 'MODIS Terra EVI Monthly',
            'colormap': 'evi_colorbar.map',
            'resolution_unit': 'deg',
            'unit': 'Index'
        }
    )