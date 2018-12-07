# -*- coding: utf-8 -*-
'''
    GIT2018 Practical Toolbox
'''
from GISPython import GISPythonTool

import Practical # import corresponding GEOPython modules

class Toolbox(object):
    """
        Toolbox itself
    """
    def __init__(self):
        self.label = "GIT2018Practical"
        self.alias = "GIT2018Practical"

        # List of tool classes associated with this toolbox
        self.tools = [sapmleToll]
        
class sapmleToll(GISPythonTool.GISPythonTool):
    def __init__(self):
        """Define tool (tool name is the class name)"""
        self.label = u"Select features in LVM forests"
        self.description = u"Select features in LVM forests"

    def getParameterInfo(self):
        """Define parameters"""
        param_0 = arcpy.Parameter(
            displayName=r'input layer:',
            name="inLayer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        ret_val = [param_0]
        return ret_val

    def execute(self, parameters, messages):
        """Tool execution"""
        Practical.MainModule(parameters[0].valueAsText).DoJob()
        return
