#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.enum, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def draw_arrays_instanced(mode, first, count, instancecount):
    '''draw multiple instances of a range of elements'''

@accepts(t.enum, t.sizei, t.enum, t.void, t.sizei)
@returns(t.void)
@binds(dll)
def draw_elements_instanced(mode, count, type, indices, instancecount):
    '''draw multiple instances of a set of elements'''

@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_buffer(target, internalformat, buffer):
    '''attach a buffer object's data store to a buffer texture object'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def primitive_restart_index(index):
    '''specify the primitive restart index'''

SAMPLER_2D_RECT = 0x8B63
SAMPLER_2D_RECT_SHADOW = 0x8B64
SAMPLER_BUFFER = 0x8DC2
INT_SAMPLER_2D_RECT = 0x8DCD
INT_SAMPLER_BUFFER = 0x8DD0
UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
TEXTURE_BUFFER = 0x8C2A
MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
TEXTURE_BINDING_BUFFER = 0x8C2C
TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
TEXTURE_RECTANGLE = 0x84F5
TEXTURE_BINDING_RECTANGLE = 0x84F6
PROXY_TEXTURE_RECTANGLE = 0x84F7
MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
R8_SNORM = 0x8F94
RG8_SNORM = 0x8F95
RGB8_SNORM = 0x8F96
RGBA8_SNORM = 0x8F97
R16_SNORM = 0x8F98
RG16_SNORM = 0x8F99
RGB16_SNORM = 0x8F9A
RGBA16_SNORM = 0x8F9B
SIGNED_NORMALIZED = 0x8F9C
PRIMITIVE_RESTART = 0x8F9D
PRIMITIVE_RESTART_INDEX = 0x8F9E
@accepts(t.enum, t.enum, t.intptr, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def copy_buffer_sub_data(readTarget, writeTarget, readOffset, writeOffset, size):
    '''copy all or part of the data store of a buffer object to the data store of another buffer object'''

COPY_READ_BUFFER = 0x8F36
COPY_WRITE_BUFFER = 0x8F37
@accepts(t.uint, t.sizei, POINTER(t.char_p), POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_uniform_indices(program, uniformCount, uniformNames, uniformIndices):
    '''retrieve the index of a named uniform block'''

@accepts(t.uint, t.sizei, POINTER(t.uint), t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_active_uniformsiv(program, uniformCount, uniformIndices, pname, params):
    '''Returns information about several active uniform variables for the specified program object'''

@accepts(t.uint, t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_active_uniform_name(program, uniformIndex, bufSize, length, uniformName):
    '''query the name of an active uniform'''

@accepts(t.uint, t.char_p)
@returns(t.uint)
@binds(dll)
def get_uniform_block_index(program, uniformBlockName):
    '''retrieve the index of a named uniform block'''

@accepts(t.uint, t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_active_uniform_blockiv(program, uniformBlockIndex, pname, params):
    pass

@accepts(t.uint, t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_active_uniform_block_name(program, uniformBlockIndex, bufSize, length, uniformBlockName):
    '''retrieve the name of an active uniform block'''

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def uniform_block_binding(program, uniformBlockIndex, uniformBlockBinding):
    '''assign a binding point to an active uniform block'''

@accepts(t.enum, t.uint, t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def bind_buffer_range(target, index, buffer, offset, size):
    '''bind a range within a buffer object to an indexed buffer target'''

@accepts(t.enum, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def bind_buffer_base(target, index, buffer):
    '''bind a buffer object to an indexed buffer target'''

@accepts(t.enum, t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_integeri_v(target, index, data):
    pass

UNIFORM_BUFFER = 0x8A11
UNIFORM_BUFFER_BINDING = 0x8A28
UNIFORM_BUFFER_START = 0x8A29
UNIFORM_BUFFER_SIZE = 0x8A2A
MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
MAX_UNIFORM_BLOCK_SIZE = 0x8A30
MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
ACTIVE_UNIFORM_BLOCKS = 0x8A36
UNIFORM_TYPE = 0x8A37
UNIFORM_SIZE = 0x8A38
UNIFORM_NAME_LENGTH = 0x8A39
UNIFORM_BLOCK_INDEX = 0x8A3A
UNIFORM_OFFSET = 0x8A3B
UNIFORM_ARRAY_STRIDE = 0x8A3C
UNIFORM_MATRIX_STRIDE = 0x8A3D
UNIFORM_IS_ROW_MAJOR = 0x8A3E
UNIFORM_BLOCK_BINDING = 0x8A3F
UNIFORM_BLOCK_DATA_SIZE = 0x8A40
UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
INVALID_INDEX = 0xFFFFFFFF