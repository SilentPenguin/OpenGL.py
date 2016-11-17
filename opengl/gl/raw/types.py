import ctypes

def type_(ctype):
    '''
    Monkey patching method that creates wrapper types
    '''
    class GLMeta(type(ctype)):
        '''implements gl.type[array_size] array typing'''
        def __getitem__(self, other):
            return type(ctype).__mul__(self, other)
        def __instancecheck__(self, other):
            return ctype.__instancecheck__(other)
            
    class GLType(ctype):
        __metaclass__ = GLMeta
        
    return GLType

boolean = type_(ctypes.c_ubyte)
byte = type_(ctypes.c_byte)
ubyte = type_(ctypes.c_ubyte)
short = type_(ctypes.c_short)
ushort = type_(ctypes.c_ushort)
int = type_(ctypes.c_int)
uint = type_(ctypes.c_uint)
fixed = type_(ctypes.c_int)
int64 = type_(ctypes.c_int64)
uint64 = type_(ctypes.c_uint64)
sizei = type_(ctypes.c_int)
enum = type_(ctypes.c_uint)
intptr = type_(ctypes.c_int)
sizeiptr = type_(ctypes.c_int)
sync = type_(ctypes.c_int)
bitfield = type_(ctypes.c_uint)
half = type_(ctypes.c_int16)
float = type_(ctypes.c_float)
clampf = type_(ctypes.c_float)
double = type_(ctypes.c_double)
clampd = type_(ctypes.c_double)
void = ctypes.c_void_p
char = type_(ctypes.c_char)
char_p = type_(ctypes.c_char_p)

DEBUGPROC = ctypes.CFUNCTYPE(enum, enum, uint, enum, sizei, ctypes.POINTER(char), void)
clampx = type_(ctypes.c_int)