#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

FIXED = 0x140C
IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
LOW_FLOAT = 0x8DF0
MEDIUM_FLOAT = 0x8DF1
HIGH_FLOAT = 0x8DF2
LOW_INT = 0x8DF3
MEDIUM_INT = 0x8DF4
HIGH_INT = 0x8DF5
SHADER_COMPILER = 0x8DFA
SHADER_BINARY_FORMATS = 0x8DF8
NUM_SHADER_BINARY_FORMATS = 0x8DF9
MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
MAX_VARYING_VECTORS = 0x8DFC
MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
RGB565 = 0x8D62
PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
PROGRAM_BINARY_LENGTH = 0x8741
NUM_PROGRAM_BINARY_FORMATS = 0x87FE
PROGRAM_BINARY_FORMATS = 0x87FF
VERTEX_SHADER_BIT = 0x00000001
FRAGMENT_SHADER_BIT = 0x00000002
GEOMETRY_SHADER_BIT = 0x00000004
TESS_CONTROL_SHADER_BIT = 0x00000008
TESS_EVALUATION_SHADER_BIT = 0x00000010
ALL_SHADER_BITS = 0xFFFFFFFF
PROGRAM_SEPARABLE = 0x8258
ACTIVE_PROGRAM = 0x8259
PROGRAM_PIPELINE_BINDING = 0x825A
MAX_VIEWPORTS = 0x825B
VIEWPORT_SUBPIXEL_BITS = 0x825C
VIEWPORT_BOUNDS_RANGE = 0x825D
LAYER_PROVOKING_VERTEX = 0x825E
VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
UNDEFINED_VERTEX = 0x8260
@accepts()
@returns(t.void)
@binds(dll)
def release_shader_compiler():
    '''
    release resources consumed by the implementation's shader compiler
    
    Args:
    '''

@accepts(t.sizei, POINTER(t.uint), t.enum, t.void, t.sizei)
@returns(t.void)
@binds(dll)
def shader_binary(count, shaders, binaryformat, binary, length):
    '''
    load pre-compiled shader binaries
    
    Args:
        count: Specifies the number of shader object handles contained in shaders
        shaders: Specifies the address of an array of shader handles into which to load pre-compiled shader binaries
        binaryformat: Specifies the format of the shader binaries contained in binary
        binary: Specifies the address of an array of bytes containing pre-compiled binary shader code
        length: Specifies the length of the array whose address is given in binary
    '''

@accepts(t.enum, t.enum, POINTER(t.int), POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_shader_precision_format(shadertype, precisiontype, range, precision):
    '''
    retrieve the range and precision for numeric formats supported by the shader compiler
    
    Args:
        shadertype: Specifies the type of shader whose precision to query
        precisiontype: Specifies the numeric format whose precision and range to query
        range: Specifies the address of array of two integers into which encodings of the implementation's numeric range are returned
        precision: Specifies the address of an integer into which the numeric precision of the implementation is written
    '''

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def depth_rangef(n, f):
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def clear_depthf(d):
    pass

@accepts(t.uint, t.sizei, POINTER(t.sizei), POINTER(t.enum), t.void)
@returns(t.void)
@binds(dll)
def get_program_binary(program, bufsize, length, binaryformat, binary):
    '''
    return a binary representation of a program object's compiled and linked executable source
    
    Args:
        program: Specifies the name of a program object whose binary representation to retrieve
        bufsize: Specifies the size of the buffer whose address is given by binary
        length: Specifies the address of a variable to receive the number of bytes written into binary
        binaryformat: Specifies the address of a variable to receive a token indicating the format of the binary data returned by the GL
        binary: Specifies the address an array into which the GL will return program's binary representation
    '''

@accepts(t.uint, t.enum, t.void, t.sizei)
@returns(t.void)
@binds(dll)
def program_binary(program, binaryformat, binary, length):
    '''
    load a program object with a program binary
    
    Args:
        program: Specifies the name of a program object into which to load a program binary
        binaryformat: Specifies the format of the binary data in binary
        binary: Specifies the address an array containing the binary to be loaded into program
        length: Specifies the number of bytes contained in binary
    '''

@accepts(t.uint, t.enum, t.int)
@returns(t.void)
@binds(dll)
def program_parameteri(program, pname, value):
    pass

@accepts(t.uint, t.bitfield, t.uint)
@returns(t.void)
@binds(dll)
def use_program_stages(pipeline, stages, program):
    '''
    bind stages of a program object to a program pipeline
    
    Args:
        pipeline: Specifies the program pipeline object to which to bind stages from program
        stages: Specifies a set of program stages to bind to the program pipeline object
        program: Specifies the program object containing the shader executables to use in pipeline
    '''

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def active_shader_program(pipeline, program):
    '''
    set the active program object for a program pipeline object
    
    Args:
        pipeline: Specifies the program pipeline object to set the active program object for
        program: Specifies the program object to set as the active program pipeline object pipeline
    '''

@accepts(t.enum, t.sizei, POINTER(t.char_p))
@returns(t.uint)
@binds(dll)
def create_shader_programv(type, count, strings):
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def bind_program_pipeline(pipeline):
    '''
    bind a program pipeline to the current context
    
    Args:
        pipeline: Specifies the name of the pipeline object to bind to the context
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_program_pipelines(n, pipelines):
    '''
    delete program pipeline objects
    
    Args:
        n: Specifies the number of program pipeline objects to delete
        pipelines: Specifies an array of names of program pipeline objects to delete
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_program_pipelines(n, pipelines):
    '''
    reserve program pipeline object names
    
    Args:
        n: Specifies the number of program pipeline object names to reserve
        pipelines: Specifies an array of into which the reserved names will be written
    '''

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_program_pipeline(pipeline):
    '''
    determine if a name corresponds to a program pipeline object
    
    Args:
        pipeline: Specifies a value that may be the name of a program pipeline object
    '''

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_program_pipelineiv(pipeline, pname, params):
    pass

@accepts(t.uint, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform1i(program, location, v0):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform1iv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.float)
@returns(t.void)
@binds(dll)
def program_uniform1f(program, location, v0):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform1fv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.double)
@returns(t.void)
@binds(dll)
def program_uniform1d(program, location, v0):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform1dv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform1ui(program, location, v0):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform1uiv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform2i(program, location, v0, v1):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform2iv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform2f(program, location, v0, v1):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform2fv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.double, t.double)
@returns(t.void)
@binds(dll)
def program_uniform2d(program, location, v0, v1):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform2dv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform2ui(program, location, v0, v1):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform2uiv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform3i(program, location, v0, v1, v2):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform3iv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform3f(program, location, v0, v1, v2):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform3fv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def program_uniform3d(program, location, v0, v1, v2):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform3dv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform3ui(program, location, v0, v1, v2):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform3uiv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform4i(program, location, v0, v1, v2, v3):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform4iv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform4f(program, location, v0, v1, v2, v3):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform4fv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def program_uniform4d(program, location, v0, v1, v2, v3):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform4dv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform4ui(program, location, v0, v1, v2, v3):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform4uiv(program, location, count, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2x3fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3x2fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2x4fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4x2fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3x4fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4x3fv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2x3dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3x2dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix2x4dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4x2dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix3x4dv(program, location, count, transpose, value):
    pass

@accepts(t.uint, t.int, t.sizei, t.boolean, POINTER(t.double))
@returns(t.void)
@binds(dll)
def program_uniform_matrix4x3dv(program, location, count, transpose, value):
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def validate_program_pipeline(pipeline):
    '''
    validate a program pipeline object against current GL state
    
    Args:
        pipeline: Specifies the name of a program pipeline object to validate
    '''

@accepts(t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_program_pipeline_info_log(pipeline, bufsize, length, infolog):
    '''
    retrieve the info log string from a program pipeline object
    
    Args:
        pipeline: Specifies the name of a program pipeline object from which to retrieve the info log
        bufsize: Specifies the maximum number of characters, including the null terminator, that may be written into infoLog
        length: Specifies the address of a variable into which will be written the number of characters written into infoLog
        infolog: Specifies the address of an array of characters into which will be written the info log for pipeline
    '''

@accepts(t.uint, t.double)
@returns(t.void)
@binds(dll)
def vertex_attrib_l1d(index, x):
    pass

@accepts(t.uint, t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex_attrib_l2d(index, x, y):
    pass

@accepts(t.uint, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex_attrib_l3d(index, x, y, z):
    pass

@accepts(t.uint, t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex_attrib_l4d(index, x, y, z, w):
    pass

@accepts(t.uint, POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex_attrib_l1dv(index, v):
    pass

@accepts(t.uint, POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex_attrib_l2dv(index, v):
    pass

@accepts(t.uint, POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex_attrib_l3dv(index, v):
    pass

@accepts(t.uint, POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex_attrib_l4dv(index, v):
    pass

@accepts(t.uint, t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def vertex_attrib_l_pointer(index, size, type, stride, pointer):
    pass

@accepts(t.uint, t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_vertex_attrib_ldv(index, pname, params):
    pass

@accepts(t.uint, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def viewport_arrayv(first, count, v):
    pass

@accepts(t.uint, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def viewport_indexedf(index, x, y, w, h):
    pass

@accepts(t.uint, POINTER(t.float))
@returns(t.void)
@binds(dll)
def viewport_indexedfv(index, v):
    pass

@accepts(t.uint, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def scissor_arrayv(first, count, v):
    pass

@accepts(t.uint, t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def scissor_indexed(index, left, bottom, width, height):
    '''
    define the scissor box for a specific viewport
    
    Args:
        index: Specifies the index of the viewport whose scissor box to modify
        left, bottom: Specify the coordinate of the bottom left corner of the scissor box, in pixels
        width, height: Specify ths dimensions of the scissor box, in pixels
    '''

@accepts(t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def scissor_indexedv(index, v):
    pass

@accepts(t.uint, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def depth_range_arrayv(first, count, v):
    pass

@accepts(t.uint, t.double, t.double)
@returns(t.void)
@binds(dll)
def depth_range_indexed(index, n, f):
    '''
    specify mapping of depth values from normalized device coordinates to window coordinates for a specified viewport
    
    Args:
        index: Specifies the index of the viewport whose depth range to update
    '''

@accepts(t.enum, t.uint, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_floati_v(target, index, data):
    pass

@accepts(t.enum, t.uint, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_doublei_v(target, index, data):
    pass
