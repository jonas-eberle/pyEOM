__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD11A1'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P1D'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Dailies_E/MOLA/MYD11A1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Daytime'], self.bands['Nighttime']]

    def getQualityBands(self):
        return [self.bands['QCDay'], self.bands['QCNight']]

    bands = dict(EmissNight={
            'name': 'MODIS_Grid_Daily_1km_LST:Emis_31',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A1_LST_Night_Series_B31_Emissivity',
            'title': 'Daily Nighttime Land Surface Temperature from MODIS Aqua Band 31 Emissivity',
            'abstract': 'Time-series of daily Aqua MODIS nighttime land surface temperature B31 emissivity without unit at 1 km spatial resolution. Scale factor is 0.002. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_night_b31_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night Daily b31 emiss',
            'wms_description': 'MODIS Aqua LST Night Daily b31 emiss',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },EmissDay={
            'name': 'MODIS_Grid_Daily_1km_LST:Emis_32',
            'nodata': 0,
            'scale': 0.002,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A1_LST_Day_Series_B32_Emissivity',
            'title': 'Daily Daytime Land Surface Temperature from MODIS Aqua Band 32 Emissivity',
            'abstract': 'Time-series of daily Aqua MODIS daytime land surface temperature B32 emissivity without unit at 1 km spatial resolution. Scale factor is 0.002. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_day_b32_emiss',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day Daily b32 emiss',
            'wms_description': 'MODIS Aqua LST Day Daily b32 emiss',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },QCDay={
            'name': 'MODIS_Grid_Daily_1km_LST:QC_Day',
            'nodata': 0,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD11_A1_LST_Day_Series_QC',
            'title': 'Daily Daytime Land Surface Temperature from MODIS Aqua Quality Dataset',
            'abstract': 'Time-series of daily Aqua MODIS daytime land surface temperature Quality Data in Bit (Bit-Field) at 1 km spatial resolution. No scale factor. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_day_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day Daily quality',
            'wms_description': 'MODIS Aqua LST Day Daily quality',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'Bit'
        },Nighttime={
            'name': 'MODIS_Grid_Daily_1km_LST:LST_Night_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A1_LST_Night_Series',
            'title': 'Daily Nighttime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of daily Aqua MODIS nighttime land surface temperature in Kelvin at 1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_night',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night Daily',
            'wms_description': 'MODIS Aqua LST Night Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },Daytime={
            'name': 'MODIS_Grid_Daily_1km_LST:LST_Day_1km',
            'nodata': 0,
            'scale': 0.02,
            'offset': None,
            'imagetype': 'physicalMeasurement',

            'identifier': 'MODIS_MYD11_A1_LST_Day_Series',
            'title': 'Daily Daytime Land Surface Temperature from MODIS Aqua',
            'abstract': 'Time-series of daily Aqua MODIS daytime land surface temperature in Kelvin at 1 km spatial resolution. To retrieve actual values in Kelvin a scale factor of 0.02 has to be applied. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Daytime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_day',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Day Daily',
            'wms_description': 'MODIS Aqua LST Day Daily',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'None'
        },QCNight={
            'name': 'MODIS_Grid_Daily_1km_LST:QC_Night',
            'nodata': 0,
            'scale': None,
            'offset': None,
            'imagetype': 'qualityInformation',

            'identifier': 'MODIS_MYD11_A1_LST_Night_Series_QC',
            'title': 'Daily Nighttime Land Surface Temperature from MODIS Aqua Quality Dataset',
            'abstract': 'Time-series of daily Aqua MODIS nighttime land surface temperature Quality Data in Bit (Bit-Field) at 1 km spatial resolution. No scale factor. The unscaled nodata value is encoded as 0. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLT/).',
            'keywords': 'MODIS,Aqua,Siberia,Temperature,Global,Daily,Series,Nighttime',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOLA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Land Surface Temperature',
            'datatype': 'RASTER',

            'resolution': 1000.0,
            'layername': 'myd11a1_lst_night_qc',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua LST Night Daily quality',
            'wms_description': 'MODIS Aqua LST Night Daily quality',
            'colormap': 'lst_colorbar2.map',
            'resolution_unit': 'm',
            'unit': 'Bit'
        }
    )