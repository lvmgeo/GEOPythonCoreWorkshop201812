# -*- coding: utf-8 -*-

# Params
ftp_adress = 'sapleftpaddress.lvm.lv'
ftp_user = 'sampleuser'
ftp_pwd = 'samplepassword'
ftp_file = 'sampleFile.zip'
file_download_path = r'c:\tmp\MyData.zip'
tmp_path = r'c:\tmp'
shp_path = r'c:\tmp\downloaded.shp'
target_layer = r'c:\conn\MyDBConn.sde\targetFeatureClass'
target_layer_name = 'targetFeatureClass'
work_db = r'c:\conn\MyDBConn.sde'
ags_server = 'https://MyServer.lvm.lv'
ags_user = 'sampleuser'
ags_pwd = 'samplepassword'
service = 'MyServiceFolder/MyService.MapServer/'
mailserver = 'mailserver.mycompany.com'
mailserver_port = 587
mail_user = 'sampleuser'
mail_pwd = 'samplepassword'

# ---------------------------------
# Step one get data form FTP
# ---------------------------------

import ftplib
import zipfile

ftp = ftplib.FTP(ftp_adress, ftp_user, ftp_pwd)

print 'Opening local file ' + file_download_path
file = open(file_download_path, 'wb')
fSize = [0, 0]

def download_file_callback(data):
    """Download file callback"""
    file.write(data)
    fSize[0] += len(data)
    fSize[1] += len(data)
    if fSize[1] >= 10485760:
        file.flush()
        print 'Downloaded ' + str(fSize[0]/1048576) + ' MB'
        fSize[1] = 0

print 'Getting ' + file_download_path
ftp.retrbinary('RETR %s' % ftp_file, download_file_callback, 4096)

print 'File Downloaded!'
file.close()

# ---------------------------------
# Step two unzip data
# ---------------------------------

zfile = zipfile.ZipFile(file_download_path)
zfile.extractall(tmp_path)
zfile.close()
print 'File unzipped!'

# ---------------------------------
# Step three Stopping AGS service
# ---------------------------------

import httplib, urllib, json, urllib2

# Getting autorization tocken
query_dict = {'username':   ags_user,
                      'password':   ags_pwd,
                      'expiration': 60,
                      'client':     'requestip'}

query_string = urllib.urlencode(query_dict)
url = "{}/arcgis/admin/generateToken".format(ags_server)
token = json.loads(urllib.urlopen(url + "?f=json", query_string).read())
print 'AGS autorization done'

# Stopping service
folderURL = "/arcgis/admin/services/{}/stop".format(service)
params = urllib.urlencode({'token': token, 'f': 'json'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
httpConn = httplib.HTTPSConnection(ags_server)
httpConn.request("POST", folderURL, params, headers)
response = httpConn.getresponse()
httpConn.close()
print 'AGS stop done'

# ---------------------------------
# Step for updating the data
# ---------------------------------

import arcpy

mylayer = 'MylayerName'
arcpy.MakeFeatureLayer_management(shp_path, mylayer, 'someParamsField > 100')

for i in xrange(0, arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
arcpy.Append_management(mylayer, target_layer, 'NO_TEST')

for i in xrange(0, arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)

arcpy.RebuildIndexes_management(work_db, '#', [target_layer_name])

for i in xrange(0, arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)

# starting service
folderURL = "/arcgis/admin/services/{}/start".format(service)
params = urllib.urlencode({'token': token, 'f': 'json'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
httpConn = httplib.HTTPSConnection(ags_server)
httpConn.request("POST", folderURL, params, headers)
response = httpConn.getresponse()
httpConn.close()
print 'AGS start done'

# ---------------------------------
# Step five repporting results
# ---------------------------------

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
msg['Subject'] = "Repport"
msg['To'] = ", ".join(['Carl@mycompany.com', 'Pater@mycompany.com'])

elementCount = (arcpy.GetCount_management(mylayer)).getOutput(0)

msg.attach(MIMEText('Inserted into DB {} elements'.format(elementCount), 'plain', 'utf-8'))

import smtplib

mailer = smtplib.SMTP_SSL()
mailer.connect(mailserver, mailserver_port)
mailer.login(mail_user, mail_pwd)
mailer.sendmail('Rolands@mycompany.com', ['Carl@mycompany.com', 'Pater@mycompany.com'], msg.as_string())
mailer.close()