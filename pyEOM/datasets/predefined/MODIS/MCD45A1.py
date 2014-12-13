__author__ = 'we32zac'

from pyEOM.datasets import Dataset as DatasetAbs


class Dataset(DatasetAbs):
    shortname = 'MCD45A1'
    platform = 'Combined'
    collection = '005'
    rastertype = 'Tile'
    timeInterval = 'P1M'

    host = 'http://e4ftl01.cr.usgs.gov'
    dir = '/MODIS_Composites/MOTA/MCD45A1.005'
    sources = ['LPDAAC']

    def getDownloadInfo(self):
        return dict(shortname=self.shortname, platform=self.platform, collection=self.collection, rastertype=self.rastertype, host=self.host, directory=self.dir, sources=self.sources)

    def getBands(self):
        return self.bands

    def getThematicBands(self):
        return [self.bands['Burndate']]

    def getQualityBands(self):
        return []

    bands = dict(Burndate={
            'name': 'MOD_GRID_Monthly_500km_BA:burndate',
            'nodata': 11111,
            'scale': None,
            'offset': None,
            'imagetype': 'thematicClassification',

            'identifier': 'MODIS_MCD45_A1_BurntArea_Date_Series',
            'title': 'Monthly Burnt Area Date from MODIS Aqua and Terra',
            'abstract': 'Time-series of monthly MODIS Aqua and Terra Burnt Area at 500 m spatial resolution. Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOTA/).',
            'keywords': 'Modis,Aqua,Terra,Siberia,Burnt Area,Fire,Global,Monthly,Series',
            'lineage': 'Original MODIS data retrieved from the Land Processes Distributed Active Archive Center (ftp://e4ftl01.cr.usgs.gov/MOTA/) and processed with GDAL 1.9.0.',
            'datasetname': 'Burnt Area',
            'datatype': 'RASTER',

            'resolution': 500.0,
            'layername': 'mcd45a1_burndate',
            'templates': 'template_header_evi.html',
            'wcs_description': 'MODIS Combined Burnt Area Date Monthly',
            'wms_description': 'MODIS Combined Burnt Area Date Monthly',
            'colormap': 'burntarea_colorbar.map',
            'resolution_unit': 'm',
            'unit': 'None'
        }
    )