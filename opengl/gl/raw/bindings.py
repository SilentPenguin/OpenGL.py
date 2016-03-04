from ctypes import *
from ctypes.util import *
from opengl.gl.raw import types as t

path = find_library('OpenGL')
dll = cdll.LoadLibrary(path)

def convert(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
    
def accepts(*argtypes, **kwargtypes):
    def decorator(func):
        if func: func.argtypes = argtypes
        return func
    return decorator
    
def returns(type):
    def decorator(func):
        if func: func.restype = type
        return func
    return decorator
    
def errors(**errors):
    def decorator(func):
        def check_error(result, func, arguments):
            code = get_error()
            if code: raise Exception(errors[code])
        func.errcheck = check_error
        
def binds(dll, name=None):
    def decorator(func):
        try:
            binding = getattr(dll, name or 'gl' + convert(func.__name__))
            binding.__doc__ = func.__doc__
            return binding
        except:
            return False
    return decorator