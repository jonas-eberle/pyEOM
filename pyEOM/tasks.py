__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'

import logging
from pyEOM.datasets import *
from pyEOM import log
import os
import sys
import importlib
import ConfigParser

LOGGER = log.LOGGER

def TestIngestion():
    ingest = Ingestion({
        'dataset': 'MODIS/MOD13Q1',
        'geom': 'POLYGON((7.807615733070551 26.259757466002124,7.434080576820532 25.607681923751194,8.510740733070508 25.09140328282509,9.082029795570381 25.884760600666922,7.807615733070551 26.259757466002124))',
        'start': '2001-01-01',
        'end': '2001-02-01',
        'qualityValue': '0;1',
        'qualityBand': 'PR',
        'publishPath': '/tmp/pyEOM',
        'format': 'HDF4Image',
        'EPSG': None,
        'resample': None,
        'source': 'LPDAAC'
    })
    output = ingest.start()
    return output

def TestIngestionPoint():
    ingest = Ingestion({
        'dataset': 'MODIS/MOD13Q1',
        'geom': 'POINT(7.807615733070551 26.259757466002124)',
        'start': '2001-01-01',
        'end': '2001-02-01',
        'qualityValue': '0;1',
        'qualityBand': 'PR',
        'publishPath': '/tmp/pyEOM/POINT',
        'format': 'HDF4Image',
        'EPSG': None,
        'resample': None,
        'source': 'LPDAAC'
    })
    output = ingest.start()
    return output


def TestIngestionFTP():
    ingest = Ingestion({
        'dataset': 'MODIS/MOD10CM',
        'geom': 'POLYGON((7.807615733070551 26.259757466002124,7.434080576820532 25.607681923751194,8.510740733070508 25.09140328282509,9.082029795570381 25.884760600666922,7.807615733070551 26.259757466002124))',
        'start': '2001-01-01',
        'end': '2001-02-01',
        'publishPath': '/tmp/pyEOM/MOD10CM',
        'format': 'HDF4Image',
        'EPSG': None,
        'resample': None
    })
    output = ingest.start()
    return output


class Ingestion(object):
    task = dict()
    processing = dict()
    downloadPath = None
    publishPath = None
    format = "HDF4Image"

    def __init__(self, task, downloadPath=None):
        self.setupLogging()
        self.task = task
        LOGGER.info('Start ingestion with task '+str(task))
        if 'dataset' not in task or 'geom' not in task:
            raise Exception('Dataset or Geometry not available in Task!')
        if 'format' in task:
            self.format = task['format']
        if downloadPath != None:
            self.downloadPath = downloadPath
            if not os.path.exists(downloadPath): os.makedirs(downloadPath)
        if 'publishPath' in task:
            self.publishPath = task['publishPath']

    def setupLogging(self, config=None):
        log.setup_logger(config)
        LOGGER.info('Setting up logger')

    def save(self):
        processConfig = ConfigParser.RawConfigParser()
        processConfig.add_section('input')
        for key, val in self.task.items():
            processConfig.set('input', key, str(val))

        if not os.path.exists(self.publishPath+'/data'): os.makedirs(self.publishPath+'/data')
        with open(self.publishPath+'/data/task.cfg', 'wb') as configfile:
            processConfig.write(configfile)

    def start(self):
        dataset = self.task['dataset'].split('/')
        if len(dataset) != 2:
            raise Exception('Name of dataset is not valid!')

        LOGGER.debug('Dataset: '+dataset[0])
        LOGGER.debug('Product: '+dataset[1])
        if "MODIS" == dataset[0]:
            try:
                dataset = getattr(importlib.import_module('pyEOM.datasets.predefined.MODIS.'+dataset[1]), 'Dataset')
            except Exception as e:
                raise Exception('Dataset Class is not available: '+str(e))
                sys.exit(1)
            self.processing['dataset'] = dataset()

            if len(self.processing['dataset'].sources) == 0:
                raise Exception('No sources available!')

            from datasets import MODIS
            LOGGER.debug('Import MODIS datasets '+str(MODIS))

            LOGGER.info('Dataset Default Source: '+self.processing['dataset'].sources[0])
            if 'source' in self.task:
                source = self.task['source']
                LOGGER.info('Source defined by the user: '+source)
            else:
                source = self.processing['dataset'].sources[0]
                self.task['source'] = source

            self.save()
            self.task['dataset'] = self.processing['dataset'].getDownloadInfo()
            try:
                LOGGER.debug('Try to get source class: '+source)
                if source == 'LPDAAC' or source == 'NSIDC':
                    sourceObj = getattr(MODIS, source)()
                    if source == 'LPDAAC':
                        sourceObj.setUserPwd(self.task['userPwd'])
                    self.processing['source'] = getattr(MODIS, 'MODISHDF')(self.task, self.processing['dataset'], sourceObj)
                else:
                    self.processing['source'] = getattr(MODIS, source)(self.task, self.processing['dataset'])
            except NameError, e:
                LOGGER.error('Dataset modul not found')
                raise e
            except AttributeError, e:
                LOGGER.error('Source class not found in dataset modul')
                raise e
            LOGGER.info('ingest task')
            if self.downloadPath != None: self.processing['source'].setDownloadPath(self.downloadPath)
            self.processing['source'].setPublishPath(self.publishPath)
            return self.processing['source'].ingest(self.format)

        elif "LANDSAT" == dataset[0]:
            from datasets import Landsat
            self.processing['source'] = Landsat.GEE(task)
            return self.processing['source'].run()
        elif "NOAA" == dataset[0]:
            pass



class Analysis(object):
    def __init__(self, tsRasterOutput):
        pass

    def doAnalysis(self, type, params):
        pass


class Monitoring(object):
    def __init__(self, dataset):
        pass

    def defineMonitor(self, param, value):
        pass

    def defineNotification(self, type, value):
        pass

