import ctypes

boolean = ctypes.c_ubyte
byte = ctypes.c_byte
ubyte = ctypes.c_ubyte
short = ctypes.c_short
ushort = ctypes.c_ushort
int = ctypes.c_int
uint = ctypes.c_uint
fixed = ctypes.c_int
int64 = ctypes.c_int64
uint64 = ctypes.c_uint64
sizei = ctypes.c_int
enum = ctypes.c_uint
intptr = ctypes.c_int
sizeiptr = ctypes.c_int
sync = ctypes.c_int
bitfield = ctypes.c_uint
half = ctypes.c_int16
float = ctypes.c_float
clampf = ctypes.c_float
double = ctypes.c_double
clampd = ctypes.c_double
void = ctypes.c_void_p
char = ctypes.c_char
char_p = ctypes.c_char_p

DEBUGPROC = ctypes.CFUNCTYPE(enum, enum, uint, enum, sizei, ctypes.POINTER(char), void)
clampx = ctypes.c_int