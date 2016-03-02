#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

VERSION_ES_CL_1_0 = 1
VERSION_ES_CM_1_1 = 1
VERSION_ES_CL_1_1 = 1
DEPTH_BUFFER_BIT = 0x00000100
STENCIL_BUFFER_BIT = 0x00000400
COLOR_BUFFER_BIT = 0x00004000
FALSE = 0
TRUE = 1
POINTS = 0x0000
LINES = 0x0001
LINE_LOOP = 0x0002
LINE_STRIP = 0x0003
TRIANGLES = 0x0004
TRIANGLE_STRIP = 0x0005
TRIANGLE_FAN = 0x0006
NEVER = 0x0200
LESS = 0x0201
EQUAL = 0x0202
LEQUAL = 0x0203
GREATER = 0x0204
NOTEQUAL = 0x0205
GEQUAL = 0x0206
ALWAYS = 0x0207
ZERO = 0
ONE = 1
SRC_COLOR = 0x0300
ONE_MINUS_SRC_COLOR = 0x0301
SRC_ALPHA = 0x0302
ONE_MINUS_SRC_ALPHA = 0x0303
DST_ALPHA = 0x0304
ONE_MINUS_DST_ALPHA = 0x0305
DST_COLOR = 0x0306
ONE_MINUS_DST_COLOR = 0x0307
SRC_ALPHA_SATURATE = 0x0308
CLIP_PLANE0 = 0x3000
CLIP_PLANE1 = 0x3001
CLIP_PLANE2 = 0x3002
CLIP_PLANE3 = 0x3003
CLIP_PLANE4 = 0x3004
CLIP_PLANE5 = 0x3005
FRONT = 0x0404
BACK = 0x0405
FRONT_AND_BACK = 0x0408
FOG = 0x0B60
LIGHTING = 0x0B50
TEXTURE_2D = 0x0DE1
CULL_FACE = 0x0B44
ALPHA_TEST = 0x0BC0
BLEND = 0x0BE2
COLOR_LOGIC_OP = 0x0BF2
DITHER = 0x0BD0
STENCIL_TEST = 0x0B90
DEPTH_TEST = 0x0B71
POINT_SMOOTH = 0x0B10
LINE_SMOOTH = 0x0B20
SCISSOR_TEST = 0x0C11
COLOR_MATERIAL = 0x0B57
NORMALIZE = 0x0BA1
RESCALE_NORMAL = 0x803A
VERTEX_ARRAY = 0x8074
NORMAL_ARRAY = 0x8075
COLOR_ARRAY = 0x8076
TEXTURE_COORD_ARRAY = 0x8078
MULTISAMPLE = 0x809D
SAMPLE_ALPHA_TO_COVERAGE = 0x809E
SAMPLE_ALPHA_TO_ONE = 0x809F
SAMPLE_COVERAGE = 0x80A0
NO_ERROR = 0
INVALID_ENUM = 0x0500
INVALID_VALUE = 0x0501
INVALID_OPERATION = 0x0502
STACK_OVERFLOW = 0x0503
STACK_UNDERFLOW = 0x0504
OUT_OF_MEMORY = 0x0505
EXP = 0x0800
EXP2 = 0x0801
FOG_DENSITY = 0x0B62
FOG_START = 0x0B63
FOG_END = 0x0B64
FOG_MODE = 0x0B65
FOG_COLOR = 0x0B66
CW = 0x0900
CCW = 0x0901
CURRENT_COLOR = 0x0B00
CURRENT_NORMAL = 0x0B02
CURRENT_TEXTURE_COORDS = 0x0B03
POINT_SIZE = 0x0B11
POINT_SIZE_MIN = 0x8126
POINT_SIZE_MAX = 0x8127
POINT_FADE_THRESHOLD_SIZE = 0x8128
POINT_DISTANCE_ATTENUATION = 0x8129
SMOOTH_POINT_SIZE_RANGE = 0x0B12
LINE_WIDTH = 0x0B21
SMOOTH_LINE_WIDTH_RANGE = 0x0B22
ALIASED_POINT_SIZE_RANGE = 0x846D
ALIASED_LINE_WIDTH_RANGE = 0x846E
CULL_FACE_MODE = 0x0B45
FRONT_FACE = 0x0B46
SHADE_MODEL = 0x0B54
DEPTH_RANGE = 0x0B70
DEPTH_WRITEMASK = 0x0B72
DEPTH_CLEAR_VALUE = 0x0B73
DEPTH_FUNC = 0x0B74
STENCIL_CLEAR_VALUE = 0x0B91
STENCIL_FUNC = 0x0B92
STENCIL_VALUE_MASK = 0x0B93
STENCIL_FAIL = 0x0B94
STENCIL_PASS_DEPTH_FAIL = 0x0B95
STENCIL_PASS_DEPTH_PASS = 0x0B96
STENCIL_REF = 0x0B97
STENCIL_WRITEMASK = 0x0B98
MATRIX_MODE = 0x0BA0
VIEWPORT = 0x0BA2
MODELVIEW_STACK_DEPTH = 0x0BA3
PROJECTION_STACK_DEPTH = 0x0BA4
TEXTURE_STACK_DEPTH = 0x0BA5
MODELVIEW_MATRIX = 0x0BA6
PROJECTION_MATRIX = 0x0BA7
TEXTURE_MATRIX = 0x0BA8
ALPHA_TEST_FUNC = 0x0BC1
ALPHA_TEST_REF = 0x0BC2
BLEND_DST = 0x0BE0
BLEND_SRC = 0x0BE1
LOGIC_OP_MODE = 0x0BF0
SCISSOR_BOX = 0x0C10
COLOR_CLEAR_VALUE = 0x0C22
COLOR_WRITEMASK = 0x0C23
MAX_LIGHTS = 0x0D31
MAX_CLIP_PLANES = 0x0D32
MAX_TEXTURE_SIZE = 0x0D33
MAX_MODELVIEW_STACK_DEPTH = 0x0D36
MAX_PROJECTION_STACK_DEPTH = 0x0D38
MAX_TEXTURE_STACK_DEPTH = 0x0D39
MAX_VIEWPORT_DIMS = 0x0D3A
MAX_TEXTURE_UNITS = 0x84E2
SUBPIXEL_BITS = 0x0D50
RED_BITS = 0x0D52
GREEN_BITS = 0x0D53
BLUE_BITS = 0x0D54
ALPHA_BITS = 0x0D55
DEPTH_BITS = 0x0D56
STENCIL_BITS = 0x0D57
POLYGON_OFFSET_UNITS = 0x2A00
POLYGON_OFFSET_FILL = 0x8037
POLYGON_OFFSET_FACTOR = 0x8038
TEXTURE_BINDING_2D = 0x8069
VERTEX_ARRAY_SIZE = 0x807A
VERTEX_ARRAY_TYPE = 0x807B
VERTEX_ARRAY_STRIDE = 0x807C
NORMAL_ARRAY_TYPE = 0x807E
NORMAL_ARRAY_STRIDE = 0x807F
COLOR_ARRAY_SIZE = 0x8081
COLOR_ARRAY_TYPE = 0x8082
COLOR_ARRAY_STRIDE = 0x8083
TEXTURE_COORD_ARRAY_SIZE = 0x8088
TEXTURE_COORD_ARRAY_TYPE = 0x8089
TEXTURE_COORD_ARRAY_STRIDE = 0x808A
VERTEX_ARRAY_POINTER = 0x808E
NORMAL_ARRAY_POINTER = 0x808F
COLOR_ARRAY_POINTER = 0x8090
TEXTURE_COORD_ARRAY_POINTER = 0x8092
SAMPLE_BUFFERS = 0x80A8
SAMPLES = 0x80A9
SAMPLE_COVERAGE_VALUE = 0x80AA
SAMPLE_COVERAGE_INVERT = 0x80AB
NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
COMPRESSED_TEXTURE_FORMATS = 0x86A3
DONT_CARE = 0x1100
FASTEST = 0x1101
NICEST = 0x1102
PERSPECTIVE_CORRECTION_HINT = 0x0C50
POINT_SMOOTH_HINT = 0x0C51
LINE_SMOOTH_HINT = 0x0C52
FOG_HINT = 0x0C54
GENERATE_MIPMAP_HINT = 0x8192
LIGHT_MODEL_AMBIENT = 0x0B53
LIGHT_MODEL_TWO_SIDE = 0x0B52
AMBIENT = 0x1200
DIFFUSE = 0x1201
SPECULAR = 0x1202
POSITION = 0x1203
SPOT_DIRECTION = 0x1204
SPOT_EXPONENT = 0x1205
SPOT_CUTOFF = 0x1206
CONSTANT_ATTENUATION = 0x1207
LINEAR_ATTENUATION = 0x1208
QUADRATIC_ATTENUATION = 0x1209
BYTE = 0x1400
UNSIGNED_BYTE = 0x1401
SHORT = 0x1402
UNSIGNED_SHORT = 0x1403
FLOAT = 0x1406
FIXED = 0x140C
CLEAR = 0x1500
AND = 0x1501
AND_REVERSE = 0x1502
COPY = 0x1503
AND_INVERTED = 0x1504
NOOP = 0x1505
XOR = 0x1506
OR = 0x1507
NOR = 0x1508
EQUIV = 0x1509
INVERT = 0x150A
OR_REVERSE = 0x150B
COPY_INVERTED = 0x150C
OR_INVERTED = 0x150D
NAND = 0x150E
SET = 0x150F
EMISSION = 0x1600
SHININESS = 0x1601
AMBIENT_AND_DIFFUSE = 0x1602
MODELVIEW = 0x1700
PROJECTION = 0x1701
TEXTURE = 0x1702
ALPHA = 0x1906
RGB = 0x1907
RGBA = 0x1908
LUMINANCE = 0x1909
LUMINANCE_ALPHA = 0x190A
UNPACK_ALIGNMENT = 0x0CF5
PACK_ALIGNMENT = 0x0D05
UNSIGNED_SHORT_4_4_4_4 = 0x8033
UNSIGNED_SHORT_5_5_5_1 = 0x8034
UNSIGNED_SHORT_5_6_5 = 0x8363
FLAT = 0x1D00
SMOOTH = 0x1D01
KEEP = 0x1E00
REPLACE = 0x1E01
INCR = 0x1E02
DECR = 0x1E03
VENDOR = 0x1F00
RENDERER = 0x1F01
VERSION = 0x1F02
EXTENSIONS = 0x1F03
MODULATE = 0x2100
DECAL = 0x2101
ADD = 0x0104
TEXTURE_ENV_MODE = 0x2200
TEXTURE_ENV_COLOR = 0x2201
TEXTURE_ENV = 0x2300
NEAREST = 0x2600
LINEAR = 0x2601
NEAREST_MIPMAP_NEAREST = 0x2700
LINEAR_MIPMAP_NEAREST = 0x2701
NEAREST_MIPMAP_LINEAR = 0x2702
LINEAR_MIPMAP_LINEAR = 0x2703
TEXTURE_MAG_FILTER = 0x2800
TEXTURE_MIN_FILTER = 0x2801
TEXTURE_WRAP_S = 0x2802
TEXTURE_WRAP_T = 0x2803
GENERATE_MIPMAP = 0x8191
TEXTURE0 = 0x84C0
TEXTURE1 = 0x84C1
TEXTURE2 = 0x84C2
TEXTURE3 = 0x84C3
TEXTURE4 = 0x84C4
TEXTURE5 = 0x84C5
TEXTURE6 = 0x84C6
TEXTURE7 = 0x84C7
TEXTURE8 = 0x84C8
TEXTURE9 = 0x84C9
TEXTURE10 = 0x84CA
TEXTURE11 = 0x84CB
TEXTURE12 = 0x84CC
TEXTURE13 = 0x84CD
TEXTURE14 = 0x84CE
TEXTURE15 = 0x84CF
TEXTURE16 = 0x84D0
TEXTURE17 = 0x84D1
TEXTURE18 = 0x84D2
TEXTURE19 = 0x84D3
TEXTURE20 = 0x84D4
TEXTURE21 = 0x84D5
TEXTURE22 = 0x84D6
TEXTURE23 = 0x84D7
TEXTURE24 = 0x84D8
TEXTURE25 = 0x84D9
TEXTURE26 = 0x84DA
TEXTURE27 = 0x84DB
TEXTURE28 = 0x84DC
TEXTURE29 = 0x84DD
TEXTURE30 = 0x84DE
TEXTURE31 = 0x84DF
ACTIVE_TEXTURE = 0x84E0
CLIENT_ACTIVE_TEXTURE = 0x84E1
REPEAT = 0x2901
CLAMP_TO_EDGE = 0x812F
LIGHT0 = 0x4000
LIGHT1 = 0x4001
LIGHT2 = 0x4002
LIGHT3 = 0x4003
LIGHT4 = 0x4004
LIGHT5 = 0x4005
LIGHT6 = 0x4006
LIGHT7 = 0x4007
ARRAY_BUFFER = 0x8892
ELEMENT_ARRAY_BUFFER = 0x8893
ARRAY_BUFFER_BINDING = 0x8894
ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
VERTEX_ARRAY_BUFFER_BINDING = 0x8896
NORMAL_ARRAY_BUFFER_BINDING = 0x8897
COLOR_ARRAY_BUFFER_BINDING = 0x8898
TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
STATIC_DRAW = 0x88E4
DYNAMIC_DRAW = 0x88E8
BUFFER_SIZE = 0x8764
BUFFER_USAGE = 0x8765
SUBTRACT = 0x84E7
COMBINE = 0x8570
COMBINE_RGB = 0x8571
COMBINE_ALPHA = 0x8572
RGB_SCALE = 0x8573
ADD_SIGNED = 0x8574
INTERPOLATE = 0x8575
CONSTANT = 0x8576
PRIMARY_COLOR = 0x8577
PREVIOUS = 0x8578
OPERAND0_RGB = 0x8590
OPERAND1_RGB = 0x8591
OPERAND2_RGB = 0x8592
OPERAND0_ALPHA = 0x8598
OPERAND1_ALPHA = 0x8599
OPERAND2_ALPHA = 0x859A
ALPHA_SCALE = 0x0D1C
SRC0_RGB = 0x8580
SRC1_RGB = 0x8581
SRC2_RGB = 0x8582
SRC0_ALPHA = 0x8588
SRC1_ALPHA = 0x8589
SRC2_ALPHA = 0x858A
DOT3_RGB = 0x86AE
DOT3_RGBA = 0x86AF
@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def alpha_func(func, ref): 
    '''specify the alpha test function'''

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def clear_color(red, green, blue, alpha): 
    '''specify clear values for the color buffers'''

@accepts(t.float)
@returns(t.void)
@binds(dll)
def clear_depthf(d): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def clip_planef(p, eqn): 
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def color4f(red, green, blue, alpha): 
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def depth_rangef(n, f): 
    pass

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def fogf(pname, param): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def fogfv(pname, params): 
    pass

@accepts(t.float, t.float, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def frustumf(l, r, b, t, n, f): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_clip_planef(plane, equation): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_floatv(pname, data): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_lightfv(light, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_materialfv(face, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_envfv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_parameterfv(target, pname, params): 
    pass

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def light_modelf(pname, param): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def light_modelfv(pname, params): 
    pass

@accepts(t.enum, t.enum, t.float)
@returns(t.void)
@binds(dll)
def lightf(light, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def lightfv(light, pname, params): 
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def line_width(width): 
    '''specify the width of rasterized lines'''

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def load_matrixf(m): 
    pass

@accepts(t.enum, t.enum, t.float)
@returns(t.void)
@binds(dll)
def materialf(face, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def materialfv(face, pname, params): 
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def mult_matrixf(m): 
    pass

@accepts(t.enum, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def multi_tex_coord4f(target, s, t, r, q): 
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def normal3f(nx, ny, nz): 
    pass

@accepts(t.float, t.float, t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def orthof(l, r, b, t, n, f): 
    pass

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def point_parameterf(pname, param): 
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def point_parameterfv(pname, params): 
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def point_size(size): 
    '''specify the diameter of rasterized points'''

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def polygon_offset(factor, units): 
    '''set the scale and units used to calculate depth values'''

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def rotatef(angle, x, y, z): 
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def scalef(x, y, z): 
    pass

@accepts(t.enum, t.enum, t.float)
@returns(t.void)
@binds(dll)
def tex_envf(target, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_envfv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, t.float)
@returns(t.void)
@binds(dll)
def tex_parameterf(target, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_parameterfv(target, pname, params): 
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def translatef(x, y, z): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def active_texture(texture): 
    '''select active texture unit'''

@accepts(t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def alpha_funcx(func, ref): 
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def bind_buffer(target, buffer): 
    '''bind a named buffer object'''

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def bind_texture(target, texture): 
    '''bind a named texture to a texturing target'''

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_func(sfactor, dfactor): 
    '''specify pixel arithmetic'''

@accepts(t.enum, t.sizeiptr, t.void, t.enum)
@returns(t.void)
@binds(dll)
def buffer_data(target, size, data, usage): 
    '''creates and initializes a buffer object's data store'''

@accepts(t.enum, t.intptr, t.sizeiptr, t.void)
@returns(t.void)
@binds(dll)
def buffer_sub_data(target, offset, size, data): 
    '''updates a subset of a buffer object's data store'''

@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def clear(mask): 
    '''clear buffers to preset values'''

@accepts(t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def clear_colorx(red, green, blue, alpha): 
    pass

@accepts(t.fixed)
@returns(t.void)
@binds(dll)
def clear_depthx(depth): 
    pass

@accepts(t.int)
@returns(t.void)
@binds(dll)
def clear_stencil(s): 
    '''specify the clear value for the stencil buffer'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def client_active_texture(texture): 
    '''select active texture unit'''

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def clip_planex(plane, equation): 
    pass

@accepts(t.ubyte, t.ubyte, t.ubyte, t.ubyte)
@returns(t.void)
@binds(dll)
def color4ub(red, green, blue, alpha): 
    pass

@accepts(t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def color4x(red, green, blue, alpha): 
    pass

@accepts(t.boolean, t.boolean, t.boolean, t.boolean)
@returns(t.void)
@binds(dll)
def color_mask(red, green, blue, alpha): 
    '''enable and disable writing of frame buffer color components'''

@accepts(t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def color_pointer(size, type, stride, pointer): 
    '''define an array of colors'''

@accepts(t.enum, t.int, t.enum, t.sizei, t.sizei, t.int, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def compressed_tex_image2_d(target, level, internalformat, width, height, border, imageSize, data): 
    '''specify a two-dimensional texture image in a compressed format'''

@accepts(t.enum, t.int, t.int, t.int, t.sizei, t.sizei, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def compressed_tex_sub_image2_d(target, level, xoffset, yoffset, width, height, format, imageSize, data): 
    '''specify a two-dimensional texture subimage in a compressed format'''

@accepts(t.enum, t.int, t.enum, t.int, t.int, t.sizei, t.sizei, t.int)
@returns(t.void)
@binds(dll)
def copy_tex_image2_d(target, level, internalformat, x, y, width, height, border): 
    '''copy pixels into a 2D texture image'''

@accepts(t.enum, t.int, t.int, t.int, t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def copy_tex_sub_image2_d(target, level, xoffset, yoffset, x, y, width, height): 
    '''copy a two-dimensional texture subimage'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def cull_face(mode): 
    '''specify whether front- or back-facing facets can be culled'''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_buffers(n, buffers): 
    '''delete named buffer objects'''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_textures(n, textures): 
    '''delete named textures'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def depth_func(func): 
    '''specify the value used for depth buffer comparisons'''

@accepts(t.boolean)
@returns(t.void)
@binds(dll)
def depth_mask(flag): 
    '''enable or disable writing into the depth buffer'''

@accepts(t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def depth_rangex(n, f): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def disable(cap): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def disable_client_state(array): 
    pass

@accepts(t.enum, t.int, t.sizei)
@returns(t.void)
@binds(dll)
def draw_arrays(mode, first, count): 
    '''render primitives from array data'''

@accepts(t.enum, t.sizei, t.enum, t.void)
@returns(t.void)
@binds(dll)
def draw_elements(mode, count, type, indices): 
    '''render primitives from array data'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def enable(cap): 
    '''enable or disable server-side GL capabilities'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def enable_client_state(array): 
    '''enable or disable client-side capability'''

@accepts()
@returns(t.void)
@binds(dll)
def finish(): 
    '''block until all GL execution is complete'''

@accepts()
@returns(t.void)
@binds(dll)
def flush(): 
    '''force execution of GL commands in finite time'''

@accepts(t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def fogx(pname, param): 
    pass

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def fogxv(pname, param): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def front_face(mode): 
    '''define front- and back-facing polygons'''

@accepts(t.fixed, t.fixed, t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def frustumx(l, r, b, t, n, f): 
    pass

@accepts(t.enum, POINTER(t.boolean))
@returns(t.void)
@binds(dll)
def get_booleanv(pname, data): 
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_buffer_parameteriv(target, pname, params): 
    '''return parameters of a buffer object'''

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_clip_planex(plane, equation): 
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_buffers(n, buffers): 
    '''generate buffer object names'''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_textures(n, textures): 
    '''generate texture names'''

@accepts()
@returns(t.enum)
@binds(dll)
def get_error(): 
    '''return error information'''

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_fixedv(pname, params): 
    pass

@accepts(t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_integerv(pname, data): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_lightxv(light, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_materialxv(face, pname, params): 
    pass

@accepts(t.enum, t.void)
@returns(t.void)
@binds(dll)
def get_pointerv(pname, params): 
    '''return the address of the specified pointer'''

@accepts(t.enum)
@returns(POINTER(t.ubyte))
@binds(dll)
def get_string(name): 
    '''return a string describing the current GL connection'''

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_enviv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_tex_envxv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_parameteriv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def get_tex_parameterxv(target, pname, params): 
    pass

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def hint(target, mode): 
    '''specify implementation-specific hints'''

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_buffer(buffer): 
    '''determine if a name corresponds to a buffer object'''

@accepts(t.enum)
@returns(t.boolean)
@binds(dll)
def is_enabled(cap): 
    '''test whether a capability is enabled'''

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_texture(texture): 
    '''determine if a name corresponds to a texture'''

@accepts(t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def light_modelx(pname, param): 
    pass

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def light_modelxv(pname, param): 
    pass

@accepts(t.enum, t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def lightx(light, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def lightxv(light, pname, params): 
    pass

@accepts(t.fixed)
@returns(t.void)
@binds(dll)
def line_widthx(width): 
    pass

@accepts()
@returns(t.void)
@binds(dll)
def load_identity(): 
    '''replace the current matrix with the identity matrix'''

@accepts(POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def load_matrixx(m): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def logic_op(opcode): 
    '''specify a logical pixel operation for rendering'''

@accepts(t.enum, t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def materialx(face, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def materialxv(face, pname, param): 
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def matrix_mode(mode): 
    '''specify which matrix is the current matrix'''

@accepts(POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def mult_matrixx(m): 
    pass

@accepts(t.enum, t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def multi_tex_coord4x(texture, s, t, r, q): 
    pass

@accepts(t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def normal3x(nx, ny, nz): 
    pass

@accepts(t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def normal_pointer(type, stride, pointer): 
    '''define an array of normals'''

@accepts(t.fixed, t.fixed, t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def orthox(l, r, b, t, n, f): 
    pass

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def pixel_storei(pname, param): 
    pass

@accepts(t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def point_parameterx(pname, param): 
    pass

@accepts(t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def point_parameterxv(pname, params): 
    pass

@accepts(t.fixed)
@returns(t.void)
@binds(dll)
def point_sizex(size): 
    pass

@accepts(t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def polygon_offsetx(factor, units): 
    pass

@accepts()
@returns(t.void)
@binds(dll)
def pop_matrix(): 
    pass

@accepts()
@returns(t.void)
@binds(dll)
def push_matrix(): 
    '''push and pop the current matrix stack'''

@accepts(t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def read_pixels(x, y, width, height, format, type, pixels): 
    '''read a block of pixels from the frame buffer'''

@accepts(t.fixed, t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def rotatex(angle, x, y, z): 
    pass

@accepts(t.float, t.boolean)
@returns(t.void)
@binds(dll)
def sample_coverage(value, invert): 
    '''specify multisample coverage parameters'''

@accepts(t.clampx, t.boolean)
@returns(t.void)
@binds(dll)
def sample_coveragex(value, invert): 
    pass

@accepts(t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def scalex(x, y, z): 
    pass

@accepts(t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def scissor(x, y, width, height): 
    '''define the scissor box'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def shade_model(mode): 
    '''select flat or smooth shading'''

@accepts(t.enum, t.int, t.uint)
@returns(t.void)
@binds(dll)
def stencil_func(func, ref, mask): 
    '''set front and back function and reference value for stencil testing'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def stencil_mask(mask): 
    '''control the front and back writing of individual bits in the stencil planes'''

@accepts(t.enum, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def stencil_op(fail, zfail, zpass): 
    '''set front and back stencil test actions'''

@accepts(t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def tex_coord_pointer(size, type, stride, pointer): 
    '''define an array of texture coordinates'''

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def tex_envi(target, pname, param): 
    pass

@accepts(t.enum, t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def tex_envx(target, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_enviv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def tex_envxv(target, pname, params): 
    pass

@accepts(t.enum, t.int, t.int, t.sizei, t.sizei, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_image2_d(target, level, internalformat, width, height, border, format, type, pixels): 
    '''specify a two-dimensional texture image'''

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def tex_parameteri(target, pname, param): 
    pass

@accepts(t.enum, t.enum, t.fixed)
@returns(t.void)
@binds(dll)
def tex_parameterx(target, pname, param): 
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_parameteriv(target, pname, params): 
    pass

@accepts(t.enum, t.enum, POINTER(t.fixed))
@returns(t.void)
@binds(dll)
def tex_parameterxv(target, pname, params): 
    pass

@accepts(t.enum, t.int, t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_sub_image2_d(target, level, xoffset, yoffset, width, height, format, type, pixels): 
    '''specify a two-dimensional texture subimage'''

@accepts(t.fixed, t.fixed, t.fixed)
@returns(t.void)
@binds(dll)
def translatex(x, y, z): 
    pass

@accepts(t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def vertex_pointer(size, type, stride, pointer): 
    '''define an array of vertex data'''

@accepts(t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def viewport(x, y, width, height): 
    '''set the viewport'''
