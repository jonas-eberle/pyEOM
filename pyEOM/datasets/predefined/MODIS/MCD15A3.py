__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MCD15A3'
    platform = 'Combined'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P4D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOTA/MCD15A3.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['FPAR'], self.bands['LAI']]

    def getQualityBands(self):
        return [self.bands['FPARQuality'], self.bands['FparLaiQuality']]

    bands = dict(FPAR={
            'name': 'MOD_Grid_MOD15A2:Fpar_1km',
            'nodata': None,
            'scale': 0.01,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MCD15_A3_ Fpar_1km',
            'title': '4-daily Fraction of Photosynthetically Active Radiation (combined)',
            'abstract': 'Time-series of 4-daily Combined MODIS FPAR at 1000 m spatial resolution. To retrieve actual values a scale factor of 0.01 has to be applied. Valid range is 0-100. The unscaled nodata value is encoded as  249-255.',
            'keywords': 'MODIS,FPAR',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Fraction of Photosynthetically Active Radiation',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mcd15a3_fpar',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Combined FPAR 4-daily',
            'wms_description': 'MODIS Combined FPAR 4-daily',
            'colormap': 'fpar_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Percent'
        },LAI={
            'name': 'MOD_Grid_MOD15A2:Lai_1km',
            'nodata': None,
            'scale': 0.1,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MCD15_A3_Lai_1km',
            'title': '4-daily Leaf Area Index (combined)',
            'abstract': 'Time-series of 4-daily Combined MODIS LAI at 1000 m spatial resolution. To retrieve actual values a scale factor of 0.1 has to be applied. Valid range is 0-100. The unscaled nodata value is encoded as  249-255.',
            'keywords': 'MODIS,LAI',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Leaf Area Index',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mcd15a3_lai',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Combined LAI 4-daily',
            'wms_description': 'MODIS Combined LAI 4-daily',
            'colormap': 'lai_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'm2plant'
        },FPARQuality={
            'name': 'MOD_Grid_MOD15A2:FparExtra_QC',
            'nodata': None,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MCD15_A3_FparExtra_QC',
            'title': '4-daily Fraction of Photosynthetically Active Radiation Quality Dataset (combined)',
            'abstract': 'Time-series of 4-daily Combined MODIS FPAR Quality dataset at 1000 m spatial resolution. Valid range is 0-100. The unscaled nodata value is encoded as  248-255.',
            'keywords': 'MODIS,FPAR,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'FPAR extra Quality',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mcd15a3_fpar_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Combined FPAR 4-daily quality',
            'wms_description': 'MODIS Combined FPAR 4-daily quality',
            'colormap': 'fpar_qc_color.map',
            'resolution_unit': 'm',
            'unit': 'ClassFlag'
        },FparLaiQuality={
            'name': 'MOD_Grid_MOD15A2:FparLai_QC',
            'nodata': 255,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MCD15_A3_FparLai_QC',
            'title': '4-daily Fraction of Photosynthetically Active Radiation and Leaf Area Index Quality Dataset (combined)',
            'abstract': 'Time-series of 4-daily Combined MODIS FPAR and LAI Quality dataset at 1000 m spatial resolution. Valid range is 0-254. The unscaled nodata value is encoded as  255.',
            'keywords': 'MODIS,FPAR,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'FPAR and LAI Quality',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mcd15a3_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Combined FPAR LAI 4-daily quality',
            'wms_description': 'MODIS Combined FPAR LAI 4-daily quality',
            'colormap': 'fpar_lai_qc_color.map',
            'resolution_unit': 'm',
            'unit': 'ClassFlag'
        }
    )