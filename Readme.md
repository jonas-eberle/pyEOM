pyEOM
=====

pyEOM is the Python package for the Earth Observation Monitor (www.earth-observation-monitor.net), a project developed by the Friedrich-Schiller-University Jena, Department for Earth Observation (www.eo.uni-jena.de).

You can use pyEOM to extract time-series data for different MODIS products and Landsat data and a given geometry (individual Pixel or Polygon).

*Please note:* The development of this package is in an early state. Documentation, testing and completion of the work will follow.

If you have any questions, please do not hesitate to contact me: Jonas Eberle <jonas.eberle@uni-jena.de>

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

Please make sure that the command-line tools are within the System path. Otherwise you have to specify the path to the tools within the GDAL class (class variable "path") in processing.py.

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

Installation
------------

No setup.py is available at the moment. Please download the pyEOM folder and set the Python path to the parent directory.
    import sys
    sys.path.append('/directory/to/parent/folder/of/pyEOM')

Available datasets
------------------
* MODIS Surface Reflectance: MOD09A1, MOD09Q1
* MODIS Snow Cover: MOD10A1, MYD10A1, MOD10A2, MYD10A2, MOD10C1, MYD10C1, MOD10C2, MYD10C2, MOD10CM, MYD10CM
* MODIS Land Surface Temperature: MOD11A1, MYD11A1, MOD11A2, MYD11A2, MOD11B1, MYD11B1, MOD11C1, MYD11C1, MOD11C2, MYD11C2, MOD11C3, MYD11C3
* MODIS Vegetation Indices: MOD13A1, MYD13A1, MOD13A2, MYD13A2, MOD13A3, MYD13A3, MOD13C1, MYD13C1, MOD13C2, MYD13C2, MOD13Q1, MYD13Q1
* MODIS Leaf Area Index - FPAR: MCD15A2, MCD15A3
* MODIS Albedo: MCD43A3
* MODIS Vegetation Continuous Fields: MOD44B
* MODIS Thermal Anomalies & Fire: MCD45A1

Further information to the datasets can be found at the following sites:
* NASA LPDAAC: http://lpdaac.usgs.gov/products/modis_products_table
* NSIDC DAAC: http://nsidc.org/data/modis/data_summaries/index.html

Several MODIS and especially Landsat datasets are also available using Google Earth Engine. 

Google Earth Engine
-------------------

If you have an account for the Google Earth Engine (https://earthengine.google.org), you can also use the Python bindings to have access to specific MODIS products and Landsat datasets.

Please set the variables MY_SERVICE_ACCOUNT and MY_PRIVATE_KEY_FILE in gee_init.py to your service account username and the private key file.

*Examples:*
    from pyEOM.datasets import Landsat
    source = Landsat.GEE({'dataset': 'LANDSAT/LC8_L1T', 'geom': 'POINT(11 51)'})
    output = source.ingest()

    from pyEOM.datasets import MODIS
    source = MODIS.GEE({'dataset': 'MODIS/MOD13Q1', 'geom': 'POINT(11 51)'})
    output = source.ingest()