#BEWARE: automatically generated code
#This code was generated by /generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.enum, t.enum, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_func_separate(sfactorrgb, dfactorrgb, sfactoralpha, dfactoralpha):
    '''
    specify pixel arithmetic for RGB and alpha components separately.
    
    gl.blend_func_separate defines the operation of blending for all draw
    buffers when it is enabled. gl.blend_func_separatei defines the operation of
    blending for a single draw buffer specified by buf when enabled for that
    draw buffer. srcRGB specifies which method is used to scale the source RGB-
    color components. dstRGB specifies which method is used to scale the
    destination RGB-color components.
    
    Args:
        sfactorrgb: how the red, green, and blue blending factors are computed.
        dfactorrgb: how the red, green, and blue destination blending factors
            are computed.
        sfactoralpha: specified how the alpha source blending factor is
            computed.
        dfactoralpha: specified how the alpha destination blending factor is
            computed.
    '''

@accepts(t.enum, POINTER(t.int), POINTER(t.sizei), t.sizei)
@returns(t.void)
@binds(dll)
def multi_draw_arrays(mode, first, count, drawcount):
    '''
    render multiple sets of primitives from array data.
    
    gl.multi_draw_arrays specifies multiple sets of geometric primitives with
    very few subroutine calls. Instead of calling a GL procedure to pass each
    individual vertex, normal, texture coordinate, edge flag, or color, you can
    prespecify separate arrays of vertices, normals, and colors and use them to
    construct a sequence of primitives with a single call to
    gl.multi_draw_arrays.
    
    Args:
        mode: what kind of primitives to render.
        first: points to an array of starting indices in the enabled arrays.
        count: points to an array of the number of indices to be rendered.
        drawcount: the size of the first and count.
    '''

@accepts(t.enum, POINTER(t.sizei), t.enum, t.void, t.sizei)
@returns(t.void)
@binds(dll)
def multi_draw_elements(mode, count, type, indices, drawcount):
    '''
    render multiple sets of primitives by specifying indices of array data
    elements.
    
    gl.multi_draw_elements specifies multiple sets of geometric primitives with
    very few subroutine calls. Instead of calling a GL function to pass each
    individual vertex, normal, texture coordinate, edge flag, or color, you can
    prespecify separate arrays of vertices, normals, and so on, and use them to
    construct a sequence of primitives with a single call to
    gl.multi_draw_elements.
    
    Args:
        mode: what kind of primitives to render.
        count: points to an array of the elements counts.
        type: the type of the values in indices.
        indices: a pointer to the location where the indices are stored.
        drawcount: the size of the count and indices arrays.
    '''

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

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def point_parameteri(pname, param):
    pass

@accepts(t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def point_parameteriv(pname, params):
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def fog_coordf(coord):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def fog_coordfv(coord):
    pass

@accepts(t.double)
@returns(t.void)
@binds(dll)
def fog_coordd(coord):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def fog_coorddv(coord):
    pass

@accepts(t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def fog_coord_pointer(type, stride, pointer):
    '''
    define an array of fog coordinates.
    
    gl.fog_coord_pointer specifies the location and data format of an array of
    fog coordinates to use when rendering. type specifies the data type of each
    fog coordinate, and stride specifies the byte stride from one fog coordinate
    to the next, allowing vertices and attributes to be packed into a single
    array or stored in separate arrays.
    
    Args:
        type: the data type of each fog coordinate.
        stride: the byte offset between consecutive fog coordinates.
        pointer: a pointer to the first coordinate of the first fog coordinate
            in the array.
    '''

@accepts(t.byte, t.byte, t.byte)
@returns(t.void)
@binds(dll)
def secondary_color3b(red, green, blue):
    pass

@accepts(POINTER(t.byte))
@returns(t.void)
@binds(dll)
def secondary_color3bv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def secondary_color3d(red, green, blue):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def secondary_color3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def secondary_color3f(red, green, blue):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def secondary_color3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def secondary_color3i(red, green, blue):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def secondary_color3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def secondary_color3s(red, green, blue):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def secondary_color3sv(v):
    pass

@accepts(t.ubyte, t.ubyte, t.ubyte)
@returns(t.void)
@binds(dll)
def secondary_color3ub(red, green, blue):
    pass

@accepts(POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def secondary_color3ubv(v):
    pass

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def secondary_color3ui(red, green, blue):
    pass

@accepts(POINTER(t.uint))
@returns(t.void)
@binds(dll)
def secondary_color3uiv(v):
    pass

@accepts(t.ushort, t.ushort, t.ushort)
@returns(t.void)
@binds(dll)
def secondary_color3us(red, green, blue):
    pass

@accepts(POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def secondary_color3usv(v):
    pass

@accepts(t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def secondary_color_pointer(size, type, stride, pointer):
    '''
    define an array of secondary colors.
    
    gl.secondary_color_pointer specifies the location and data format of an
    array of color components to use when rendering. size specifies the number
    of components per color, and must be 3. type specifies the data type of each
    color component, and stride specifies the byte stride from one color to the
    next, allowing vertices and attributes to be packed into a single array or
    stored in separate arrays.
    
    Args:
        size: the number of components per color.
        type: the data type of each color component in the array.
        stride: the byte offset between consecutive colors.
        pointer: a pointer to the first component of the first color element in
            the array.
    '''

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def window_pos2d(x, y):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def window_pos2dv(v):
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def window_pos2f(x, y):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def window_pos2fv(v):
    pass

@accepts(t.int, t.int)
@returns(t.void)
@binds(dll)
def window_pos2i(x, y):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def window_pos2iv(v):
    pass

@accepts(t.short, t.short)
@returns(t.void)
@binds(dll)
def window_pos2s(x, y):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def window_pos2sv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def window_pos3d(x, y, z):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def window_pos3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def window_pos3f(x, y, z):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def window_pos3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def window_pos3i(x, y, z):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def window_pos3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def window_pos3s(x, y, z):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def window_pos3sv(v):
    pass

BLEND_DST_RGB = 0x80C8
BLEND_SRC_RGB = 0x80C9
BLEND_DST_ALPHA = 0x80CA
BLEND_SRC_ALPHA = 0x80CB
POINT_FADE_THRESHOLD_SIZE = 0x8128
DEPTH_COMPONENT16 = 0x81A5
DEPTH_COMPONENT24 = 0x81A6
DEPTH_COMPONENT32 = 0x81A7
MIRRORED_REPEAT = 0x8370
MAX_TEXTURE_LOD_BIAS = 0x84FD
TEXTURE_LOD_BIAS = 0x8501
INCR_WRAP = 0x8507
DECR_WRAP = 0x8508
TEXTURE_DEPTH_SIZE = 0x884A
TEXTURE_COMPARE_MODE = 0x884C
TEXTURE_COMPARE_FUNC = 0x884D
POINT_SIZE_MIN = 0x8126
POINT_SIZE_MAX = 0x8127
POINT_DISTANCE_ATTENUATION = 0x8129
GENERATE_MIPMAP = 0x8191
GENERATE_MIPMAP_HINT = 0x8192
FOG_COORDINATE_SOURCE = 0x8450
FOG_COORDINATE = 0x8451
FRAGMENT_DEPTH = 0x8452
CURRENT_FOG_COORDINATE = 0x8453
FOG_COORDINATE_ARRAY_TYPE = 0x8454
FOG_COORDINATE_ARRAY_STRIDE = 0x8455
FOG_COORDINATE_ARRAY_POINTER = 0x8456
FOG_COORDINATE_ARRAY = 0x8457
COLOR_SUM = 0x8458
CURRENT_SECONDARY_COLOR = 0x8459
SECONDARY_COLOR_ARRAY_SIZE = 0x845A
SECONDARY_COLOR_ARRAY_TYPE = 0x845B
SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
SECONDARY_COLOR_ARRAY_POINTER = 0x845D
SECONDARY_COLOR_ARRAY = 0x845E
TEXTURE_FILTER_CONTROL = 0x8500
DEPTH_TEXTURE_MODE = 0x884B
COMPARE_R_TO_TEXTURE = 0x884E
@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def blend_color(red, green, blue, alpha):
    '''
    set the blend color.
    
    Args:
        red: the components of gl_blend_color.
        green: the components of gl_blend_color.
        blue: the components of gl_blend_color.
        alpha: the components of gl_blend_color.
    '''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def blend_equation(mode):
    '''
    specify the equation used for both the RGB blend equation and the Alpha
    blend equation.
    
    Args:
        mode: how source and destination colors are combined.
    '''

FUNC_ADD = 0x8006
FUNC_SUBTRACT = 0x800A
FUNC_REVERSE_SUBTRACT = 0x800B
MIN = 0x8007
MAX = 0x8008
CONSTANT_COLOR = 0x8001
ONE_MINUS_CONSTANT_COLOR = 0x8002
CONSTANT_ALPHA = 0x8003
ONE_MINUS_CONSTANT_ALPHA = 0x8004