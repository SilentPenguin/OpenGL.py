from OpenGL import GLUT
from re import sub

def convert(name):
    s1 = sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

for key, val in GLUT.__dict__.iteritems():
    if key.startswith('GLUT_') and key != 'GLUT_': key = key[5:]
    elif key.startswith('glut') and key != 'glut': key = convert(key[4:])
    key = '_' + key if key[0] in '1234567890' else key
    locals()[key] = val
    
del GLUT