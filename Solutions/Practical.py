# -*- coding: utf-8 -*-
'''
    GIT2018 Practical
'''
import SysGISParams as Pr
import sys, os 
from GISPython import GISPythonModule
from GISPython import TimerHelper
from GISPython import SimpleFileOpsSafe
from GISPython import ZipHelper
import LVMOpenDataDownloader

class MainModule(GISPythonModule.GISPythonModule): 
    '''
        Main module
    '''
    def __init__(self, inLayer = None):
        '''Class initialization'''
        self.modulename = os.path.splitext(os.path.basename(__file__))[0]
        GISPythonModule.GISPythonModule.__init__(self, self.modulename, Pr, __file__)
        self.inLayer = GISPythonModule.GISPythonModuleArgsHelper(inLayer)

    def mainModule(self, inLayer = None):
        '''
            Main procedure
            Args:
                self: The reserved object 'self'
                inLayer: Te layer to process
        '''
        with TimerHelper.TimedSubprocess(self.Tool, u'environment setup'):  
            Tool = self.Tool
            callGP = self.Tool.callGP
            pj = os.path.join

            # TODO: Create SimpleFileOpsSafe Helper
            # TODO: Create tmp folder variable uzsing Pr.TmpFolder parameter and pj
            # TODO: use SimpleFileOpsSafe CheckCreateDir command to create folder
            # TODO: use SimpleFileOpsSafe ClearDir command to clear temp folder
            
            DH = SimpleFileOpsSafe.SimpleFileOpsSafe(Tool)
            tmp_folder = pj(Pr.TmpFolder, self.modulename)
            DH.CheckCreateDir(tmp_folder)
            DH.ClearDir(tmp_folder)
            
        with TimerHelper.TimedSubprocess(self.Tool, u'LVM block data downlaoad'):
            # TODO: create tmp.zip file name variable in tmp folder using pj 
            # TODO: use LVMOpenDataDownloader to get LVM_KVARTALI data as GDB format
            tmp_file = pj(tmp_folder, 'kvartali.zip')
            LVMOpenDataDownloader.LVM_KVARTALI(tmp_file)

        with TimerHelper.TimedSubprocess(self.Tool, u'unzip data'):
            # TODO: create ZipHelper object 
            # TODO: extract downloaded file to tmp folder via ZipHelper
            ZH = ZipHelper.ZipHelper()
            ZH.ExtractZipFile(tmp_file, tmp_folder)

        with TimerHelper.TimedSubprocess(self.Tool, u'do selection'):
            self.inLayer.SetMainModuleValue(inLayer)
            inLayer = self.inLayer.GetResultValue(False)
            # TODO: create variable to extracted GDB Feature class. use pj to combine tmp folder 'LVM_KVARTALI.gdb' and 'LVM_KVARTALI' feature class name
            # TODO: Do Select by Location in your layer. Use INTERSECT as overlap_type
            # SelectLayerByLocation_management (in_layer, {overlap_type}, {select_features}, {search_distance}, {selection_type}, {invert_spatial_relationship}) 
            workLayer = pj(tmp_folder, 'LVM_KVARTALI.gdb','LVM_KVARTALI')
            callGP('SelectLayerByLocation_management', inLayer, 'INTERSECT', workLayer)

if __name__ == "__main__":
        Module = MainModule()
        Module.inLayer.processArgument(1)
        Module.DoJob()
