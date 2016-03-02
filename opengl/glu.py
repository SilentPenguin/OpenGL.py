from OpenGL import GL
from re import sub

def convert(name):
    s1 = sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

for key, val in GL.__dict__.iteritems():
    if key.startswith('GLU_') and key != 'GLU_': key = key[4:]
    elif key.startswith('glu') and key != 'glu': key = convert(key[3:])
    key = '_' + key if key[0] in '1234567890' else key
    locals()[key] = val
    
del GLU