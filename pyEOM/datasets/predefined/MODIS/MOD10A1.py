__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD10A1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P1D'
    documentation = 'http://nsidc.org/data/docs/daac/mod10_modis_snow/version_5/mod10a1_local_attributes.html'

    host = 'n5eil01u.ecs.nsidc.org'
    dir = '/SAN/MOST/MOD10A1.005/'
    sources = ['NSIDC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['SnowCover'], self.bands['SnowAlbedo'], self.bands['FractSnowCover']]

    def getQualityBands(self):
        return [self.bands['SnowQA']]

    bands = dict(SnowCover={
            'name': 'MOD_Grid_Snow_500m:Snow_Cover_Daily_Tile',
            'nodata': 255,
            'scale': 1,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD10_A1_SnowCover_Series',
            'title': 'Daily Snow Cover from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Snow Cover',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a1_snowcover',
            'templates': 'template_header_snow.html',
            'wcs_description': 'MODIS Terra Snow Cover Daily',
            'wms_description': 'MODIS Terra Snow Cover Daily',
            'colormap': 'snow_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        }, SnowQA={
            'name': 'MOD_Grid_Snow_500m:Snow_Spatial_QA',
            'scale': 1,
            'nodata': 255,
            'imagetype': 'qualityInformation',
            'offset': None,
            'quality_datatype': 'int',

            'identifier': 'MODIS_MOD10_A2_SnowSpatialQA_Series',
            'title': 'Daily Snow Spatial QA from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Snow Spatial QA',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a1_snowspatialqa',
            'templates': 'template_header_snowspatialqa.html',
            'wcs_description': 'MODIS Terra Snow Spatial QA Daily',
            'wms_description': 'MODIS Terra Snow Spatial QA Daily',
            'colormap': 'snowspatialqa_colorbar.map',
            'resolution_unit': 'm',
            'unit': ''
        }, SnowAlbedo={
            'name': 'MOD_Grid_Snow_500m:Snow_Albedo_Daily_Tile',
            'scale': 1,
            'nodata': -6,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD10_A2_SnowAlbedo_Series',
            'title': 'Daily Snow Albedo from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Snow Albedo',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a1_snowalbedo',
            'templates': 'template_header_snowalbedo.html',
            'wcs_description': 'MODIS Terra Snow Albedo Daily',
            'wms_description': 'MODIS Terra Snow Albedo Daily',
            'colormap': 'snowalbedo_colorbar.map',
            'resolution_unit': 'm',
            'unit': ''
        }, FractSnowCover={
            'name': 'MOD_Grid_Snow_500m:Fractional_Snow_Cover',
            'scale': 1,
            'nodata': 255,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD10_A2_FractSnowCover_Series',
            'title': 'Daily Fractional Snow Cover from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Fractional Snow Cover',
            'datatype': 'RASTER',
            'resolution': 500,
            'layername': 'mod10a1_factsnowcover',
            'templates': 'template_header_factsnowcover.html',
            'wcs_description': 'MODIS Terra Fractional Snow Cover Daily',
            'wms_description': 'MODIS Terra Fractional Snow Cover Daily',
            'colormap': 'factsnowcover_colorbar.map',
            'resolution_unit': 'm',
            'unit': ''
        }
    )