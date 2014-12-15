__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'

import pyEOM.gee_init as gee
import ee
import sys
import ogr

def TestGEESource():
    source = GEESource()
    source.connect()

    geometry = source.getEEPoint(11, 51)
    scenes = source.listScenes("LANDSAT/LC8_L1T", geometry, '2014-11-01', '2014-12-11')
    print scenes
    return scenes

class GEESource(object):
    user = None

    def __init__(self, username=None, password=None):
        if username != None and password != None:
            self.connect(username, password)

    def connect(self, username=None, password=None):
        if gee.MY_SERVICE_ACCOUNT != '' and gee.MY_PRIVATE_KEY_FILE != '':
            ee.Initialize(ee.ServiceAccountCredentials(gee.MY_SERVICE_ACCOUNT, gee.MY_PRIVATE_KEY_FILE))
        elif username != None and password != None:
            pass
        else:
            raise Exception('No valid user authentication found')

    def processGeometry(self, wkt):
        if 'POINT' in wkt:
            geom = ogr.CreateGeometryFromWkt(wkt)
            return self.getEEPoint(geom.GetX(), geom.GetY())
        elif 'POLYGON' in wkt:
            return self.getEEPolygon(wkt)
        else:
            raise Exception('Wrong geometry type (either POINT or POLYGON necessary)')
            sys.exit(1)

    def getEEPoint(self, x, y):
        return ee.Geometry.Point(x, y)

    def getEEPolygon(self, wkt):
        polygon = wkt.replace('POLYGON((','').replace('))','').split(',')
        vertices = []
        for vertix in polygon:
            lon, lat = vertix.split(' ')
            vertices.append([float(lon), float(lat)])
        return ee.Geometry.Polygon(vertices)

    def getData(self, dataset, bands, eeGeometry, start, end, epsg='SR-ORG:6974', scale=None, crsTransform=None):
        collection = ee.ImageCollection(dataset).filterDate(start, end).filterBounds(eeGeometry)
        if bands != None:
            if isinstance(bands, basisstring):
                bands = [bands]
            collection = collection.select(bands)
        if crsTransform == True:
            image = collection.first().getInfo()
            crsTransform = image['bands'][0]['crs_transform']
        try:
            data = collection.getRegion(eeGeometry, scale, epsg, crsTransform).getInfo()
        except Exception, e:
            raise e
            #if e.message['code'] == 400 and "Too many values" in e.message['message']:
            #    LOGGER.info('Too many pixels in polygon: '+e.message['message'])
            #
            #    msgAr = e.message['message'].split(' ')
            #    points = int(msgAr[msgAr.index('points')-1])
            #    bands = int(msgAr[msgAr.index('bands')-1])
            #    images = int(msgAr[msgAr.index('images')-1])
            #    limit = 1048576
            #else:
            #    raise e
            #    sys.exit(1)

        return data

    def reduceRegion(self):
        pass

    def download(self, image, path):
        urls = []
        if isinstance(image, ee.Image):
            urls.append(image.getDownloadUrl())
        elif isinstance(image, ee.ImageCollection):
            for item in image:
                urls.append(item.getDownloadUrl())
        else:
            raise Exception('Wrong object type for image parameter')
            sys.exit(1)

        localFiles = []
        filepath = path+'/'+url.split('/')[-1]
        for url in urls:
            LOGGER.info('Download '+url)
            download = urllib.urlretrieve(url, filepath)
            localFiles.append(download[0])
        return localFiles

    def extractZIP(self, zipfile):
        pass

    def listScenes(self, dataset, eeGeometry, start, end):
        collection = ee.ImageCollection(dataset).filterDate(start, end).filterBounds(eeGeometry).getInfo()
        images = []
        for image in collection['features']:
            images.append(image['id'])

        return images


import urllib
from bs4 import BeautifulSoup
import re
import os

from pyEOM import log
LOGGER = log.LOGGER

def TestHTTPSource():
    source = HTTPSource('http://e4ftl01.cr.usgs.gov')
    source.listFiles('/MOLT/MOD13Q1.005/2000.02.18')
    files = source.filterFiles('.*\.(h10v09|h12v10)\..*\.hdf$')
    localFiles = source.downloadFiles('/Users/jonas/temp')
    return localFiles


class HTTPSource(object):
    url = None
    path = None
    soup = None

    directoryObj = None
    directories = []
    filesObj = None
    files = []

    def __init__(self, url):
        self.url = url

    def connect(self):
        pass

    def listDirectories(self, directory):
        self.path = directory
        LOGGER.info('Retrieving url: '+self.url+directory)
        html = urllib.urlopen(self.url+directory).read()
        self.directoryObj = BeautifulSoup(html)
        directories = self.directoryObj.findAll(href=re.compile('/'))
        directories = directories[1:]
        for dir in directories:
            self.directories.append(dir.string[0:-1])
        return self.directories

    def listFiles(self, directory):
        self.path = directory
        html = urllib.urlopen(self.url+directory).read()
        self.filesObj = BeautifulSoup(html)

    def filterFiles(self, regexp, urls=True):
        self.files = self.filesObj.findAll(text=re.compile(regexp))
        if urls==True:
            self.files = [self.url+self.path+'/'+file for file in self.files]
        return self.files

    def downloadFile(self, url, path):
        LOGGER.info('Download: '+url)
        filepath = path+'/'+url.split('/')[-1]
        if not os.path.isfile(filepath):
            download = urllib.urlretrieve(url, filepath)
            return download[0]
        else:
            return filepath

    def downloadFiles(self, path):
        localFiles = []
        for file in self.files:
            localFiles.append(self.downloadFile(file, path))
        return localFiles



def TestFTPSource():
    source = FTPSource('n5eil01u.ecs.nsidc.org', 'anonymous', 'nan')
    source.connect()
    #directories = source.listDirectories('SAN/MOST/MOD10CM.005')
    source.listFiles('/SAN/MOST/MOD10A2.005/2000.03.05')
    files = source.filterFiles('.*\.(h10v09|h12v10)\..*\.hdf$')
    source.disconnect()
    localFiles = source.downloadFiles('/Users/jonas/temp')
    return localFiles

class FTPSource(object):
    host = None
    user = None
    password = None
    directory = None
    ftpcon = None

    directories = []
    files = []

    import ftplib

    def __init__(self, host, user="anonymous", password="anon", directory=""):
        self.host = host
        self.user = user
        self.password = password
        self.directory = directory

    def connect(self):
        self.ftpcon = self.ftplib.FTP(self.host, self.user, self.password)

    def addDirectory(self, listing):
        if listing.startswith('d'): self.directories.append(listing.split()[-1])

    def listDirectories(self, directory):
        self.directory = directory
        self.ftpcon.cwd(directory)
        #self.ftpcon.dir('-d','*/',lambda L:self.directories.append(L.split()[-1]))
        self.ftpcon.dir('-d','*/',self.addDirectory)
        return self.directories

    def listFiles(self, directory):
        self.directory = directory
        self.ftpcon.cwd(directory)
        self.files = self.ftpcon.nlst()

    # filter files e.g., for a specific tile or file extension
    def filterFiles(self, regexp, urls=True):
        r = re.compile(regexp)
        objs = filter(r.match, self.files)
        files=[]
        for file in objs:
            files.append('ftp://'+self.host+self.directory+'/'+file)
        self.files = files
        return self.files

    # store file from url to path (directory), return lokal path to file
    def downloadFile(self, url, path):
        filepath = path+'/'+url.split('/')[-1]
        if not os.path.isfile(filepath):
            download = urllib.urlretrieve(url, filepath)
            return download[0]
        else:
            return filepath

    def downloadFiles(self, path):
        localFiles = []
        for file in self.files:
            localFiles.append(self.downloadFile(file, path))
        return localFiles

    def disconnect(self):
        self.ftpcon.quit()


class WCSSource(object):
    url = None

    def connect(self):
        pass


class SOSSource(object):
    url = None

    def connect(self):
        pass


