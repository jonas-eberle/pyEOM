__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD44B'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P1Y'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD44B.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['PercentTreeCover']]

    def getQualityBands(self):
        return [self.bands['QualtiyDataset'], self.bands['CloudDataset']]

    bands = dict(PercentTreeCover={
            'name': 'MOD44B_250m_GRID:Percent_Tree_Cover',
            'nodata': 253,
            'scale': 1,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD44_B_TreeCover_Series',
            'title': 'Yearly VCF Tree Cover Percentage from MODIS Terra',
            'abstract': 'Tree Cover Percentage from time-series of yearly Terra MODIS VCF at 250 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,VCF,Tree,Cover,Global,yearly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Percent Tree Cover',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod44b_tc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra VCF Percent Tree Cover Yearly',
            'wms_description': 'MODIS Terra VCF Percent Tree Cover Yearly',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },QualtiyDataset={
            'name': 'MOD44B_250m_GRID:Quality',
            'nodata': None,
            'scale': 1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD44_B_Quality_Series',
            'title': 'Yearly VCF Quality Dataset from MODIS Terra',
            'abstract': 'VCF Quality Dataset from time-series of yearly Terra MODIS VCF at 250 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,VCF,Quality,Global,yearly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'VCF Quality',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod44b_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra VCF Yearly Quality',
            'wms_description': 'MODIS Terra VCF Yearly Quality',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },CloudDataset={
            'name': 'MOD44B_250m_GRID:Cloud',
            'nodata': None,
            'scale': 1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD44_B_Cloud_Series',
            'title': 'Yearly VCF Cloud Dataset from MODIS Terra',
            'abstract': 'VCF Cloud Dataset from time-series of yearly Terra MODIS VCF at 250 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,VCF,Cloud,Global,yearly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'VCF Cloud',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'mod44b_cloud',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra VCF Yearly Cloud',
            'wms_description': 'MODIS Terra VCF Yearly Cloud',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )