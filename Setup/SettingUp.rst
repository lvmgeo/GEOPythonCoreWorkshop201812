
General information
===================

Installation
------------

Dependencies
************

- ArcGIS 10.x /recommended with newest patches and service packs/ (*GISPython* is currently running on production systems based on ArcGIS 10.2.1, ArcGIS 10.3.1 and has been tested on ArcGIS 10.4, ArcGIS 10.6.X)
- Python 2.7 (included in ArcGIS installation) (arcpy and numpy modules included)

Package installation
********************
  
*GISPython* package is available on the `Python Package Index <https://pypi.python.org/pypi/GISPython>`_, so you can get it via pip::

	pip install GISPython
	
.. Note:: If pip isn’t installed, you can get it `here <https://packaging.python.org/installing/#install-pip-setuptools-and-wheel>`_!

Upgrade existing installation::

	pip install GISPython --Upgrade

Configuration & basic usage
---------------------------
	
Before using *GISPython* modules in custom geoprocessing scripts, you need to set up your scripting environment using `SetupDefaultEnvironment.py <SetupDefaultEnvironment.py>`_ module which also includes template for user scripts.
		
*SetupDefaultEnvironment* module also includes basic parameters (variable *paramsFileSource*) for parameter file (e.g. SysGISParams.py) which is important, because *GISPython* relies of several
parameters to be present to function successfully:

* OutDir - directory for storing script output log files ``OutDir = r'C:\GIS\Log\Outlog\'``
* OutDirArh - directory for storing script output log file archive (all non active files) ``OutDirArh = r'C:\GIS\Log\Outlog\Archive\'``
* ErrorLogDir - directory for storing script error log files ``ErrorLogDir = r'C:\GIS\Log\ErrorLog\'`` *(Important! This directory can be monitored for non empty files. If this directory has a file that is non empty - this indicates that a script has failed)*
* ErrorLogDirArh - directory for storing script error log files ``ErrorLogDirArh = r'C:\GIS\Log\ErrorLog\Archive'``
* TmpFolder - Temp folder ``TmpFolder = r'C:\GIS\tmp'``
* encodingPrimary - encoding of Windows shell ``encodingPrimary = 'cp775'``
* encodingSecondary - encoding of Windows unicode language used ``encodingSecondary = 'cp1257'``
* SetLogHistory - enable or disable Geoprocessing history logging ``SetLogHistory = False``

.. Note:: It is recommended to define additional script parameters in SysGISParams.py file, to keep the main code clean. Our approach is to define all the parameters that define current system environment be kept in this one file. In case of moving environment (e.g. test system and production system) this one file has the specific connections and can be easily modified without changing the scripts.

Visual Studio Core
------------------
Download from `code.visualstudio.com <https://code.visualstudio.com/download>`_.

Extensions healpful for developing GEOPythonCore:

* Python (ms-python.python) 
* autoDocstring (njpwerner.autodocstring)
* Contextual Duplicate (lafe.contextualduplicate)

GEOPythonCore module sippet can be added to Visual Studio Core Python snippets to quickly create new modules `GEOPythonModuleSnippet.json <GEOPythonModuleSnippet.json>`_

Usefull settings::

	"files.exclude": {
        "**/*.pyc": true,
        "**/on.LST": true
    },
    "files.associations": {
        "*.pyt": "python"
    },
    "files.autoGuessEncoding": true

Usful links
-------------
* `GEOPythonCore on PyPi <https://pypi.python.org/pypi/GISPython>`_
* `GEOPythonCore on GitHub <https://github.com/lvmgeo/GISPython>`_
* `GEOPythonCore online documentation <https://gispython.readthedocs.io/en/latest/general.html>`_
* `ArcPy reference <https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm>`_