__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MCD43A3'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P16D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOTA/MCD43A3.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['BSAshortwave'], self.bands['WSAshortwave']]

    def getQualityBands(self):
        return []

    bands = dict(BSAshortwave={
            'name': 'MOD_Grid_BRDF:Albedo_BSA_shortwave',
            'nodata': 32767,
            'scale': 0.0010,
            'offset': None,
            'imagetype': 'physicalMeasurements',

            'identifier': 'MODIS_MCD43_A3_BSAshortwave_Series',
            'title': '16-daily Albedo BSA Shortwave',
            'abstract': 'Time-series of 16-daily Aqua/Terra MODIS Albedo Black Sky Albedo (BSA) from shortwave band at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0010 has to be applied. The unscaled nodata value is encoded as 32767. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOTA/MCD43A3.005).',
            'keywords': 'MODIS,Terra,Aqua,Albedo,BSA,Shortwave,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOTA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Albedo BSA',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mcd43a3_bsa_shortwave',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua/Terra Albedo BSA Shortwave',
            'wms_description': 'MODIS Aqua/Terra Albedo BSA Shortwave',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },WSAshortwave={
            'name': 'MOD_Grid_BRDF:Albedo_WSA_shortwave',
            'nodata': 32767,
            'scale': 0.0010,
            'offset': None,
            'imagetype': 'physicalMeasurements',

            'identifier': 'MODIS_MCD43_A3_WSAshortwave_Series',
            'title': '16-daily Albedo WSA Shortwave',
            'abstract': 'Time-series of 16-daily Aqua/Terra MODIS Albedo White Sky Albedo (WSA) from shortwave band at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0010 has to be applied. The unscaled nodata value is encoded as 32767. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOTA/MCD43A3.005).',
            'keywords': 'MODIS,Terra,Aqua,Albedo,WSA,Shortwave,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOTA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Albedo WSA',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mcd43a3_wsa_shortwave',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua/Terra Albedo WSA Shortwave',
            'wms_description': 'MODIS Aqua/Terra Albedo WSA Shortwave',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )