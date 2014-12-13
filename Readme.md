pyEOM
=====

Earth Observation Monitor

Installation
-----------
*Needed Python libraries:*
* beautifulsoup4
* pyspatialite
* osgeo
* numpy

*Needed command-line software:*
* gdal_translate
* gdalwarp
* gdallocationinfo
* gdalbuildvrt
* gdal_merge.py

*Further requirements:*
For MODIS HDF data processing, HDF4 image format has to be available for gdal command-line tools.

Usage
-----
    from pyEOM import tasks
    ingest = tasks.Ingestion({
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
