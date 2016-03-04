#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def cull_face(mode):
    '''specify whether front- or back-facing facets can be culled'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def front_face(mode):
    '''define front- and back-facing polygons'''

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def hint(target, mode):
    '''specify implementation-specific hints'''

@accepts(t.float)
@returns(t.void)
@binds(dll)
def line_width(width):
    '''specify the width of rasterized lines'''

@accepts(t.float)
@returns(t.void)
@binds(dll)
def point_size(size):
    '''specify the diameter of rasterized points'''

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def polygon_mode(face, mode):
    '''select a polygon rasterization mode'''

@accepts(t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def scissor(x, y, width, height):
    '''define the scissor box'''

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

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def tex_parameteri(target, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_parameteriv(target, pname, params):
    pass

@accepts(t.enum, t.int, t.int, t.sizei, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_image1_d(target, level, internalformat, width, border, format, type, pixels):
    '''specify a one-dimensional texture image'''

@accepts(t.enum, t.int, t.int, t.sizei, t.sizei, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def tex_image2_d(target, level, internalformat, width, height, border, format, type, pixels):
    '''specify a two-dimensional texture image'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def draw_buffer(buf):
    '''specify which color buffers are to be drawn into'''

@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def clear(mask):
    '''clear buffers to preset values'''

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def clear_color(red, green, blue, alpha):
    '''specify clear values for the color buffers'''

@accepts(t.int)
@returns(t.void)
@binds(dll)
def clear_stencil(s):
    '''specify the clear value for the stencil buffer'''

@accepts(t.double)
@returns(t.void)
@binds(dll)
def clear_depth(depth):
    '''specify the clear value for the depth buffer'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def stencil_mask(mask):
    '''control the front and back writing of individual bits in the stencil planes'''

@accepts(t.boolean, t.boolean, t.boolean, t.boolean)
@returns(t.void)
@binds(dll)
def color_mask(red, green, blue, alpha):
    '''enable and disable writing of frame buffer color components'''

@accepts(t.boolean)
@returns(t.void)
@binds(dll)
def depth_mask(flag):
    '''enable or disable writing into the depth buffer'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def disable(cap):
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def enable(cap):
    '''enable or disable server-side GL capabilities'''

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

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def blend_func(sfactor, dfactor):
    '''specify pixel arithmetic'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def logic_op(opcode):
    '''specify a logical pixel operation for rendering'''

@accepts(t.enum, t.int, t.uint)
@returns(t.void)
@binds(dll)
def stencil_func(func, ref, mask):
    '''set front and back function and reference value for stencil testing'''

@accepts(t.enum, t.enum, t.enum)
@returns(t.void)
@binds(dll)
def stencil_op(fail, zfail, zpass):
    '''set front and back stencil test actions'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def depth_func(func):
    '''specify the value used for depth buffer comparisons'''

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def pixel_storef(pname, param):
    pass

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def pixel_storei(pname, param):
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def read_buffer(src):
    '''select a color buffer source for pixels'''

@accepts(t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def read_pixels(x, y, width, height, format, type, pixels):
    '''read a block of pixels from the frame buffer'''

@accepts(t.enum, POINTER(t.boolean))
@returns(t.void)
@binds(dll)
def get_booleanv(pname, data):
    pass

@accepts(t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_doublev(pname, data):
    pass

@accepts()
@returns(t.enum)
@binds(dll)
def get_error():
    '''return error information'''

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_floatv(pname, data):
    pass

@accepts(t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_integerv(pname, data):
    pass

@accepts(t.enum)
@returns(POINTER(t.ubyte))
@binds(dll)
def get_string(name):
    '''return a string describing the current GL connection'''

@accepts(t.enum, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def get_tex_image(target, level, format, type, pixels):
    '''return a texture image'''

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_parameterfv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_parameteriv(target, pname, params):
    pass

@accepts(t.enum, t.int, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_level_parameterfv(target, level, pname, params):
    pass

@accepts(t.enum, t.int, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_level_parameteriv(target, level, pname, params):
    pass

@accepts(t.enum)
@returns(t.boolean)
@binds(dll)
def is_enabled(cap):
    '''test whether a capability is enabled'''

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def depth_range(near, far):
    '''specify mapping of depth values from normalized device coordinates to window coordinates'''

@accepts(t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def viewport(x, y, width, height):
    '''set the viewport'''

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def new_list(list, mode):
    '''create or replace a display list'''

@accepts()
@returns(t.void)
@binds(dll)
def end_list():
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def call_list(list):
    '''execute a display list'''

@accepts(t.sizei, t.enum, t.void)
@returns(t.void)
@binds(dll)
def call_lists(n, type, lists):
    '''execute a list of display lists'''

@accepts(t.uint, t.sizei)
@returns(t.void)
@binds(dll)
def delete_lists(list, range):
    '''delete a contiguous group of display lists'''

@accepts(t.sizei)
@returns(t.uint)
@binds(dll)
def gen_lists(range):
    '''generate a contiguous set of empty display lists'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def list_base(base):
    '''set the display-list base for gl.call_lists'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def begin(mode):
    '''delimit the vertices of a primitive or a group of like primitives'''

@accepts(t.sizei, t.sizei, t.float, t.float, t.float, t.float, POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def bitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    '''draw a bitmap'''

@accepts(t.byte, t.byte, t.byte)
@returns(t.void)
@binds(dll)
def color3b(red, green, blue):
    pass

@accepts(POINTER(t.byte))
@returns(t.void)
@binds(dll)
def color3bv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def color3d(red, green, blue):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def color3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def color3f(red, green, blue):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def color3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def color3i(red, green, blue):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def color3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def color3s(red, green, blue):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def color3sv(v):
    pass

@accepts(t.ubyte, t.ubyte, t.ubyte)
@returns(t.void)
@binds(dll)
def color3ub(red, green, blue):
    pass

@accepts(POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def color3ubv(v):
    pass

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def color3ui(red, green, blue):
    pass

@accepts(POINTER(t.uint))
@returns(t.void)
@binds(dll)
def color3uiv(v):
    pass

@accepts(t.ushort, t.ushort, t.ushort)
@returns(t.void)
@binds(dll)
def color3us(red, green, blue):
    pass

@accepts(POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def color3usv(v):
    pass

@accepts(t.byte, t.byte, t.byte, t.byte)
@returns(t.void)
@binds(dll)
def color4b(red, green, blue, alpha):
    pass

@accepts(POINTER(t.byte))
@returns(t.void)
@binds(dll)
def color4bv(v):
    pass

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def color4d(red, green, blue, alpha):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def color4dv(v):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def color4f(red, green, blue, alpha):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def color4fv(v):
    pass

@accepts(t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def color4i(red, green, blue, alpha):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def color4iv(v):
    pass

@accepts(t.short, t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def color4s(red, green, blue, alpha):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def color4sv(v):
    pass

@accepts(t.ubyte, t.ubyte, t.ubyte, t.ubyte)
@returns(t.void)
@binds(dll)
def color4ub(red, green, blue, alpha):
    pass

@accepts(POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def color4ubv(v):
    pass

@accepts(t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def color4ui(red, green, blue, alpha):
    pass

@accepts(POINTER(t.uint))
@returns(t.void)
@binds(dll)
def color4uiv(v):
    pass

@accepts(t.ushort, t.ushort, t.ushort, t.ushort)
@returns(t.void)
@binds(dll)
def color4us(red, green, blue, alpha):
    pass

@accepts(POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def color4usv(v):
    pass

@accepts(t.boolean)
@returns(t.void)
@binds(dll)
def edge_flag(flag):
    '''flag edges as either boundary or nonboundary'''

@accepts(POINTER(t.boolean))
@returns(t.void)
@binds(dll)
def edge_flagv(flag):
    pass

@accepts()
@returns(t.void)
@binds(dll)
def end():
    pass

@accepts(t.double)
@returns(t.void)
@binds(dll)
def indexd(c):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def indexdv(c):
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def indexf(c):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def indexfv(c):
    pass

@accepts(t.int)
@returns(t.void)
@binds(dll)
def indexi(c):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def indexiv(c):
    pass

@accepts(t.short)
@returns(t.void)
@binds(dll)
def indexs(c):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def indexsv(c):
    pass

@accepts(t.byte, t.byte, t.byte)
@returns(t.void)
@binds(dll)
def normal3b(nx, ny, nz):
    pass

@accepts(POINTER(t.byte))
@returns(t.void)
@binds(dll)
def normal3bv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def normal3d(nx, ny, nz):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def normal3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def normal3f(nx, ny, nz):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def normal3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def normal3i(nx, ny, nz):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def normal3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def normal3s(nx, ny, nz):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def normal3sv(v):
    pass

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def raster_pos2d(x, y):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def raster_pos2dv(v):
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def raster_pos2f(x, y):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def raster_pos2fv(v):
    pass

@accepts(t.int, t.int)
@returns(t.void)
@binds(dll)
def raster_pos2i(x, y):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def raster_pos2iv(v):
    pass

@accepts(t.short, t.short)
@returns(t.void)
@binds(dll)
def raster_pos2s(x, y):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def raster_pos2sv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def raster_pos3d(x, y, z):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def raster_pos3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def raster_pos3f(x, y, z):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def raster_pos3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def raster_pos3i(x, y, z):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def raster_pos3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def raster_pos3s(x, y, z):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def raster_pos3sv(v):
    pass

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def raster_pos4d(x, y, z, w):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def raster_pos4dv(v):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def raster_pos4f(x, y, z, w):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def raster_pos4fv(v):
    pass

@accepts(t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def raster_pos4i(x, y, z, w):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def raster_pos4iv(v):
    pass

@accepts(t.short, t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def raster_pos4s(x, y, z, w):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def raster_pos4sv(v):
    pass

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def rectd(x1, y1, x2, y2):
    pass

@accepts(POINTER(t.double), POINTER(t.double))
@returns(t.void)
@binds(dll)
def rectdv(v1, v2):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def rectf(x1, y1, x2, y2):
    pass

@accepts(POINTER(t.float), POINTER(t.float))
@returns(t.void)
@binds(dll)
def rectfv(v1, v2):
    pass

@accepts(t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def recti(x1, y1, x2, y2):
    pass

@accepts(POINTER(t.int), POINTER(t.int))
@returns(t.void)
@binds(dll)
def rectiv(v1, v2):
    pass

@accepts(t.short, t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def rects(x1, y1, x2, y2):
    pass

@accepts(POINTER(t.short), POINTER(t.short))
@returns(t.void)
@binds(dll)
def rectsv(v1, v2):
    pass

@accepts(t.double)
@returns(t.void)
@binds(dll)
def tex_coord1d(s):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def tex_coord1dv(v):
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def tex_coord1f(s):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_coord1fv(v):
    pass

@accepts(t.int)
@returns(t.void)
@binds(dll)
def tex_coord1i(s):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_coord1iv(v):
    pass

@accepts(t.short)
@returns(t.void)
@binds(dll)
def tex_coord1s(s):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def tex_coord1sv(v):
    pass

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def tex_coord2d(s, t):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def tex_coord2dv(v):
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def tex_coord2f(s, t):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_coord2fv(v):
    pass

@accepts(t.int, t.int)
@returns(t.void)
@binds(dll)
def tex_coord2i(s, t):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_coord2iv(v):
    pass

@accepts(t.short, t.short)
@returns(t.void)
@binds(dll)
def tex_coord2s(s, t):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def tex_coord2sv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def tex_coord3d(s, t, r):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def tex_coord3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def tex_coord3f(s, t, r):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_coord3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def tex_coord3i(s, t, r):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_coord3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def tex_coord3s(s, t, r):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def tex_coord3sv(v):
    pass

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def tex_coord4d(s, t, r, q):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def tex_coord4dv(v):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def tex_coord4f(s, t, r, q):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_coord4fv(v):
    pass

@accepts(t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def tex_coord4i(s, t, r, q):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_coord4iv(v):
    pass

@accepts(t.short, t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def tex_coord4s(s, t, r, q):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def tex_coord4sv(v):
    pass

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex2d(x, y):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex2dv(v):
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def vertex2f(x, y):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def vertex2fv(v):
    pass

@accepts(t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex2i(x, y):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex2iv(v):
    pass

@accepts(t.short, t.short)
@returns(t.void)
@binds(dll)
def vertex2s(x, y):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def vertex2sv(v):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex3d(x, y, z):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex3dv(v):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def vertex3f(x, y, z):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def vertex3fv(v):
    pass

@accepts(t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex3i(x, y, z):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex3iv(v):
    pass

@accepts(t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def vertex3s(x, y, z):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def vertex3sv(v):
    pass

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def vertex4d(x, y, z, w):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def vertex4dv(v):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def vertex4f(x, y, z, w):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def vertex4fv(v):
    pass

@accepts(t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex4i(x, y, z, w):
    pass

@accepts(POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex4iv(v):
    pass

@accepts(t.short, t.short, t.short, t.short)
@returns(t.void)
@binds(dll)
def vertex4s(x, y, z, w):
    pass

@accepts(POINTER(t.short))
@returns(t.void)
@binds(dll)
def vertex4sv(v):
    pass

@accepts(t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def clip_plane(plane, equation):
    '''specify a plane against which all geometry is clipped'''

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def color_material(face, mode):
    '''cause a material color to track the current color'''

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

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def fogi(pname, param):
    pass

@accepts(t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def fogiv(pname, params):
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

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def lighti(light, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def lightiv(light, pname, params):
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

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def light_modeli(pname, param):
    pass

@accepts(t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def light_modeliv(pname, params):
    pass

@accepts(t.int, t.ushort)
@returns(t.void)
@binds(dll)
def line_stipple(factor, pattern):
    '''specify the line stipple pattern'''

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

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def materiali(face, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def materialiv(face, pname, params):
    pass

@accepts(POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def polygon_stipple(mask):
    '''set the polygon stippling pattern'''

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def shade_model(mode):
    '''select flat or smooth shading'''

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

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def tex_envi(target, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_enviv(target, pname, params):
    pass

@accepts(t.enum, t.enum, t.double)
@returns(t.void)
@binds(dll)
def tex_gend(coord, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def tex_gendv(coord, pname, params):
    pass

@accepts(t.enum, t.enum, t.float)
@returns(t.void)
@binds(dll)
def tex_genf(coord, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def tex_genfv(coord, pname, params):
    pass

@accepts(t.enum, t.enum, t.int)
@returns(t.void)
@binds(dll)
def tex_geni(coord, pname, param):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def tex_geniv(coord, pname, params):
    pass

@accepts(t.sizei, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def feedback_buffer(size, type, buffer):
    '''controls feedback mode'''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def select_buffer(size, buffer):
    '''establish a buffer for selection mode values'''

@accepts(t.enum)
@returns(t.int)
@binds(dll)
def render_mode(mode):
    '''set rasterization mode'''

@accepts()
@returns(t.void)
@binds(dll)
def init_names():
    '''initialize the name stack'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def load_name(name):
    '''load a name onto the name stack'''

@accepts(t.float)
@returns(t.void)
@binds(dll)
def pass_through(token):
    '''place a marker in the feedback buffer'''

@accepts()
@returns(t.void)
@binds(dll)
def pop_name():
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def push_name(name):
    '''push and pop the name stack'''

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def clear_accum(red, green, blue, alpha):
    '''specify clear values for the accumulation buffer'''

@accepts(t.float)
@returns(t.void)
@binds(dll)
def clear_index(c):
    '''specify the clear value for the color index buffers'''

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def index_mask(mask):
    '''control the writing of individual bits in the color index buffers'''

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def accum(op, value):
    '''operate on the accumulation buffer'''

@accepts()
@returns(t.void)
@binds(dll)
def pop_attrib():
    pass

@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def push_attrib(mask):
    '''push and pop the server attribute stack'''

@accepts(t.enum, t.double, t.double, t.int, t.int, POINTER(t.double))
@returns(t.void)
@binds(dll)
def map1d(target, u1, u2, stride, order, points):
    pass

@accepts(t.enum, t.float, t.float, t.int, t.int, POINTER(t.float))
@returns(t.void)
@binds(dll)
def map1f(target, u1, u2, stride, order, points):
    pass

@accepts(t.enum, t.double, t.double, t.int, t.int, t.double, t.double, t.int, t.int, POINTER(t.double))
@returns(t.void)
@binds(dll)
def map2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
    pass

@accepts(t.enum, t.float, t.float, t.int, t.int, t.float, t.float, t.int, t.int, POINTER(t.float))
@returns(t.void)
@binds(dll)
def map2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
    pass

@accepts(t.int, t.double, t.double)
@returns(t.void)
@binds(dll)
def map_grid1d(un, u1, u2):
    pass

@accepts(t.int, t.float, t.float)
@returns(t.void)
@binds(dll)
def map_grid1f(un, u1, u2):
    pass

@accepts(t.int, t.double, t.double, t.int, t.double, t.double)
@returns(t.void)
@binds(dll)
def map_grid2d(un, u1, u2, vn, v1, v2):
    pass

@accepts(t.int, t.float, t.float, t.int, t.float, t.float)
@returns(t.void)
@binds(dll)
def map_grid2f(un, u1, u2, vn, v1, v2):
    pass

@accepts(t.double)
@returns(t.void)
@binds(dll)
def eval_coord1d(u):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def eval_coord1dv(u):
    pass

@accepts(t.float)
@returns(t.void)
@binds(dll)
def eval_coord1f(u):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def eval_coord1fv(u):
    pass

@accepts(t.double, t.double)
@returns(t.void)
@binds(dll)
def eval_coord2d(u, v):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def eval_coord2dv(u):
    pass

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def eval_coord2f(u, v):
    pass

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def eval_coord2fv(u):
    pass

@accepts(t.enum, t.int, t.int)
@returns(t.void)
@binds(dll)
def eval_mesh1(mode, i1, i2):
    pass

@accepts(t.int)
@returns(t.void)
@binds(dll)
def eval_point1(i):
    pass

@accepts(t.enum, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def eval_mesh2(mode, i1, i2, j1, j2):
    pass

@accepts(t.int, t.int)
@returns(t.void)
@binds(dll)
def eval_point2(i, j):
    pass

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def alpha_func(func, ref):
    '''specify the alpha test function'''

@accepts(t.float, t.float)
@returns(t.void)
@binds(dll)
def pixel_zoom(xfactor, yfactor):
    '''specify the pixel zoom factors'''

@accepts(t.enum, t.float)
@returns(t.void)
@binds(dll)
def pixel_transferf(pname, param):
    pass

@accepts(t.enum, t.int)
@returns(t.void)
@binds(dll)
def pixel_transferi(pname, param):
    pass

@accepts(t.enum, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def pixel_mapfv(map, mapsize, values):
    pass

@accepts(t.enum, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def pixel_mapuiv(map, mapsize, values):
    pass

@accepts(t.enum, t.sizei, POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def pixel_mapusv(map, mapsize, values):
    pass

@accepts(t.int, t.int, t.sizei, t.sizei, t.enum)
@returns(t.void)
@binds(dll)
def copy_pixels(x, y, width, height, type):
    '''copy pixels in the frame buffer'''

@accepts(t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def draw_pixels(width, height, format, type, pixels):
    '''write a block of pixels to the frame buffer'''

@accepts(t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_clip_plane(plane, equation):
    '''return the coefficients of the specified clipping plane'''

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_lightfv(light, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_lightiv(light, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_mapdv(target, query, v):
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_mapfv(target, query, v):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_mapiv(target, query, v):
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_materialfv(face, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_materialiv(face, pname, params):
    pass

@accepts(t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_pixel_mapfv(map, values):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_pixel_mapuiv(map, values):
    pass

@accepts(t.enum, POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def get_pixel_mapusv(map, values):
    pass

@accepts(POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def get_polygon_stipple(mask):
    '''return the polygon stipple pattern'''

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_envfv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_enviv(target, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.double))
@returns(t.void)
@binds(dll)
def get_tex_gendv(coord, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_tex_genfv(coord, pname, params):
    pass

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_tex_geniv(coord, pname, params):
    pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_list(list):
    '''determine if a name corresponds to a display list'''

@accepts(t.double, t.double, t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def frustum(left, right, bottom, top, zNear, zFar):
    '''multiply the current matrix by a perspective matrix'''

@accepts()
@returns(t.void)
@binds(dll)
def load_identity():
    '''replace the current matrix with the identity matrix'''

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def load_matrixf(m):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def load_matrixd(m):
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def matrix_mode(mode):
    '''specify which matrix is the current matrix'''

@accepts(POINTER(t.float))
@returns(t.void)
@binds(dll)
def mult_matrixf(m):
    pass

@accepts(POINTER(t.double))
@returns(t.void)
@binds(dll)
def mult_matrixd(m):
    pass

@accepts(t.double, t.double, t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def ortho(left, right, bottom, top, zNear, zFar):
    '''multiply the current matrix with an orthographic matrix'''

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

@accepts(t.double, t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def rotated(angle, x, y, z):
    pass

@accepts(t.float, t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def rotatef(angle, x, y, z):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def scaled(x, y, z):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def scalef(x, y, z):
    pass

@accepts(t.double, t.double, t.double)
@returns(t.void)
@binds(dll)
def translated(x, y, z):
    pass

@accepts(t.float, t.float, t.float)
@returns(t.void)
@binds(dll)
def translatef(x, y, z):
    pass
