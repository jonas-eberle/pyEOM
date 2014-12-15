__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'
from pyEOM.sources import *

class GEE(GEESource):
    dataset = None
    start = '1900-01-01'
    end = '2100-01-01'
    epsg = 'EPSG:4326'
    scale = 30

    def __init__(self, task):
        self.task = task
        if 'dataset' not in task:
            raise Exception('No dataset found in task')
            sys.exit(1)
        self.dataset = task['dataset']
        if 'geom' not in task:
            raise Exception('No geometry found in task')
            sys.exit(1)
        if 'start' in task:
            self.start = task['start']
        if 'end' in task:
            self.end = task['end']
        if 'scale' in task:
            self.scale = int(task['scale'])
        if 'publishPath' not in task:
            self.publishPath = os.getcwd()
        else:
            self.publishPath = task['publishPath']

        self.connect()

        self.geom = self.processGeometry(task['geom'])

    def setPublishPath(self, path):
        self.publishPath = path

    def run(self):
        #                   dataset     bands   geom        start       end     epsg        scale       crsTransform
        data = self.getData(self.dataset, None, self.geom, self.start, self.end, self.epsg, self.scale, None)
        return data

    def ingest(self, format=None):
        return self.run()