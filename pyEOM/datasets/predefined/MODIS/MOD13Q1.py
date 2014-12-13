__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD13Q1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P16D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD13Q1.005'
    sources = ['LPDAAC','GEE']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['EVI'], self.bands['NDVI']]

    def getQualityBands(self):
        return [self.bands['PR'], self.bands['QC']]

    bands = dict(EVI={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days EVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD13_Q1_EVI_Series',
            'title': '16-daily Enhanced Vegetation Index from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Enhanced Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 250,
            'layername': 'mod13q1_evi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra EVI 16-daily',
            'wms_description': 'MODIS Terra EVI 16-daily',
            'colormap': 'evi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        }, NDVI={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days NDVI',
            'scale': 0.0001,
            'nodata': -3000,
            'imagetype': 'thematicClassification',
            'offset': None,

            'identifier': 'MODIS_MOD13_Q1_NDVI_Series',
            'title': '16-daily Normalized Difference Vegetation Index from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Normalized Difference Vegetation Index',
            'datatype': 'RASTER',
            'resolution': 250,
            'layername': 'mod13q1_ndvi',
            'templates': 'template_header_ndvi.html',
            'wcs_description': 'MODIS Terra NDVI 16-daily',
            'wms_description': 'MODIS Terra NDVI 16-daily',
            'colormap': 'ndvi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        }, PR={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days pixel reliability',
            'scale': 1,
            'nodata': -1,
            'imagetype': 'qualityInformation',
            'offset': None,
            'quality_datatype': 'int',

            'identifier': 'MODIS_MOD13_Q1_PR_Series',
            'title': '16-daily Vegetation Indices Pixel Reliability from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Pixel reliability',
            'datatype': 'RASTER',
            'resolution': 250,
            'layername': 'mod13q1_pr',
            'templates': 'template_header_vi_qc.html',
            'wcs_description': 'MODIS Terra VI Pixel Reliability 16-daily',
            'wms_description': 'MODIS Terra VI Pixel Reliability 16-daily',
            'colormap': 'vi_pr_colormap.map',
            'resolution_unit': 'm',
            'unit': None
        }, QC={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days VI Quality',
            'scale': 1,
            'nodata': 65535,
            'imagetype': 'qualityInformation',
            'offset': None,
            'quality_datatype': 'bit',

            'identifier': 'MODIS_MOD13_Q1_QC_Series',
            'title': '16-daily Vegetation Indices Quality from MODIS Terra',
            'abstract': '',
            'keywords': '',
            'lineage': '',
            'datasetname': 'Quality Flags',
            'datatype': 'RASTER',
            'resolution': 250,
            'layername': 'mod13q1_qc',
            'templates': 'template_header_vi_qc.html',
            'wcs_description': 'MODIS Terra VI Quality 16-daily',
            'wms_description': 'MODIS Terra VI Quality 16-daily',
            'colormap': 'vi_qc_colormap.map',
            'resolution_unit': 'm',
            'unit': None
        }
    )