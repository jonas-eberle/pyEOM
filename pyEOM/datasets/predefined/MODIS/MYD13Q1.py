__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD13Q1'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P16D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLA/MYD13Q1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['EVI'], self.bands['NDVI']]

    def getQualityBands(self):
        return [self.bands['PR'], self.bands['QC']]

    bands = dict(PR={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days pixel reliability',
            'nodata': -1,
            'scale': 1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD13_Q1_PR_Series',
            'title': '16-daily Vegetation Indices Pixel Reliability from MODIS Aqua',
            'abstract': 'Pixel Reliability from time-series of 16-daily Aqua MODIS Vegetation Indices at 250 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Quality,Pixel,Reliability,Vegetation,NDVI,EVI,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Pixel Reliability',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'myd13q1_pr',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua VI Pixel Reliability 16-daily',
            'wms_description': 'MODIS Aqua VI Pixel Reliability 16-daily',
            'colormap': 'vi_pr_colormap.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        },QC={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days VI Quality',
            'nodata': 65535,
            'scale': 1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD13_Q1_QC_Series',
            'title': '16-daily Vegetation Indices Quality from MODIS Aqua',
            'abstract': 'Quality data from time-series of 16-daily Aqua MODIS Vegetation Indices at 250 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Quality,Vegetation,NDVI,EVI,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Quality Flags',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'myd13q1_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua VI Quality 16-daily',
            'wms_description': 'MODIS Aqua VI Quality 16-daily',
            'colormap': 'vi_qc_colormap.map',
            'resolution_unit': 'm',
            'unit': 'Index'
        },NDVI={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days NDVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MYD13_Q1_NDVI_Series',
            'title': '16-daily Normalized Difference Vegetation Index from MODIS Aqua',
            'abstract': 'Time-series of 16-daily Aqua MODIS Normalized Difference Vegetation Index (NDVI) at 250 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/).',
            'keywords': 'MODIS,Aqua,Siberia,NDVI,Normalized Difference Vegetation Index,Vegetation,Index,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Normalized Difference Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'myd13q1_ndvi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua NDVI 16-daily',
            'wms_description': 'MODIS Aqua NDVI 16-daily',
            'colormap': 'ndvi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },EVI={
            'name': 'MODIS_Grid_16DAY_250m_500m_VI:250m 16 days EVI',
            'nodata': -3000,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MYD13_Q1_EVI_Series',
            'title': '16-daily Enhanced Vegetation Index from MODIS Aqua',
            'abstract': 'Time-series of 16-daily Aqua MODIS Enhanced Vegetation Index (EVI) at 250 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/).',
            'keywords': 'MODIS,Aqua,Siberia,EVI,Enhanced Vegetation Index,Vegetation,Index,Global,16-daily,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Enhanced Vegetation Index',
            'datatype': 'RASTER',

            'resolution': 250.0,
            'layername': 'myd13q1_evi',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua EVI 16-daily',
            'wms_description': 'MODIS Aqua EVI 16-daily',
            'colormap': 'evi_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )