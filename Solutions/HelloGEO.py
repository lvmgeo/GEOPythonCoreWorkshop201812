# -*- coding: utf-8 -*-
'''
    This ir Hello GEO example
'''
import SysGISParams as Pr
import sys, os 
from GISPython import GISPythonModule
from GISPython import TimerHelper

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

        Tool.AddMessage('Hello GEO!')

if __name__ == "__main__":
        Module = MainModule()
        Module.DoJob()
