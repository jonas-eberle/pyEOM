__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD09A1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P8D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD09A1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Band1'], self.bands['Band2'], self.bands['Band3'], self.bands['Band4'], self.bands['Band5'], self.bands['Band6'], self.bands['Band7']]

    def getQualityBands(self):
        return [self.bands['Quality'], self.bands['StateFlags']]

    bands = dict(Band1={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b01',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band1',
            'title': '8-Daily Surface Reflectance Band 1',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 1 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band1',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band1',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 1 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 1 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band2={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b02',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band2',
            'title': '8-Daily Surface Reflectance Band 2',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 2 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band2',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band2',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 2 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 2 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band3={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b03',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band3',
            'title': '8-Daily Surface Reflectance Band 3',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 3 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band3',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band3',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 3 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 3 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band4={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b04',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band4',
            'title': '8-Daily Surface Reflectance Band 4',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 4 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band4',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band4',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 4 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 4 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band5={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b05',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band5',
            'title': '8-Daily Surface Reflectance Band 5',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 5 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band5',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band5',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 5 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 5 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band6={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b06',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band6',
            'title': '8-Daily Surface Reflectance Band 6',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 6 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band6',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band6',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 6 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 6 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Band7={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_b07',
            'nodata': -28672,
            'scale': 0.0001,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD09_A1_Refl_Band7',
            'title': '8-Daily Surface Reflectance Band 7',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band 7 at 500 m spatial resolution. To retrieve actual values a scale factor of 0.0001 has to be applied. The unscaled nodata value is encoded as -28672. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Band7',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_band7',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band 7 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band 7 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },Quality={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_qc_500m',
            'nodata': 4294967295,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD09_A1_Refl_BandQuality',
            'title': '8-Daily Surface Reflectance Band Quality',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance band quality at 500 m spatial resolution. The nodata value is encoded as 4294967295. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Surface Reflectance',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_quality',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Band Quality 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Band Quality 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        },StateFlags={
            'name': 'MOD_Grid_500m_Surface_Reflectance:sur_refl_state_500m',
            'nodata': 65535,
            'scale': None,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD09_A1_Refl_DataStateFlags',
            'title': '8-Daily Surface Reflectance Data State Flags',
            'abstract': 'Time-series of 8-daily Terra MODIS surface reflectance data state flags at 500 m spatial resolution. The nodata value is encoded as 65535. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Surface,Reflectance,Global,8-Daily,Series,State,Flags',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Data State Flags',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mod09a1_stateflags',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Surface Reflectance Data State Flags 8-Daily',
            'wms_description': 'MODIS Terra Surface Reflectance Data State Flags 8-Daily',
            'colormap': 'None',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )