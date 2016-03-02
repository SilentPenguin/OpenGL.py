#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def dispatch_compute(num_groups_x, num_groups_y, num_groups_z): 
    pass

@accepts(t.intptr)
@returns(t.void)
@binds(dll)
def dispatch_compute_indirect(indirect): 
    pass

COMPUTE_SHADER = 0x91B9
MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
MAX_COMPUTE_WORK_GROUP_INVOCATIONS = 0x90EB
MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
COMPUTE_WORK_GROUP_SIZE = 0x8267
DISPATCH_INDIRECT_BUFFER = 0x90EE
DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
COMPUTE_SHADER_BIT = 0x00000020
@accepts(t.enum, t.void)
@returns(t.void)
@binds(dll)
def draw_arrays_indirect(mode, indirect): 
    pass

@accepts(t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def draw_elements_indirect(mode, type, indirect): 
    pass

DRAW_INDIRECT_BUFFER = 0x8F3F
DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
MAX_UNIFORM_LOCATIONS = 0x826E
@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_parameteri(target, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_framebuffer_parameteriv(target, pname, params): 
    pass

FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
MAX_FRAMEBUFFER_WIDTH = 0x9315
MAX_FRAMEBUFFER_HEIGHT = 0x9316
MAX_FRAMEBUFFER_SAMPLES = 0x9318
@accepts(t.uint, t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_program_interfaceiv(program, programInterface, pname, params): 
    pass

@accepts(t.uint, t.enum, t.char_p)
@returns(t.uint)
@binds(dll)
def get_program_resource_index(program, programInterface, name): 
    pass

@accepts(t.uint, t.enum, t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_program_resource_name(program, programInterface, index, bufSize, length, name): 
    pass

@accepts(t.uint, t.enum, t.uint, t.sizei, POINTER(t.enum), t.sizei, POINTER(t.sizei), POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_program_resourceiv(program, programInterface, index, propCount, props, bufSize, length, params): 
    pass

@accepts(t.uint, t.enum, t.char_p)
@returns(t.int)
@binds(dll)
def get_program_resource_location(program, programInterface, name): 
    pass

UNIFORM = 0x92E1
UNIFORM_BLOCK = 0x92E2
PROGRAM_INPUT = 0x92E3
PROGRAM_OUTPUT = 0x92E4
BUFFER_VARIABLE = 0x92E5
SHADER_STORAGE_BLOCK = 0x92E6
ATOMIC_COUNTER_BUFFER = 0x92C0
TRANSFORM_FEEDBACK_VARYING = 0x92F4
ACTIVE_RESOURCES = 0x92F5
MAX_NAME_LENGTH = 0x92F6
MAX_NUM_ACTIVE_VARIABLES = 0x92F7
NAME_LENGTH = 0x92F9
TYPE = 0x92FA
ARRAY_SIZE = 0x92FB
OFFSET = 0x92FC
BLOCK_INDEX = 0x92FD
ARRAY_STRIDE = 0x92FE
MATRIX_STRIDE = 0x92FF
IS_ROW_MAJOR = 0x9300
ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
BUFFER_BINDING = 0x9302
BUFFER_DATA_SIZE = 0x9303
NUM_ACTIVE_VARIABLES = 0x9304
ACTIVE_VARIABLES = 0x9305
REFERENCED_BY_VERTEX_SHADER = 0x9306
REFERENCED_BY_FRAGMENT_SHADER = 0x930A
REFERENCED_BY_COMPUTE_SHADER = 0x930B
TOP_LEVEL_ARRAY_SIZE = 0x930C
TOP_LEVEL_ARRAY_STRIDE = 0x930D
LOCATION = 0x930E
@accepts(t.uint, t.bitfield, t.uint)
@returns(t.void)
@binds(dll)
def use_program_stages(pipeline, stages, program): 
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def active_shader_program(pipeline, program): 
    pass

@accepts(t.enum, t.sizei, POINTER(t.char_p))
@returns(t.uint)
@binds(dll)
def create_shader_programv(type, count, strings): 
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def bind_program_pipeline(pipeline): 
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_program_pipelines(n, pipelines): 
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_program_pipelines(n, pipelines): 
    pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_program_pipeline(pipeline): 
    pass

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

@accepts(t.uint, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform2i(program, location, v0, v1): 
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform3i(program, location, v0, v1, v2): 
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def program_uniform4i(program, location, v0, v1, v2, v3): 
    pass

@accepts(t.uint, t.int, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform1ui(program, location, v0): 
    pass

@accepts(t.uint, t.int, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform2ui(program, location, v0, v1): 
    pass

@accepts(t.uint, t.int, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform3ui(program, location, v0, v1, v2): 
    pass

@accepts(t.uint, t.int, t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def program_uniform4ui(program, location, v0, v1, v2, v3): 
    pass

@accepts(t.uint, t.int, t.float)
@returns(t.void)
@binds(dll)
def program_uniform1f(program, location, v0): 
    pass

@accepts(t.uint, t.int, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform2f(program, location, v0, v1): 
    pass

@accepts(t.uint, t.int, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform3f(program, location, v0, v1, v2): 
    pass

@accepts(t.uint, t.int, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def program_uniform4f(program, location, v0, v1, v2, v3): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform1iv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform2iv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform3iv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def program_uniform4iv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform1uiv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform2uiv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform3uiv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def program_uniform4uiv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform1fv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform2fv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform3fv(program, location, count, value): 
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def program_uniform4fv(program, location, count, value): 
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

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def validate_program_pipeline(pipeline): 
    pass

@accepts(t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_program_pipeline_info_log(pipeline, bufSize, length, infoLog): 
    pass

VERTEX_SHADER_BIT = 0x00000001
FRAGMENT_SHADER_BIT = 0x00000002
ALL_SHADER_BITS = 0xFFFFFFFF
PROGRAM_SEPARABLE = 0x8258
ACTIVE_PROGRAM = 0x8259
PROGRAM_PIPELINE_BINDING = 0x825A
ATOMIC_COUNTER_BUFFER = 0x92C0
ATOMIC_COUNTER_BUFFER_BINDING = 0x92C1
ATOMIC_COUNTER_BUFFER_START = 0x92C2
ATOMIC_COUNTER_BUFFER_SIZE = 0x92C3
MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 0x92CC
MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 0x92D0
MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 0x92D1
MAX_VERTEX_ATOMIC_COUNTERS = 0x92D2
MAX_FRAGMENT_ATOMIC_COUNTERS = 0x92D6
MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
MAX_COMBINED_ATOMIC_COUNTERS = 0x92D7
MAX_ATOMIC_COUNTER_BUFFER_SIZE = 0x92D8
MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 0x92DC
ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9
UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB
@accepts(t.uint, t.uint, t.int, t.boolean, t.int, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def bind_image_texture(unit, texture, level, layered, layer, access, format): 
    pass

@accepts(t.enum, t.uint, POINTER(t.boolean))
@returns(t.void)
@binds(dll)
def get_booleani_v(target, index, data): 
    pass

@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def memory_barrier(barriers): 
    pass

@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def memory_barrier_by_region(barriers): 
    pass

MAX_IMAGE_UNITS = 0x8F38
MAX_VERTEX_IMAGE_UNIFORMS = 0x90CA
MAX_FRAGMENT_IMAGE_UNIFORMS = 0x90CE
MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
MAX_COMBINED_IMAGE_UNIFORMS = 0x90CF
IMAGE_BINDING_NAME = 0x8F3A
IMAGE_BINDING_LEVEL = 0x8F3B
IMAGE_BINDING_LAYERED = 0x8F3C
IMAGE_BINDING_LAYER = 0x8F3D
IMAGE_BINDING_ACCESS = 0x8F3E
IMAGE_BINDING_FORMAT = 0x906E
VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 0x00000001
ELEMENT_ARRAY_BARRIER_BIT = 0x00000002
UNIFORM_BARRIER_BIT = 0x00000004
TEXTURE_FETCH_BARRIER_BIT = 0x00000008
SHADER_IMAGE_ACCESS_BARRIER_BIT = 0x00000020
COMMAND_BARRIER_BIT = 0x00000040
PIXEL_BUFFER_BARRIER_BIT = 0x00000080
TEXTURE_UPDATE_BARRIER_BIT = 0x00000100
BUFFER_UPDATE_BARRIER_BIT = 0x00000200
FRAMEBUFFER_BARRIER_BIT = 0x00000400
TRANSFORM_FEEDBACK_BARRIER_BIT = 0x00000800
ATOMIC_COUNTER_BARRIER_BIT = 0x00001000
ALL_BARRIER_BITS = 0xFFFFFFFF
IMAGE_2D = 0x904D
IMAGE_3D = 0x904E
IMAGE_CUBE = 0x9050
IMAGE_2D_ARRAY = 0x9053
INT_IMAGE_2D = 0x9058
INT_IMAGE_3D = 0x9059
INT_IMAGE_CUBE = 0x905B
INT_IMAGE_2D_ARRAY = 0x905E
UNSIGNED_INT_IMAGE_2D = 0x9063
UNSIGNED_INT_IMAGE_3D = 0x9064
UNSIGNED_INT_IMAGE_CUBE = 0x9066
UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
IMAGE_FORMAT_COMPATIBILITY_TYPE = 0x90C7
IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 0x90C8
IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 0x90C9
READ_ONLY = 0x88B8
WRITE_ONLY = 0x88B9
READ_WRITE = 0x88BA
SHADER_STORAGE_BUFFER = 0x90D2
SHADER_STORAGE_BUFFER_BINDING = 0x90D3
SHADER_STORAGE_BUFFER_START = 0x90D4
SHADER_STORAGE_BUFFER_SIZE = 0x90D5
MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
SHADER_STORAGE_BARRIER_BIT = 0x00002000
MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 0x8F39
DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
STENCIL_INDEX = 0x1901
MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
@accepts(t.enum, t.sizei, t.enum, t.sizei, t.sizei, t.boolean)
@returns(t.void)
@binds(dll)
def tex_storage2_d_multisample(target, samples, internalformat, width, height, fixedsamplelocations): 
    pass

@accepts(t.enum, t.uint, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_multisamplefv(pname, index, val): 
    pass

@accepts(t.uint, t.bitfield)
@returns(t.void)
@binds(dll)
def sample_maski(maskNumber, mask): 
    '''set the value of a sub-word of the sample mask'''

@accepts(t.enum, t.int, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_level_parameteriv(target, level, pname, params): 
    pass

@accepts(t.enum, t.int, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_level_parameterfv(target, level, pname, params): 
    pass

SAMPLE_POSITION = 0x8E50
SAMPLE_MASK = 0x8E51
SAMPLE_MASK_VALUE = 0x8E52
TEXTURE_2D_MULTISAMPLE = 0x9100
MAX_SAMPLE_MASK_WORDS = 0x8E59
MAX_COLOR_TEXTURE_SAMPLES = 0x910E
MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
MAX_INTEGER_SAMPLES = 0x9110
TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
TEXTURE_SAMPLES = 0x9106
TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
TEXTURE_WIDTH = 0x1000
TEXTURE_HEIGHT = 0x1001
TEXTURE_DEPTH = 0x8071
TEXTURE_INTERNAL_FORMAT = 0x1003
TEXTURE_RED_SIZE = 0x805C
TEXTURE_GREEN_SIZE = 0x805D
TEXTURE_BLUE_SIZE = 0x805E
TEXTURE_ALPHA_SIZE = 0x805F
TEXTURE_DEPTH_SIZE = 0x884A
TEXTURE_STENCIL_SIZE = 0x88F1
TEXTURE_SHARED_SIZE = 0x8C3F
TEXTURE_RED_TYPE = 0x8C10
TEXTURE_GREEN_TYPE = 0x8C11
TEXTURE_BLUE_TYPE = 0x8C12
TEXTURE_ALPHA_TYPE = 0x8C13
TEXTURE_DEPTH_TYPE = 0x8C16
TEXTURE_COMPRESSED = 0x86A1
SAMPLER_2D_MULTISAMPLE = 0x9108
INT_SAMPLER_2D_MULTISAMPLE = 0x9109
UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
@accepts(t.uint, t.uint, t.intptr, t.sizei)
@returns(t.void)
@binds(dll)
def bind_vertex_buffer(bindingindex, buffer, offset, stride): 
    pass

@accepts(t.uint, t.int, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_format(attribindex, size, type, normalized, relativeoffset): 
    pass

@accepts(t.uint, t.int, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_i_format(attribindex, size, type, relativeoffset): 
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_binding(attribindex, bindingindex): 
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_binding_divisor(bindingindex, divisor): 
    pass

VERTEX_ATTRIB_BINDING = 0x82D4
VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
VERTEX_BINDING_DIVISOR = 0x82D6
VERTEX_BINDING_OFFSET = 0x82D7
VERTEX_BINDING_STRIDE = 0x82D8
VERTEX_BINDING_BUFFER = 0x8F4F
MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
MAX_VERTEX_ATTRIB_STRIDE = 0x82E5