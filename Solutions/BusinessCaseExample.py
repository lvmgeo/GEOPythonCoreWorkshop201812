# -*- coding: utf-8 -*-
'''
    Our buisiness Case example in GEOPython
'''
import SysGISParams as Pr
import sys, os 
from GISPython import GISPythonModule
from GISPython import TimerHelper 
from GISPython import FTPHleper
from GISPython import AGServerHelper
from GISPython import ZipHelper
from GISPython import MailHelper
from GISPython import SimpleFileOpsSafe


class MainModule(GISPythonModule.GISPythonModule): 
    '''
        Main module
    '''
    def __init__(self):
        '''Class initialization'''
        self.modulename = os.path.splitext(os.path.basename(__file__))[0]
        GISPythonModule.GISPythonModule.__init__(self, self.modulename, Pr, __file__)

    def mainModule(self):
        '''
            Main procedure
            Args:
                self: The reserved object 'self'
        '''
        with TimerHelper.TimedSubprocess(self.Tool, u'environment setup'):  
            Tool = self.Tool
            callGP = self.Tool.callGP
            pj = os.path.join
            
            DH = SimpleFileOpsSafe.SimpleFileOpsSafe(Tool)
            tmp_folder = pj(Pr.TmpFolder, self.modulename)
            DH.CheckCreateDir(tmp_folder)
            DH.ClearDir(tmp_folder)
            

        with TimerHelper.TimedSubprocess(self.Tool, u'Step one get data form FTP'): 
            ftp = FTPHleper.FTPHleper(Pr.ftp_adress, Pr.ftp_user, Pr.ftp_pwd) # Set up Healper object
            tmpZIP = pj(tmp_folder, 'tmp.zip')  # get temporarry zip file name and path
            ftp.get_file(Pr.ftp_file, tmpZIP) # download the file

        with TimerHelper.TimedSubprocess(self.Tool, u'Step two unzip data'): 
            ziph = ZipHelper.ZipHelper()  # Set up Healper object
            ziph.ExtractZipFile(tmpZIP, tmp_folder) # Do the extract of the shp file

        with TimerHelper.TimedSubprocess(self.Tool, u'Step three Stopping AGS service'): 
            AGS = AGServerHelper.AGSServerHelper(Pr.ags_server, Pr.ags_user, Pr.ags_pwd, Tool=Tool ) # Set up Healper object
            AGS.StopService(Pr.serviceFolder, Pr.service) # Stop the service

        with TimerHelper.TimedSubprocess(self.Tool, u'Step for updating the data'): 
            layer = callGP('MakeFeatureLayer_management', pj(tmp_folder, Pr.shp_name), '#', 'someParamsField > 100') # creating a subset of data
            target_layer = pj(Pr.work_db, Pr.target_layer_name) # set up a full path to work layer in DB
            callGP('Append_management', layer, target_layer, 'NO_TEST') 
            callGP('RebuildIndexes_management', Pr.work_db, '#', [Pr.target_layer_name])
            AGS.StartService(Pr.serviceFolder, Pr.service) # Stop the service

        with TimerHelper.TimedSubprocess(self.Tool, u'Step five repporting results'): 
            elementCount = Tool.callGPSilent('GetCount_management', layer) # counting the elements added to DB
            mailSender = MailHelper.MailHelper('Rolands@mycompany.com', ['Carl@mycompany.com', 'Pater@mycompany.com'], 'Repport', 'Inserted into DB {} elements'.format(elementCount)) # Set up the e-mail for sending
            mailSender.SendMessage(Pr.mailserver, Pr.mailserver_port, Pr.mail_user, Pr.mail_pwd, useSSL=True) # Send e-mail

if __name__ == "__main__":
        Module = MainModule()
        Module.DoJob()
