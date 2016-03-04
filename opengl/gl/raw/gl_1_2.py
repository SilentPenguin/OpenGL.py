#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.enum, t.uint, t.uint, t.sizei, t.enum, t.void)
@returns(t.void)
@binds(dll)
def draw_range_elements(mode, start, end, count, type, indices):
    '''render primitives from array data'''

@accepts(t.enum, t.int, t.int, t.sizei, t.sizei, t.sizei, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_image3_d(target, level, internalformat, width, height, depth, border, format, type, pixels):
    '''specify a three-dimensional texture image'''

@accepts(t.enum, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_sub_image3_d(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
    '''specify a three-dimensional texture subimage'''

@accepts(t.enum, t.int, t.int, t.int, t.int, t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def copy_tex_sub_image3_d(target, level, xoffset, yoffset, zoffset, x, y, width, height):
    '''copy a three-dimensional texture subimage'''

UNSIGNED_BYTE_3_3_2 = 0x8032
UNSIGNED_SHORT_4_4_4_4 = 0x8033
UNSIGNED_SHORT_5_5_5_1 = 0x8034
UNSIGNED_INT_8_8_8_8 = 0x8035
UNSIGNED_INT_10_10_10_2 = 0x8036
TEXTURE_BINDING_3D = 0x806A
PACK_SKIP_IMAGES = 0x806B
PACK_IMAGE_HEIGHT = 0x806C
UNPACK_SKIP_IMAGES = 0x806D
UNPACK_IMAGE_HEIGHT = 0x806E
TEXTURE_3D = 0x806F
PROXY_TEXTURE_3D = 0x8070
TEXTURE_DEPTH = 0x8071
TEXTURE_WRAP_R = 0x8072
MAX_3D_TEXTURE_SIZE = 0x8073
UNSIGNED_BYTE_2_3_3_REV = 0x8362
UNSIGNED_SHORT_5_6_5 = 0x8363
UNSIGNED_SHORT_5_6_5_REV = 0x8364
UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
UNSIGNED_INT_8_8_8_8_REV = 0x8367
UNSIGNED_INT_2_10_10_10_REV = 0x8368
BGR = 0x80E0
BGRA = 0x80E1
MAX_ELEMENTS_VERTICES = 0x80E8
MAX_ELEMENTS_INDICES = 0x80E9
CLAMP_TO_EDGE = 0x812F
TEXTURE_MIN_LOD = 0x813A
TEXTURE_MAX_LOD = 0x813B
TEXTURE_BASE_LEVEL = 0x813C
TEXTURE_MAX_LEVEL = 0x813D
SMOOTH_POINT_SIZE_RANGE = 0x0B12
SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
SMOOTH_LINE_WIDTH_RANGE = 0x0B22
SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
ALIASED_LINE_WIDTH_RANGE = 0x846E
RESCALE_NORMAL = 0x803A
LIGHT_MODEL_COLOR_CONTROL = 0x81F8
SINGLE_COLOR = 0x81F9
SEPARATE_SPECULAR_COLOR = 0x81FA
ALIASED_POINT_SIZE_RANGE = 0x846D