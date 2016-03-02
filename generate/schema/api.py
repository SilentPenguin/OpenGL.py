from xml.etree import ElementTree
from re import sub
from decorators import *
#xml elements, as seen in gl.xml
    
class Element(object):
    def __init__(self, element):
        self.element = element
    @property
    def text(self): return self.element.text
    
class Enum(Element):
    @attribute()
    def value():pass
    @attribute()
    def name(): pass
    @property
    def pep_name(self):
        name = self.name[3:]
        if name and name[0].isdigit(): name = '_' + name
        return name
    
class Name(Element):
    @property
    def text(self): return self.element.text
    
class PType(Element):
    @property
    def text(self): return self.element.text if self.element is not None else ''
    @property
    def pointer(self): return self.element is not None and self.element.tail.count('*')
    @property
    def type(self):
        type = self.text[2:] if self.text else 'void'
        format_str = 't.{}'
        for i in range(self.pointer):
            pointer_str = 't.char_p' if type == 'char' and i == 0 else 'POINTER({})'
            format_str = pointer_str.format(format_str)
        return format_str.format(type)
        
class Proto(Element):
    @element(Name)
    def name(): pass
    @element(PType)
    def ptype(): pass
    
class Param(Element):
    @element(Name)
    def name(): pass
    @element(PType)
    def ptype(): pass
    
class Command(Element):
    @attribute()
    def name(): pass
    @element(Proto)
    def proto(): pass
    @elements(Param, 'param')
    def params(): pass
    @property
    def pep_name(self):
        s1 = sub('(.)([A-Z][a-z]+)', r'\1_\2', self.name[2:])
        return sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        
class Require(Element):
    @elements(Command, 'command')
    def commands(): pass
    @elements(Enum, 'enum')
    def enums(): pass
        
class Feature(Element):
    @attribute()
    def name(): pass
    @attribute()
    def version(): pass
    @elements(Require, 'require')
    def requires(): pass
    @property
    def pep_name(self):
        return self.name.replace('_VERSION_', '_').lower()
    
class Group(Element):
    @attribute()
    def name(): pass
    
class Enums(Element):
    @elements(Enum, 'enum')
    def values(): pass
    @attribute()
    def namespace(): pass
    @attribute()
    def group(): pass
    @attribute()
    def vendor(): pass
    @attribute()
    def comment(): pass
    
class Commands(Element):
    @elements(Command, 'command')
    def values(): pass
    @attribute()
    def namespace(): pass
    
class Registry(Element):
    @elements(Feature, 'feature')
    def features(): pass
    @elements(Enums)
    def enums(): pass
    @elements(Commands)
    def commands(): pass
    
class Document:
    def __init__(self, path):
        self.tree = ElementTree.parse(path)
    @property
    def registry(self):
        return Registry(self.tree.getroot())