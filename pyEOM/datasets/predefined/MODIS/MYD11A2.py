__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD11A2'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P8D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOLA/MYD11A2.005'
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
            'nodata': 0,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD11_A2_LST_Night_Series',
            'title': '8-Daily Daytime Land Surface Temperature from MODIS Aqua Quality Dataset',
            'abstract': 'Time-series of 8-daily Aqua MODIS daytime land surface temperature Quality Data in Bit (Bit-Field) at 1 km spatial resolution. No scale factor. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Daytime,Quality Dataset',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature Quality Dataset',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_day_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day 8-Daily quality',
            'wms_description': 'MODIS Aqua LST Day 8-Daily quality',
            'colormap': 'lst_qc_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Bit'
        },QCNight={
            'name': 'MODIS_Grid_8Day_1km_LST:QC_Night',
            'nodata': 0,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD11_A2_LST_Night_Series',
            'title': '8-Daily Nighttime Land Surface Temperature from MODIS Aqua Quality Dataset',
            'abstract': 'Time-series of 8-daily Aqua MODIS nighttime land surface temperature Quality Data in Bit (Bit-Field) at 1 km spatial resolution. No scale factor. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Quality Dataset',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature Quality Dataset',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_night_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night 8- Daily quality',
            'wms_description': 'MODIS Aqua LST Night 8- Daily quality',
            'colormap': 'lst_qc_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'Bit'
        },EmissNight={
            'name': 'MODIS_Grid_8Day_1km_LST:Emis_31',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A2_LST_Night_Series_B31_Emissivity',
            'title': '8-Daily Nighttime Land Surface Temperature from MODIS Aqua Band 31 Emissivity',
            'abstract': 'Time-series of 8-daily Aqua MODIS nighttime land surface temperature B31 emissivity without unit at 1 km spatial resolution. Scale factor is 0.0020 (+0.49). The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Emissivity,B31',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature B31',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_b31_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night 8- Daily b31 emiss',
            'wms_description': 'MODIS Aqua LST Night 8- Daily b31 emiss',
            'colormap': 'lst_emiss_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },EmissDay={
            'name': 'MODIS_Grid_8Day_1km_LST:Emis_32',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A2_LST_Day_Series_B32_Emissivity',
            'title': '8-Daily Daytime Land Surface Temperature from MODIS Aqua Band 32 Emissivity',
            'abstract': 'Time-series of 8-daily Aqua MODIS daytime land surface temperature B32 emissivity without unit at 1 km spatial resolution. Scale factor is 0.0020 (+0.49). The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Nighttime,Emissivity,B32',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature B32',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_b32_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night 8- Daily b32 emiss',
            'wms_description': 'MODIS Aqua LST Night 8- Daily b32 emiss',
            'colormap': 'lst_emiss_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },Nighttime={
            'name': 'MODIS_Grid_8Day_1km_LST:LST_Night_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A2_LST_Night_Series',
            'title': '8-Daily Nighttime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of 8-daily Aqua MODIS nighttime land surface temperature in Kelvin at1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_night',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night 8-Daily',
            'wms_description': 'MODIS Aqua LST Night 8-Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },Daytime={
            'name': 'MODIS_Grid_8Day_1km_LST:LST_Day_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A2_LST_Day_Series',
            'title': '8-Daily Daytime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of 8-daily Aqua MODIS daytime land surface temperature in Kelvin at 1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,8-Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a2_lst_day',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day 8-Daily',
            'wms_description': 'MODIS Aqua LST Day 8-Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )