#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_queries(n, ids): pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_queries(n, ids): pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_query(id): pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def begin_query(target, id): pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def end_query(target): pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_queryiv(target, pname, params): pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_query_objectiv(id, pname, params): pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_query_objectuiv(id, pname, params): pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def bind_buffer(target, buffer): pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_buffers(n, buffers): pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_buffers(n, buffers): pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_buffer(buffer): pass

@accepts(t.enum, t.sizeiptr, t.void, t.enum)
@returns(t.void)
@binds(dll)
def buffer_data(target, size, data, usage): pass

@accepts(t.enum, t.intptr, t.sizeiptr, t.void)
@returns(t.void)
@binds(dll)
def buffer_sub_data(target, offset, size, data): pass

@accepts(t.enum, t.intptr, t.sizeiptr, t.void)
@returns(t.void)
@binds(dll)
def get_buffer_sub_data(target, offset, size, data): pass

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def map_buffer(target, access): pass

@accepts(t.enum)
@returns(t.boolean)
@binds(dll)
def unmap_buffer(target): pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_buffer_parameteriv(target, pname, params): pass

@accepts(t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def get_buffer_pointerv(target, pname, params): pass

BUFFER_SIZE = 0x8764
BUFFER_USAGE = 0x8765
QUERY_COUNTER_BITS = 0x8864
CURRENT_QUERY = 0x8865
QUERY_RESULT = 0x8866
QUERY_RESULT_AVAILABLE = 0x8867
ARRAY_BUFFER = 0x8892
ELEMENT_ARRAY_BUFFER = 0x8893
ARRAY_BUFFER_BINDING = 0x8894
ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
READ_ONLY = 0x88B8
WRITE_ONLY = 0x88B9
READ_WRITE = 0x88BA
BUFFER_ACCESS = 0x88BB
BUFFER_MAPPED = 0x88BC
BUFFER_MAP_POINTER = 0x88BD
STREAM_DRAW = 0x88E0
STREAM_READ = 0x88E1
STREAM_COPY = 0x88E2
STATIC_DRAW = 0x88E4
STATIC_READ = 0x88E5
STATIC_COPY = 0x88E6
DYNAMIC_DRAW = 0x88E8
DYNAMIC_READ = 0x88E9
DYNAMIC_COPY = 0x88EA
SAMPLES_PASSED = 0x8914
SRC1_ALPHA = 0x8589
VERTEX_ARRAY_BUFFER_BINDING = 0x8896
NORMAL_ARRAY_BUFFER_BINDING = 0x8897
COLOR_ARRAY_BUFFER_BINDING = 0x8898
INDEX_ARRAY_BUFFER_BINDING = 0x8899
TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
FOG_COORD_SRC = 0x8450
FOG_COORD = 0x8451
CURRENT_FOG_COORD = 0x8453
FOG_COORD_ARRAY_TYPE = 0x8454
FOG_COORD_ARRAY_STRIDE = 0x8455
FOG_COORD_ARRAY_POINTER = 0x8456
FOG_COORD_ARRAY = 0x8457
FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
SRC0_RGB = 0x8580
SRC1_RGB = 0x8581
SRC2_RGB = 0x8582
SRC0_ALPHA = 0x8588
SRC2_ALPHA = 0x858A