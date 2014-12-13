__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'


class Sensor(object):
    values = []
    dates = []
    publishPath = None
    name = None
    dataset = None
    sensorInfo = dict()

    def __init__(self, name, dataset, localPath, sensorInfo=None):
        self.name = name
        self.dataset = dataset
        self.values = []
        self.dates = []
        self.sensorInfo = dict()
        self.publishPath = localPath
        if isinstance(sensorInfo, dict):
            self.setSensorInfo(sensorInfo)

    def setSensorInfo(self, sensorInfo):
        for key, val in sensorInfo.items():
            self.sensorInfo[key] = val
        return sensorInfo

    def addEntry(self, date, value):
        self.values.append(value)
        self.dates.append(date)

    def setMergedFile(self, file):
        self.mergedFile = file