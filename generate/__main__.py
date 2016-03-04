import re
import rxml

MAN_PATH = 'OpenGL/registry/man/man{}/{}.xml'
XML_PATH = 'OpenGL/registry/api/gl.xml'
RAW_PATH = 'OpenGL/opengl/gl/raw/'

def main():
    doc = rxml.Document(XML_PATH)
    write.init(doc)
    write.raw(doc)
    
class write:
    @staticmethod
    def init(doc):
        lines = []
        for feature in doc.feature:
            lines.append('from opengl.gl.raw.' + pep.feature(feature['name']) + ' import *')
        write.file(lines, RAW_PATH + '__init__.py')
    
    @staticmethod
    def raw(doc):
        write.enum_values = define.enums(doc)
        write.command_values = define.commands(doc)
        for feature in doc.feature:
            write.feature(feature)
            
    @staticmethod
    def headers(lines):
        lines.append('#BEWARE: automatically generated code')
        lines.append('#This code was generated by /generate/__main__.py')
        lines.append('')
        lines.append('from opengl.gl.raw.bindings import *')
        lines.append('')
            
    @staticmethod
    def feature(feature):
        lines = []
        name = feature['name']
        feature_path = RAW_PATH + pep.feature(name) + '.py'
        write.headers(lines)
        for require in feature.require:
            for command in require.command:
                write.command(lines, command)
            for enum in require.enum:
                write.enum(lines, enum)
        write.file(lines, feature_path)
        
    @staticmethod
    def command(lines, command):
        name = command['name']
        ret, params, types = write.command_values[name]
        lines.append('@accepts({})'.format(', '.join(types)))
        lines.append('@returns({})'.format(ret))
        lines.append('@binds(dll)')
        lines.append('def {}({}):'.format(pep.command(name), ', '.join(params)))
        document.command(lines, command, params)
        lines.append('')
        
    @staticmethod
    def enum(lines, enum):
        name = enum['name']
        lines.append('{} = {}'.format(pep.enum(name), write.enum_values[name]))
        
    @staticmethod
    def file(lines, path):
        with open(path, 'w') as file:
            lines = '\n'.join(lines)
            file.writelines(lines)
            
class document:
    @staticmethod
    def command(lines, command, params):
        for i in (4,3,2):
            try:
                path = MAN_PATH.format(i, command['name'])
                doc = rxml.Document(path)
                lines.append('    \'\'\'')
                document.command_description(lines, doc)
                document.command_args(lines, params, doc)
                lines.append('    \'\'\'')
                break
            except IOError:
                if i == 2: lines.append('    pass')
            
    @staticmethod
    def command_description(lines, doc):
        text = doc.refnamediv[0].refpurpose[0].node_text
        text = pep.doc_body(text)
        lines.append('    ' + text)
        
    @staticmethod
    def command_args(lines, params, doc):
        lines.append('    ')
        lines.append('    Args:')
        if not doc.refsect1 or not doc.refsect1[0].variablelist or not doc.refsect1[0].variablelist[0].varlistentry: return
        variable_list = doc.refsect1[0].variablelist[0].varlistentry
        for param in variable_list:
            if not param.term: break
            name = ', '.join(term.parameter[0].text.lower() for term in param.term if term.parameter and term.parameter[0].text.lower() in params)
            if not name: continue
            text = param.listitem[0].para[0].node_text
            text = pep.doc_body(text)
            lines.append('        {}: {}'.format(name, text))
            
class define:
    @staticmethod
    def commands(doc):
        return {
            command.proto[0].name[0].text:
            (
                pep.type(command.proto[0].ptype[0].text, command.proto[0].ptype[0].tail) if command.proto and command.proto[0].ptype else 't.void',
                tuple(param.name[0].text.lower() for param in command.param),
                tuple(pep.type(param.ptype[0].text, param.ptype[0].tail) if param.ptype else 't.void' for param in command.param),
            )
            for group in doc.commands
            for command in group.command
        }
    
    @staticmethod
    def enums(doc):
        return {
            enum['name']:enum['value']
            for group in doc.enums
            for enum in group.enum
        }

class pep:
    @staticmethod
    def feature(string):
        return string.replace('_VERSION_', '_').lower()
        
    @staticmethod
    def command(string):
        if string.startswith('gl'): string = string[2:]
        string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string)
        return string.lower()
        
    @staticmethod
    def enum(string):
        if string.startswith('GL_'): string = string[3:]
        if string and string[0].isdigit(): string = '_' + string
        return string
    
    @staticmethod
    def type(string, tail):
        string = string or 'void'
        if string.startswith('GL'): string = string[2:]
        format_str = 't.{}'
        for i in range(tail.count('*')):
            pointer_str = 't.char_p' if string == 'char' and i == 0 else 'POINTER({})'
            format_str = pointer_str.format(format_str)
        return format_str.format(string)
        
    @staticmethod
    def doc_body(string):
        def command_replace(match):
            return 'gl.' + pep.command(match.group(0))
        import lxml.html
        string = string.split(".")[0]
        string = re.sub('GL_([_A-Z]*?)', r'gl.\1', string)
        string = re.sub('gl[A-Z][A-Za-z]+', command_replace, string)
        string = string.replace('NULL', 'None')
        string = string.replace('\n', '').replace('\r', '')
        string = lxml.html.fromstring(string).text_content().encode('unicode-escape')
        string = ' '.join(string.split())
        return string
        

if __name__ == '__main__': main()