__author__ = 'Jonas Eberle <jonas.eberle@eberle-mail.de>'

from pyEOM.datsets import MODIS

dataset = MODIS.Dataset('MOD13Q1')

import pyEOM.tasks as tasks
ingest = tasks.Ingestion([{
    'dataset': 'MODIS/MOD13Q1',
    'geom': 'POINT(10 20)',
    'start': '2001-01-01',
    'end': '2001-02-01',
    'quality': '',
    'localPath': '/tmp/pyEOM'
}])
ingest.run()

tsRasterOutput = ingest.processed[0]

tsRasterOutput.publish()
tsRasterOutput.update()