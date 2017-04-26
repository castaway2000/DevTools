import sys
import os
import selenium

from fusil.application import Application
from fusil.process.create import ProjectProcess


class FusilFuzzer():
    '''passive fuzzer'''
    def setupProject(self):
        ProjectProcess(self, ['echo', 'Hello World!'])
    
    
class SeleniumFuzzer():
    '''active/hands on fuzzer'''
    def setupProject(self):
        return 'bar'