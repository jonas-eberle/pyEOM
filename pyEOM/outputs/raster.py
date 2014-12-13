__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'


from pyspatialite import dbapi2 as db
import os
import sys
from osgeo import gdal
import ogr
from datetime import datetime

class Raster(object):
    file = None
    xsize = None
    ysize = None
    bbox = None

    def __init__(self, file):
        self.file = file
        ds = gdal.Open(file)
        self.xsize = ds.RasterXSize
        self.ysize = ds.RasterYSize
        ds = None

    def getFile(self):
        return self.file

    def getFilename(self):
        return os.path.basename(self.file)

    def getDirectory(self):
        return os.path.dirname(self.file)

    def provideOGC(self):
        pass


class TSRaster(object):
    files = []
    dates = []
    path = None
    mergedFile = None
    epsg = None

    """
    rasterInfo - Dictionary for specific raster options:
    - rows
    - cols
    - nodata
    - scale
    - offset
    - geom
    """
    rasterInfo = dict()

    def __init__(self, name, dataset, path, rasterInfo=None):
        self.name = name
        self.dataset = dataset
        self.path = path
        self.files = []
        self.dates = []
        self.epsg = 4326
        self.mergedFile = None
        if isinstance(rasterInfo, dict):
            self.setRasterInfo(rasterInfo)

    def setRasterInfo(self, rasterInfo):
        for key, val in rasterInfo.items():
            self.rasterInfo[key] = val
        return rasterInfo

    def addEntry(self, date, file):
        self.files.append(Raster(file))
        self.dates.append(date)

    def setMergedFile(self, file):
        self.mergedFile = file

    def getBoundingBox(self):
        if 'geom' not in self.rasterInfo:
            raise Exception('No Geometry available')
            return
        geom = ogr.CreateGeometryFromWkt(self.rasterInfo['geom'])
        bounds = geom.GetEnvelope()
        return bounds

    def saveToDB(self, filename):
        if  os.path.exists(filename):
            raise Exception('File already exists')
            sys.exit(1)
        conn = db.connect(filename)
        cur = conn.cursor()
        cur.execute("SELECT InitSpatialMetaData();")
        cur.execute("CREATE TABLE tsraster (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, file TEXT NOT NULL, date TEXT NOT NULL)")
        cur.execute("SELECT AddGeometryColumn('tsraster', 'the_geom', "+str(self.epsg)+", 'POLYGON', 'XY');")
        conn.commit()

        for key, file in enumerate(self.files):
            date = datetime.strptime(self.dates[key], '%Y.%m.%d')
            filename = file.getFile()
            cur.execute("INSERT INTO tsraster (file, date, the_geom) VALUES ('%s', '%s', GeomFromText('%s', %i))" % (filename, date, self.rasterInfo['geom'], self.epsg))
        conn.commit()
        conn.close()

    def provideOGC(self, directory, datasetname):
        self.saveToDB(directory+'/'+datasetname+'.sqlite')
        pass

class MapServer(object):
    url = None

class Geoserver(object):
    url = None

