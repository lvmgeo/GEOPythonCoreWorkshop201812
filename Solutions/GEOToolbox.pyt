# -*- coding: utf-8 -*-
'''
    Toolbox purpose
'''
from  GISPython import GISPythonTool

import HelloGEO # import corresponding GEOPython modules

class Toolbox(object):
    """
        Toolbox itself
    """
    def __init__(self):
        self.label = "Toolbox label"
        self.alias = "Toolbox alias"

        # List of tool classes associated with this toolbox
        self.tools = [sapmleToll]
        
class sapmleToll(GISPythonTool.GISPythonTool):
    def __init__(self):
        """Define tool (tool name is the class name)"""
        self.label = u"Tool alilabelas"
        self.description = u"Tool description"

    def execute(self, parameters, messages):
        """Tool execution"""
        HelloGEO.MainModule().DoJob()
        return
