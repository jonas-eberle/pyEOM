__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MOD10CM'
    platform = 'Terra'
    collection = '005'
    rastertype = 'CMG'
    timeInterval = 'P1M'
    documentation = 'http://nsidc.org/data/docs/daac/mod10_modis_snow/version_5/mod10cm_local_attributes.html'

    host = 'n5eil01u.ecs.nsidc.org'
    dir = '/SAN/MOST/MOD10CM.005/'
    sources = ['NSIDC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['SnowCover']]

    def getQualityBands(self):
        return [self.bands['SnowQA']]

    bands = dict(SnowCover={
            'name': 'MOD_CMG_Snow_5km:Snow_Cover_Monthly_CMG',
            'nodata': 255,
            'scale': 1,
            'imagetype': 'thematicClassification',
            'offset': None
        }, SnowQA={
            'name': 'MOD_CMG_Snow_5km:Snow_Spatial_QA',
            'scale': 1,
            'nodata': 255,
            'imagetype': 'qualityInformation',
            'offset': None,
            'quality_datatype': 'int'
        }
    )