__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD10A2'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P8D'
    documentation = 'http://nsidc.org/data/docs/daac/mod10_modis_snow/version_5/mod10a2_local_attributes.html'

    host = 'n5eil01u.ecs.nsidc.org'
    dir = '/SAN/MOST/MOD10A2.005/'
    sources = ['NSIDC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['SnowCover'], self.bands['MaxSnowExtent']]

    def getQualityBands(self):
        return []

    bands = dict(SnowCover={
            'name': 'MOD_Grid_Snow_500m:Eight_Day_Snow_Cover',
            'nodata': 255,
            'scale': 1,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD10_A2_SnowCover_Series',
            'title': '8-daily Snow Cover from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Snow Cover',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a2_snowcover',
            'templates': 'template_header_snow.html',
            'wcs_description': 'MODIS Terra Snow Cover 8-daily',
            'wms_description': 'MODIS Terra Snow Cover 8-daily',
            'colormap': 'snow_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        }, MaxSnowExtent={
            'name': 'MOD_Grid_Snow_500m:Maximum_Snow_Extent',
            'scale': 1,
            'nodata': 255,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD10_A2_MaxSnowExtent_Series',
            'title': '8-daily Maximum Snow Extent from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Maximum Snow Extent',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a2_snowextent',
            'templates': 'template_header_snowextent.html',
            'wcs_description': 'MODIS Terra Max Snow Extent 8-daily',
            'wms_description': 'MODIS Terra Max Snow Extent 8-daily',
            'colormap': 'snowextent_colorbar.map',
            'resolution_unit': 'm',
            'unit': ''
        }
    )