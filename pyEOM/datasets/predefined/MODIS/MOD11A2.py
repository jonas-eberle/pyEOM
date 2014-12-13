__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD11A2'
    platform = 'Terra'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P8D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLT/MOD11A2.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Daytime'], self.bands['Nighttime']]

    def getQualityBands(self):
        return [self.bands['QCDay'], self.bands['QCNight']]

    bands = dict(QCDay={
            'name': 'MODIS_Grid_8Day_1km_LST:QC_Day',
            'nodata': None,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_QCDay_Series',
            'title': '8-Daily Land Surface Temperature Quality Daytime from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS daytime quality control of land surface temperature data at 1 km spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Daytime,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_qcday',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST QC Day 8-Daily',
            'wms_description': 'MODIS Terra LST QC Day 8-Daily',
            'colormap': 'lst_qc_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },QCNight={
            'name': 'MODIS_Grid_8Day_1km_LST:QC_Night',
            'nodata': None,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_QCNight_Series',
            'title': '8-Daily Land Surface Temperature Quality Nighttime from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS nighttime quality control of land surface temperature data at 1 km spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Quality',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_qcnight',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST QC Night 8-Daily',
            'wms_description': 'MODIS Terra LST QC Night 8-Daily',
            'colormap': 'lst_qc_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },DayViewtime={
            'name': 'MODIS_Grid_8Day_1km_LST:Day_view_time',
            'nodata': 0,
            'scale': 0.1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_DayViewTime_Series',
            'title': '8-Daily Land Surface Temperature Day Viewtime from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS day view time of land surface temperature data at 1 km spatial resolution. To retrieve actual values in Hours a scale factor of 0.1 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Daytime,Viewtime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_dayviewtime',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Day Viewtime 8-Daily',
            'wms_description': 'MODIS Terra LST Day Viewtime 8-Daily',
            'colormap': 'lst_viewtime_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },EmissNight={
            'name': 'MODIS_Grid_8Day_1km_LST:Emis_31',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_A2_LST_Night_Series_B31_Emissivity',
            'title': '8-Daily Nighttime Land Surface Temperature from MODIS Terra Band 31 Emissivity',
            'abstract': 'Time-series of 8-daily Terra MODIS nighttime land surface temperature B31 emissivity without unit at 1 km spatial resolution. Scale factor is 0.0020 (+0.49). The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Emissivity,B31',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature B31',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_b31_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night 8- Daily b31 emiss',
            'wms_description': 'MODIS Terra LST Night 8- Daily b31 emiss',
            'colormap': 'lst_emiss_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },EmissDay={
            'name': 'MODIS_Grid_8Day_1km_LST:Emis_32',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_A2_LST_Day_Series_B32_Emissivity',
            'title': '8-Daily Daytime Land Surface Temperature from MODIS Terra Band 32 Emissivity',
            'abstract': 'Time-series of 8-daily Terra MODIS daytime land surface temperature B32 emissivity without unit at 1 km spatial resolution. Scale factor is 0.0020 (+0.49). The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Emissivity,B32',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature B32',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_b32_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night 8- Daily b32 emiss',
            'wms_description': 'MODIS Terra LST Night 8- Daily b32 emiss',
            'colormap': 'lst_emiss_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },NightViewtime={
            'name': 'MODIS_Grid_8Day_1km_LST:Night_view_time',
            'nodata': 0,
            'scale': 0.1,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_NightViewTime_Series',
            'title': '8-Daily Land Surface Temperature Night Viewtime from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS night view time of land surface temperature data at 1 km spatial resolution. To retrieve actual values in Hours a scale factor of 0.1 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Viewtime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_nightviewtime',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night Viewtime 8-Daily',
            'wms_description': 'MODIS Terra LST Night Viewtime 8-Daily',
            'colormap': 'lst_viewtime_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },DayViewangle={
            'name': 'MODIS_Grid_8Day_1km_LST:Day_view_angl',
            'nodata': 255,
            'scale': 1.0,
            'offset': -65.0,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_DayViewangle_Series',
            'title': '8-Daily Land Surface Temperature Day Viewangle from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS day view angle of land surface temperature data at 1 km spatial resolution. To retrieve actual values in Degrees an offset value of -65.0 has to be applied. The nodata value is encoded as 255. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Daytime,Viewangle',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_dayviewangle',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Day Viewangle 8-Daily',
            'wms_description': 'MODIS Terra LST Day Viewangle 8-Daily',
            'colormap': 'lst_viewangle_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },NightViewangle={
            'name': 'MODIS_Grid_8Day_1km_LST:Night_view_angl',
            'nodata': 255,
            'scale': 1.0,
            'offset': -65.0,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MOD11_A2_LST_NightViewangle_Series',
            'title': '8-Daily Land Surface Temperature Night Viewangle from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS night view angle of land surface temperature data at 1 km spatial resolution. To retrieve actual values in Degrees an offset value of -65.0 has to be applied. The nodata value is encoded as 255. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Viewangle',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (http://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_nightviewangle',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night Viewangle 8-Daily',
            'wms_description': 'MODIS Terra LST Night Viewangle 8-Daily',
            'colormap': 'lst_viewangle_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },Nighttime={
            'name': 'MODIS_Grid_8Day_1km_LST:LST_Night_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_A2_LST_Night_Series',
            'title': '8-Daily Nighttime Land Surface Temperature from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS nighttime land surface temperature in Kelvin at 1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_night',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Night8- Daily',
            'wms_description': 'MODIS Terra LST Night8- Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        },Daytime={
            'name': 'MODIS_Grid_8Day_1km_LST:LST_Day_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MOD11_A2_LST_Day_Series',
            'title': '8-Daily Daytime Land Surface Temperature from MODIS Terra',
            'abstract': 'Time-series of 8-daily Terra MODIS daytime land surface temperature in Kelvin at 1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Terra,Siberia,Temperature,Global,8-Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'mod11a2_lst_day',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra LST Day 8-Daily',
            'wms_description': 'MODIS Terra LST Day 8-Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'Kelvin'
        }
    )