from lxml import etree
import re

'''access xml using lxml'''

class Element(object):
    def __init__(self, element):
        self.element = element
        self.element.tag = re.sub('\{.*?\}','', self.element.tag)
        
    def __getitem__(self, key):
        return self.element.get(key)
        
    def getattr(self, key):
        return tuple(
            Element(child) 
            for child in self.element.iterchildren()
            if isinstance(child.tag, basestring) and re.sub('\{.*?\}', '', child.tag) == key
        )
        
    __getattr__ = getattr
        
    @property
    def text(self):
        return self.element.text
        
    @property
    def tail(self):
        return self.element.tail
        
    @property
    def node_text(self):
        result = etree.tostring(self.element).strip()
        result = re.search('<[^>]*>([\s\S]*)<\/[^>]*>', result).group(1)
        return result

class Document(Element):
    def __init__(self, xml):
        parser = etree.XMLParser(recover=True)
        tree = etree.parse(xml, parser)
        Element.__init__(self, tree.getroot())