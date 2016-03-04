#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

MULTISAMPLE_LINE_WIDTH_RANGE = 0x9381
MULTISAMPLE_LINE_WIDTH_GRANULARITY = 0x9382
@accepts()
@returns(t.void)
@binds(dll)
def blend_barrier():
    pass

MULTIPLY = 0x9294
SCREEN = 0x9295
OVERLAY = 0x9296
DARKEN = 0x9297
LIGHTEN = 0x9298
COLORDODGE = 0x9299
COLORBURN = 0x929A
HARDLIGHT = 0x929B
SOFTLIGHT = 0x929C
DIFFERENCE = 0x929E
EXCLUSION = 0x92A0
HSL_HUE = 0x92AD
HSL_SATURATION = 0x92AE
HSL_COLOR = 0x92AF
HSL_LUMINOSITY = 0x92B0
@accepts(t.uint, t.enum, t.int, t.int, t.int, t.int, t.uint, t.enum, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def copy_image_sub_data(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
    '''perform a raw data copy between two images'''

@accepts(t.enum, t.enum, t.enum, t.sizei, POINTER(t.uint), t.boolean)
@returns(t.void)
@binds(dll)
def debug_message_control(source, type, severity, count, ids, enabled):
    '''control the reporting of debug messages in a debug context'''

@accepts(t.enum, t.enum, t.uint, t.enum, t.sizei, t.char_p)
@returns(t.void)
@binds(dll)
def debug_message_insert(source, type, id, severity, length, buf):
    '''inject an application-supplied message into the debug message queue'''

@accepts(t.DEBUGPROC, t.void)
@returns(t.void)
@binds(dll)
def debug_message_callback(callback, userParam):
    '''specify a callback to receive debugging messages from the GL'''

@accepts(t.uint, t.sizei, POINTER(t.enum), POINTER(t.enum), POINTER(t.uint), POINTER(t.enum), POINTER(t.sizei), t.char_p)
@returns(t.uint)
@binds(dll)
def get_debug_message_log(count, bufSize, sources, types, ids, severities, lengths, messageLog):
    '''retrieve messages from the debug message log'''

@accepts(t.enum, t.uint, t.sizei, t.char_p)
@returns(t.void)
@binds(dll)
def push_debug_group(source, id, length, message):
    '''push a named debug group into the command stream'''

@accepts()
@returns(t.void)
@binds(dll)
def pop_debug_group():
    '''pop the active debug group'''

@accepts(t.enum, t.uint, t.sizei, t.char_p)
@returns(t.void)
@binds(dll)
def object_label(identifier, name, length, label):
    '''label a named object identified within a namespace'''

@accepts(t.enum, t.uint, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_object_label(identifier, name, bufSize, length, label):
    '''retrieve the label of a named object identified within a namespace'''

@accepts(t.void, t.sizei, t.char_p)
@returns(t.void)
@binds(dll)
def object_ptr_label(ptr, length, label):
    '''label a a sync object identified by a pointer'''

@accepts(t.void, t.sizei, POINTER(t.sizei), t.char_p)
@returns(t.void)
@binds(dll)
def get_object_ptr_label(ptr, bufSize, length, label):
    '''retrieve the label of a sync object identified by a pointer'''

@accepts(t.enum, t.void)
@returns(t.void)
@binds(dll)
def get_pointerv(pname, params):
    '''return the address of the specified pointer'''

DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
DEBUG_CALLBACK_FUNCTION = 0x8244
DEBUG_CALLBACK_USER_PARAM = 0x8245
DEBUG_SOURCE_API = 0x8246
DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
DEBUG_SOURCE_SHADER_COMPILER = 0x8248
DEBUG_SOURCE_THIRD_PARTY = 0x8249
DEBUG_SOURCE_APPLICATION = 0x824A
DEBUG_SOURCE_OTHER = 0x824B
DEBUG_TYPE_ERROR = 0x824C
DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
DEBUG_TYPE_PORTABILITY = 0x824F
DEBUG_TYPE_PERFORMANCE = 0x8250
DEBUG_TYPE_OTHER = 0x8251
DEBUG_TYPE_MARKER = 0x8268
DEBUG_TYPE_PUSH_GROUP = 0x8269
DEBUG_TYPE_POP_GROUP = 0x826A
DEBUG_SEVERITY_NOTIFICATION = 0x826B
MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
DEBUG_GROUP_STACK_DEPTH = 0x826D
BUFFER = 0x82E0
SHADER = 0x82E1
PROGRAM = 0x82E2
VERTEX_ARRAY = 0x8074
QUERY = 0x82E3
PROGRAM_PIPELINE = 0x82E4
SAMPLER = 0x82E6
MAX_LABEL_LENGTH = 0x82E8
MAX_DEBUG_MESSAGE_LENGTH = 0x9143
MAX_DEBUG_LOGGED_MESSAGES = 0x9144
DEBUG_LOGGED_MESSAGES = 0x9145
DEBUG_SEVERITY_HIGH = 0x9146
DEBUG_SEVERITY_MEDIUM = 0x9147
DEBUG_SEVERITY_LOW = 0x9148
DEBUG_OUTPUT = 0x92E0
CONTEXT_FLAG_DEBUG_BIT = 0x00000002
STACK_OVERFLOW = 0x0503
STACK_UNDERFLOW = 0x0504
@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def enablei(target, index):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def disablei(target, index):
    pass

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def blend_equationi(buf, mode):
    pass

@accepts(t.uint, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_equation_separatei(buf, modeRGB, modeAlpha):
    pass

@accepts(t.uint, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_funci(buf, src, dst):
    pass

@accepts(t.uint, t.enum, t.enum, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_func_separatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
    pass

@accepts(t.uint, t.boolean, t.boolean, t.boolean, t.boolean)
@returns(t.void)
@binds(dll)
def color_maski(index, r, g, b, a):
    pass

@accepts(t.enum, t.uint)
@returns(t.boolean)
@binds(dll)
def is_enabledi(target, index):
    pass

@accepts(t.enum, t.sizei, t.enum, t.void, t.int)
@returns(t.void)
@binds(dll)
def draw_elements_base_vertex(mode, count, type, indices, basevertex):
    '''render primitives from array data with a per-element offset'''

@accepts(t.enum, t.uint, t.uint, t.sizei, t.enum, t.void, t.int)
@returns(t.void)
@binds(dll)
def draw_range_elements_base_vertex(mode, start, end, count, type, indices, basevertex):
    '''render primitives from array data with a per-element offset'''

@accepts(t.enum, t.sizei, t.enum, t.void, t.sizei, t.int)
@returns(t.void)
@binds(dll)
def draw_elements_instanced_base_vertex(mode, count, type, indices, instancecount, basevertex):
    '''render multiple instances of a set of primitives from array data with a per-element offset'''

@accepts(t.enum, t.enum, t.uint, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_texture(target, attachment, texture, level):
    '''attach a level of a texture object as a logical buffer of a framebuffer object'''

GEOMETRY_SHADER = 0x8DD9
GEOMETRY_SHADER_BIT = 0x00000004
GEOMETRY_VERTICES_OUT = 0x8916
GEOMETRY_INPUT_TYPE = 0x8917
GEOMETRY_OUTPUT_TYPE = 0x8918
GEOMETRY_SHADER_INVOCATIONS = 0x887F
LAYER_PROVOKING_VERTEX = 0x825E
LINES_ADJACENCY = 0x000A
LINE_STRIP_ADJACENCY = 0x000B
TRIANGLES_ADJACENCY = 0x000C
TRIANGLE_STRIP_ADJACENCY = 0x000D
MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 0x92CF
MAX_GEOMETRY_ATOMIC_COUNTERS = 0x92D5
MAX_GEOMETRY_IMAGE_UNIFORMS = 0x90CD
MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
FIRST_VERTEX_CONVENTION = 0x8E4D
LAST_VERTEX_CONVENTION = 0x8E4E
UNDEFINED_VERTEX = 0x8260
PRIMITIVES_GENERATED = 0x8C87
FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
MAX_FRAMEBUFFER_LAYERS = 0x9317
FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
REFERENCED_BY_GEOMETRY_SHADER = 0x9309
@accepts(t.float, t.float, t.float, t.float, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def primitive_bounding_box(minX, minY, minZ, minW, maxX, maxY, maxZ, maxW):
    pass

PRIMITIVE_BOUNDING_BOX = 0x92BE
@accepts()
@returns(t.enum)
@binds(dll)
def get_graphics_reset_status():
    '''check if the rendering context has not been lost due to software or hardware issues'''

@accepts(t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def readn_pixels(x, y, width, height, format, type, bufSize, data):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def getn_uniformfv(program, location, bufSize, params):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def getn_uniformiv(program, location, bufSize, params):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def getn_uniformuiv(program, location, bufSize, params):
    pass

NO_ERROR = 0
CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
CONTEXT_FLAGS = 0x821E
LOSE_CONTEXT_ON_RESET = 0x8252
GUILTY_CONTEXT_RESET = 0x8253
INNOCENT_CONTEXT_RESET = 0x8254
UNKNOWN_CONTEXT_RESET = 0x8255
RESET_NOTIFICATION_STRATEGY = 0x8256
NO_RESET_NOTIFICATION = 0x8261
CONTEXT_LOST = 0x0507
@accepts(t.float)
@returns(t.void)
@binds(dll)
def min_sample_shading(value):
    '''specifies minimum rate at which sample shaing takes place'''

SAMPLE_SHADING = 0x8C36
MIN_SAMPLE_SHADING_VALUE = 0x8C37
MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def patch_parameteri(pname, value):
    pass

PATCHES = 0x000E
PATCH_VERTICES = 0x8E72
TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
TESS_GEN_MODE = 0x8E76
TESS_GEN_SPACING = 0x8E77
TESS_GEN_VERTEX_ORDER = 0x8E78
TESS_GEN_POINT_MODE = 0x8E79
TRIANGLES = 0x0004
ISOLINES = 0x8E7A
QUADS = 0x0007
EQUAL = 0x0202
FRACTIONAL_ODD = 0x8E7B
FRACTIONAL_EVEN = 0x8E7C
CCW = 0x0901
CW = 0x0900
MAX_PATCH_VERTICES = 0x8E7D
MAX_TESS_GEN_LEVEL = 0x8E7E
MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
MAX_TESS_PATCH_COMPONENTS = 0x8E84
MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 0x92CD
MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 0x92CE
MAX_TESS_CONTROL_ATOMIC_COUNTERS = 0x92D3
MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 0x92D4
MAX_TESS_CONTROL_IMAGE_UNIFORMS = 0x90CB
MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 0x90CC
MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 0x8221
IS_PER_PATCH = 0x92E7
REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
TESS_CONTROL_SHADER = 0x8E88
TESS_EVALUATION_SHADER = 0x8E87
TESS_CONTROL_SHADER_BIT = 0x00000008
TESS_EVALUATION_SHADER_BIT = 0x00000010
@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_parameter_iiv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def tex_parameter_iuiv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_parameter_iiv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_tex_parameter_iuiv(target, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def sampler_parameter_iiv(sampler, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def sampler_parameter_iuiv(sampler, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_sampler_parameter_iiv(sampler, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_sampler_parameter_iuiv(sampler, pname, params):
    pass

TEXTURE_BORDER_COLOR = 0x1004
CLAMP_TO_BORDER = 0x812D
@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_buffer(target, internalformat, buffer):
    '''attach a buffer object's data store to a buffer texture object'''

@accepts(t.enum, t.enum, t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def tex_buffer_range(target, internalformat, buffer, offset, size):
    '''attach a range of a buffer object's data store to a buffer texture object'''

TEXTURE_BUFFER = 0x8C2A
TEXTURE_BUFFER_BINDING = 0x8C2A
MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
TEXTURE_BINDING_BUFFER = 0x8C2C
TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
SAMPLER_BUFFER = 0x8DC2
INT_SAMPLER_BUFFER = 0x8DD0
UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
IMAGE_BUFFER = 0x9051
INT_IMAGE_BUFFER = 0x905C
UNSIGNED_INT_IMAGE_BUFFER = 0x9067
TEXTURE_BUFFER_OFFSET = 0x919D
TEXTURE_BUFFER_SIZE = 0x919E
COMPRESSED_RGBA_ASTC_4x4 = 0x93B0
COMPRESSED_RGBA_ASTC_5x4 = 0x93B1
COMPRESSED_RGBA_ASTC_5x5 = 0x93B2
COMPRESSED_RGBA_ASTC_6x5 = 0x93B3
COMPRESSED_RGBA_ASTC_6x6 = 0x93B4
COMPRESSED_RGBA_ASTC_8x5 = 0x93B5
COMPRESSED_RGBA_ASTC_8x6 = 0x93B6
COMPRESSED_RGBA_ASTC_8x8 = 0x93B7
COMPRESSED_RGBA_ASTC_10x5 = 0x93B8
COMPRESSED_RGBA_ASTC_10x6 = 0x93B9
COMPRESSED_RGBA_ASTC_10x8 = 0x93BA
COMPRESSED_RGBA_ASTC_10x10 = 0x93BB
COMPRESSED_RGBA_ASTC_12x10 = 0x93BC
COMPRESSED_RGBA_ASTC_12x12 = 0x93BD
COMPRESSED_SRGB8_ALPHA8_ASTC_4x4 = 0x93D0
COMPRESSED_SRGB8_ALPHA8_ASTC_5x4 = 0x93D1
COMPRESSED_SRGB8_ALPHA8_ASTC_5x5 = 0x93D2
COMPRESSED_SRGB8_ALPHA8_ASTC_6x5 = 0x93D3
COMPRESSED_SRGB8_ALPHA8_ASTC_6x6 = 0x93D4
COMPRESSED_SRGB8_ALPHA8_ASTC_8x5 = 0x93D5
COMPRESSED_SRGB8_ALPHA8_ASTC_8x6 = 0x93D6
COMPRESSED_SRGB8_ALPHA8_ASTC_8x8 = 0x93D7
COMPRESSED_SRGB8_ALPHA8_ASTC_10x5 = 0x93D8
COMPRESSED_SRGB8_ALPHA8_ASTC_10x6 = 0x93D9
COMPRESSED_SRGB8_ALPHA8_ASTC_10x8 = 0x93DA
COMPRESSED_SRGB8_ALPHA8_ASTC_10x10 = 0x93DB
COMPRESSED_SRGB8_ALPHA8_ASTC_12x10 = 0x93DC
COMPRESSED_SRGB8_ALPHA8_ASTC_12x12 = 0x93DD
TEXTURE_CUBE_MAP_ARRAY = 0x9009
TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
SAMPLER_CUBE_MAP_ARRAY = 0x900C
SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
IMAGE_CUBE_MAP_ARRAY = 0x9054
INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
STENCIL_INDEX = 0x1901
STENCIL_INDEX8 = 0x8D48
@accepts(t.enum, t.sizei, t.enum, t.sizei, t.sizei, t.sizei, t.boolean)
@returns(t.void)
@binds(dll)
def tex_storage3_d_multisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
    '''specify storage for a two-dimensional multisample array texture'''

TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D