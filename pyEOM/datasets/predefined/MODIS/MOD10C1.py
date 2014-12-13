__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD10C1'
    platform = 'Terra'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1D'

    host = 'n5eil01u.ecs.nsidc.org'
    dir = '/SAN/MOST/MOD10C1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Snowcover']]

    def getQualityBands(self):
        return []

    bands = dict(Snowcover={
            'name': 'MOD_CMG_Snow_5km:Day_CMG_Snow_Cover',
            'nodata': 255,
            'scale': 1,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MOD10_C1_SnowCover_Series',
            'title': 'Daily Snow Cover from MODIS Terra',
            'abstract': 'Time-series of daily Terra MODIS Snow Cover at 0.05 deg spatial resolution. Available classes are: No Snow, Snow (in percent), Cloud, No decision, Water Mask. Original MODIS data retrieved from the National Snow &amp; Ice Data Center (ftp://n4ftl01u.ecs.nasa.gov/SAN/MOST/).',
            'keywords': 'MODIS,Terra,Siberia,Snow,Snow Cover,Global,daily,Series,Classification',
            'lineage': 'Original MODIS data retrieved from the National Snow &amp; Ice Data Center (ftp://n4ftl01u.ecs.nasa.gov/SAN/MOST/) and processed with GDAL 1.9.0.',
            'datasetname': 'Snow Cover',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'mod10c1_snowcover',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Terra Snow Cover daily',
            'wms_description': 'MODIS Terra Snow Cover daily',
            'colormap': 'snow_colorbar.map',
            'resolution_unit': 'deg',
            'unit': 'None'
        }
    )