__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MYD10CM'
    platform = 'Aqua'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1M'

    host = 'n5eil01u.ecs.nsidc.org'
    dir = '/SAN/MOSA/MYD10CM.005'
    sources = ['NSIDC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Snowcover']]

    def getQualityBands(self):
        return []

    bands = dict(Snowcover={
            'name': 'MOD_CMG_Snow_5km:Snow_Cover_Monthly_CMG',
            'nodata': 255,
            'scale': 1,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MYD10_CM_SnowCover_Series',
            'title': 'Monthly Snow Cover from MODIS Aqua',
            'abstract': 'Time-series of monthly Aqua MODIS Snow Cover at 0.05 deg spatial resolution. Available classes are: No Snow, Snow (in percent), Cloud, No decision, Water Mask. Original MODIS data retrieved from the National Snow &amp; Ice Data Center (ftp://n4ftl01u.ecs.nasa.gov/SAN/MOSA/).',
            'keywords': 'MODIS,Aqua,Siberia,Snow,Snow Cover,Global,Monthly,Series,Classification',
            'lineage': 'Original MODIS data retrieved from the National Snow &amp; Ice Data Center (ftp://n4ftl01u.ecs.nasa.gov/SAN/MOSA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Snow Cover',
            'datatype': 'RASTER',

            'resolution': 0.05,
            'layername': 'myd10cm_snowcover',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Aqua Snow Cover Monthly',
            'wms_description': 'MODIS Aqua Snow Cover Monthly',
            'colormap': 'snow_colorbar.map',
            'resolution_unit': 'deg',
            'unit': 'None'
        }
    )