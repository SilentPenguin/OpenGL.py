from xml.etree import ElementTree
from decorators import *

class Element(object):
    def __init__(self, element):
        self.element = element
    @property
    def text(self): return self.element.text
    
class Document:
    def __init__(self, path):
        self.tree = ElementTree.parse(path)
    @property
    def refentry(self):
        return RefEntry(self.tree.getroot())
        
class RefPurpose(Element): pass
        
class RefNameDiv(Element):
    @element(RefPurpose)
    def refpurpose(): pass
        
class RefEntry(Element):
    @element(RefNameDiv)
    def refnamediv(): pass