# -*- coding: utf-8 -*-
'''
    Standard generated gispython params file
    see: http://gispython.readthedocs.io/en/latest/index.html
'''

import  GISPython.SysGISToolsSysParams
import os


# ---------------------------------------------------------------------------
# Basic parameters
# ---------------------------------------------------------------------------
Version =  GISPython.SysGISToolsSysParams.Version
OutDir = 'C:\\GIS\\Log\\Outlog\\' # Output file directory
OutDirArh = 'C:\\GIS\\Log\\Outlog\\Archive\\' # Output file directory archive
ErrorLogDir = 'C:\\GIS\\Log\\ErrorLog\\' # Error output file directory
ErrorLogDirArh = 'C:\\GIS\\Log\\ErrorLog\\Archive\\' # Error output file directory archive
TmpFolder = 'C:\\GIS\\tmp\\' # Temp directory
# DataFolder = 'C:\\GIS\\Data\\' # Directory for storing source data (not automaticaly created)
# BackupFolder = 'C:\\GIS\\Backup\\' # Directory for storing data backup (not automaticaly created)
encodingPrimary = 'cp1257' # Windows charset
encodingSecondary = 'cp775' # Windows Shell charset
SetLogHistory = False # enable or disable Geoprocessing history logging 

# ---------------------------------
# business case example params
# ---------------------------------
ftp_adress = 'sapleftpaddress.lvm.lv'
ftp_user = 'sampleuser'
ftp_pwd = 'samplepassword'
ftp_file = 'sampleFile.zip'
# file_download_path = r'c:\tmp\MyData.zip' not needed
# tmp_path = r'c:\tmp'  not needed
# shp_path = r'c:\tmp\downloaded.shp'  not needed using shp file name
shp_name = r'downloaded.shp'
# target_layer = r'c:\conn\MyDBConn.sde\targetFeatureClass' not needed
target_layer_name = 'targetFeatureClass'
work_db = r'c:\conn\MyDBConn.sde'
ags_server = 'https://MyServer.lvm.lv'
ags_user = 'sampleuser'
ags_pwd = 'samplepassword'
serviceFolder = 'MyServiceFolder' # Splitted from service
service = 'MyService.MapServer'
mailserver = 'mailserver.mycompany.com'
mailserver_port = 587
mail_user = 'sampleuser'
mail_pwd = 'samplepassword'

