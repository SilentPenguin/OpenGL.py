#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

@accepts(t.uint, t.boolean, t.boolean, t.boolean, t.boolean)
@returns(t.void)
@binds(dll)
def color_maski(index, r, g, b, a):
    pass

@accepts(t.enum, t.uint, POINTER(t.boolean))
@returns(t.void)
@binds(dll)
def get_booleani_v(target, index, data):
    pass

@accepts(t.enum, t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_integeri_v(target, index, data):
    pass

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

@accepts(t.enum, t.uint)
@returns(t.boolean)
@binds(dll)
def is_enabledi(target, index):
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def begin_transform_feedback(primitivemode):
    '''
    start transform feedback operation
    
    Args:
        primitivemode: Specify the output type of the primitives that will be recorded into the buffer objects that are bound for transform feedback
    '''

@accepts()
@returns(t.void)
@binds(dll)
def end_transform_feedback():
    pass

@accepts(t.enum, t.uint, t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def bind_buffer_range(target, index, buffer, offset, size):
    '''
    bind a range within a buffer object to an indexed buffer target
    
    Args:
        target: Specify the target of the bind operation
        index: Specify the index of the binding point within the array specified by target
        buffer: The name of a buffer object to bind to the specified binding point
        offset: The starting offset in basic machine units into the buffer object buffer
        size: The amount of data in machine units that can be read from the buffer object while used as an indexed target
    '''

@accepts(t.enum, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def bind_buffer_base(target, index, buffer):
    '''
    bind a buffer object to an indexed buffer target
    
    Args:
        target: Specify the target of the bind operation
        index: Specify the index of the binding point within the array specified by target
        buffer: The name of a buffer object to bind to the specified binding point
    '''

@accepts(t.uint, t.sizei, POINTER(t.char_p), t.enum)
@returns(t.void)
@binds(dll)
def transform_feedback_varyings(program, count, varyings, buffermode):
    '''
    specify values to record in transform feedback buffers
    
    Args:
        program: The name of the target program object
        count: The number of varying variables used for transform feedback
        varyings: An array of count zero-terminated strings specifying the names of the varying variables to use for transform feedback
        buffermode: Identifies the mode used to capture the varying variables when transform feedback is active
    '''

@accepts(t.uint, t.uint, t.sizei, POINTER(t.sizei), POINTER(t.sizei), POINTER(t.enum), t.char_p)
@returns(t.void)
@binds(dll)
def get_transform_feedback_varying(program, index, bufsize, length, size, type, name):
    '''
    retrieve information about varying variables selected for transform feedback
    
    Args:
        program: The name of the target program object
        index: The index of the varying variable whose information to retrieve
        bufsize: The maximum number of characters, including the null terminator, that may be written into name
        length: The address of a variable which will receive the number of characters written into name, excluding the null-terminator
        size: The address of a variable that will receive the size of the varying
        type: The address of a variable that will recieve the type of the varying
        name: The address of a buffer into which will be written the name of the varying
    '''

@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def clamp_color(target, clamp):
    '''
    specify whether data read via glReadPixels should be clamped
    
    Args:
        target: Target for color clamping
        clamp: Specifies whether to apply color clamping
    '''

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def begin_conditional_render(id, mode):
    '''
    start conditional rendering
    
    Args:
        id: Specifies the name of an occlusion query object whose results are used to determine if the rendering commands are discarded
        mode: Specifies how glBeginConditionalRender interprets the results of the occlusion query
    '''

@accepts()
@returns(t.void)
@binds(dll)
def end_conditional_render():
    pass

@accepts(t.uint, t.int, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def vertex_attrib_i_pointer(index, size, type, stride, pointer):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_vertex_attrib_iiv(index, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_vertex_attrib_iuiv(index, pname, params):
    pass

@accepts(t.uint, t.int)
@returns(t.void)
@binds(dll)
def vertex_attrib_i1i(index, x):
    pass

@accepts(t.uint, t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex_attrib_i2i(index, x, y):
    pass

@accepts(t.uint, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex_attrib_i3i(index, x, y, z):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int)
@returns(t.void)
@binds(dll)
def vertex_attrib_i4i(index, x, y, z, w):
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_i1ui(index, x):
    pass

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_i2ui(index, x, y):
    pass

@accepts(t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_i3ui(index, x, y, z):
    pass

@accepts(t.uint, t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_i4ui(index, x, y, z, w):
    pass

@accepts(t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex_attrib_i1iv(index, v):
    pass

@accepts(t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex_attrib_i2iv(index, v):
    pass

@accepts(t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex_attrib_i3iv(index, v):
    pass

@accepts(t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4iv(index, v):
    pass

@accepts(t.uint, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_i1uiv(index, v):
    pass

@accepts(t.uint, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_i2uiv(index, v):
    pass

@accepts(t.uint, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_i3uiv(index, v):
    pass

@accepts(t.uint, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4uiv(index, v):
    pass

@accepts(t.uint, POINTER(t.byte))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4bv(index, v):
    pass

@accepts(t.uint, POINTER(t.short))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4sv(index, v):
    pass

@accepts(t.uint, POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4ubv(index, v):
    pass

@accepts(t.uint, POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def vertex_attrib_i4usv(index, v):
    pass

@accepts(t.uint, t.int, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_uniformuiv(program, location, params):
    pass

@accepts(t.uint, t.uint, t.char_p)
@returns(t.void)
@binds(dll)
def bind_frag_data_location(program, color, name):
    '''
    bind a user-defined varying out variable to a fragment shader color number
    
    Args:
        program: The name of the program containing varying out variable whose binding to modify
        name: The name of the user-defined varying out variable whose binding to modify
    '''

@accepts(t.uint, t.char_p)
@returns(t.int)
@binds(dll)
def get_frag_data_location(program, name):
    '''
    query the bindings of color numbers to user-defined varying out variables
    
    Args:
        program: The name of the program containing varying out variable whose binding to query
        name: The name of the user-defined varying out variable whose binding to query
    '''

@accepts(t.int, t.uint)
@returns(t.void)
@binds(dll)
def uniform1ui(location, v0):
    pass

@accepts(t.int, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def uniform2ui(location, v0, v1):
    pass

@accepts(t.int, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def uniform3ui(location, v0, v1, v2):
    pass

@accepts(t.int, t.uint, t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def uniform4ui(location, v0, v1, v2, v3):
    pass

@accepts(t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def uniform1uiv(location, count, value):
    pass

@accepts(t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def uniform2uiv(location, count, value):
    pass

@accepts(t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def uniform3uiv(location, count, value):
    pass

@accepts(t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def uniform4uiv(location, count, value):
    pass

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

@accepts(t.enum, t.int, POINTER(t.int))
@returns(t.void)
@binds(dll)
def clear_bufferiv(buffer, drawbuffer, value):
    pass

@accepts(t.enum, t.int, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def clear_bufferuiv(buffer, drawbuffer, value):
    pass

@accepts(t.enum, t.int, POINTER(t.float))
@returns(t.void)
@binds(dll)
def clear_bufferfv(buffer, drawbuffer, value):
    pass

@accepts(t.enum, t.int, t.float, t.int)
@returns(t.void)
@binds(dll)
def clear_bufferfi(buffer, drawbuffer, depth, stencil):
    pass

@accepts(t.enum, t.uint)
@returns(POINTER(t.ubyte))
@binds(dll)
def get_stringi(name, index):
    pass

COMPARE_REF_TO_TEXTURE = 0x884E
CLIP_DISTANCE0 = 0x3000
CLIP_DISTANCE1 = 0x3001
CLIP_DISTANCE2 = 0x3002
CLIP_DISTANCE3 = 0x3003
CLIP_DISTANCE4 = 0x3004
CLIP_DISTANCE5 = 0x3005
CLIP_DISTANCE6 = 0x3006
CLIP_DISTANCE7 = 0x3007
MAX_CLIP_DISTANCES = 0x0D32
MAJOR_VERSION = 0x821B
MINOR_VERSION = 0x821C
NUM_EXTENSIONS = 0x821D
CONTEXT_FLAGS = 0x821E
COMPRESSED_RED = 0x8225
COMPRESSED_RG = 0x8226
CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 0x00000001
RGBA32F = 0x8814
RGB32F = 0x8815
RGBA16F = 0x881A
RGB16F = 0x881B
VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
MIN_PROGRAM_TEXEL_OFFSET = 0x8904
MAX_PROGRAM_TEXEL_OFFSET = 0x8905
CLAMP_READ_COLOR = 0x891C
FIXED_ONLY = 0x891D
MAX_VARYING_COMPONENTS = 0x8B4B
TEXTURE_1D_ARRAY = 0x8C18
PROXY_TEXTURE_1D_ARRAY = 0x8C19
TEXTURE_2D_ARRAY = 0x8C1A
PROXY_TEXTURE_2D_ARRAY = 0x8C1B
TEXTURE_BINDING_1D_ARRAY = 0x8C1C
TEXTURE_BINDING_2D_ARRAY = 0x8C1D
R11F_G11F_B10F = 0x8C3A
UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
RGB9_E5 = 0x8C3D
UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
TEXTURE_SHARED_SIZE = 0x8C3F
TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
PRIMITIVES_GENERATED = 0x8C87
TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
RASTERIZER_DISCARD = 0x8C89
MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
INTERLEAVED_ATTRIBS = 0x8C8C
SEPARATE_ATTRIBS = 0x8C8D
TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
RGBA32UI = 0x8D70
RGB32UI = 0x8D71
RGBA16UI = 0x8D76
RGB16UI = 0x8D77
RGBA8UI = 0x8D7C
RGB8UI = 0x8D7D
RGBA32I = 0x8D82
RGB32I = 0x8D83
RGBA16I = 0x8D88
RGB16I = 0x8D89
RGBA8I = 0x8D8E
RGB8I = 0x8D8F
RED_INTEGER = 0x8D94
GREEN_INTEGER = 0x8D95
BLUE_INTEGER = 0x8D96
RGB_INTEGER = 0x8D98
RGBA_INTEGER = 0x8D99
BGR_INTEGER = 0x8D9A
BGRA_INTEGER = 0x8D9B
SAMPLER_1D_ARRAY = 0x8DC0
SAMPLER_2D_ARRAY = 0x8DC1
SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
SAMPLER_CUBE_SHADOW = 0x8DC5
UNSIGNED_INT_VEC2 = 0x8DC6
UNSIGNED_INT_VEC3 = 0x8DC7
UNSIGNED_INT_VEC4 = 0x8DC8
INT_SAMPLER_1D = 0x8DC9
INT_SAMPLER_2D = 0x8DCA
INT_SAMPLER_3D = 0x8DCB
INT_SAMPLER_CUBE = 0x8DCC
INT_SAMPLER_1D_ARRAY = 0x8DCE
INT_SAMPLER_2D_ARRAY = 0x8DCF
UNSIGNED_INT_SAMPLER_1D = 0x8DD1
UNSIGNED_INT_SAMPLER_2D = 0x8DD2
UNSIGNED_INT_SAMPLER_3D = 0x8DD3
UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
QUERY_WAIT = 0x8E13
QUERY_NO_WAIT = 0x8E14
QUERY_BY_REGION_WAIT = 0x8E15
QUERY_BY_REGION_NO_WAIT = 0x8E16
BUFFER_ACCESS_FLAGS = 0x911F
BUFFER_MAP_LENGTH = 0x9120
BUFFER_MAP_OFFSET = 0x9121
DEPTH_COMPONENT32F = 0x8CAC
DEPTH32F_STENCIL8 = 0x8CAD
FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_renderbuffer(renderbuffer):
    '''
    determine if a name corresponds to a renderbuffer object
    
    Args:
        renderbuffer: Specifies a value that may be the name of a renderbuffer object
    '''

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def bind_renderbuffer(target, renderbuffer):
    '''
    bind a renderbuffer to a renderbuffer target
    
    Args:
        target: Specifies the renderbuffer target of the binding operation
        renderbuffer: Specifies the name of the renderbuffer object to bind
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_renderbuffers(n, renderbuffers):
    '''
    delete renderbuffer objects
    
    Args:
        n: Specifies the number of renderbuffer objects to be deleted
        renderbuffers: A pointer to an array containing n renderbuffer objects to be deleted
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_renderbuffers(n, renderbuffers):
    '''
    generate renderbuffer object names
    
    Args:
        n: Specifies the number of renderbuffer object names to generate
        renderbuffers: Specifies an array in which the generated renderbuffer object names are stored
    '''

@accepts(t.enum, t.enum, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def renderbuffer_storage(target, internalformat, width, height):
    '''
    establish data storage, format and dimensions of a renderbuffer object's image
    
    Args:
        target: Specifies a binding target of the allocation for glRenderbufferStorage function
        internalformat: Specifies the internal format to use for the renderbuffer object's image
        width: Specifies the width of the renderbuffer, in pixels
        height: Specifies the height of the renderbuffer, in pixels
    '''

@accepts(t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_renderbuffer_parameteriv(target, pname, params):
    pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_framebuffer(framebuffer):
    '''
    determine if a name corresponds to a framebuffer object
    
    Args:
        framebuffer: Specifies a value that may be the name of a framebuffer object
    '''

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def bind_framebuffer(target, framebuffer):
    '''
    bind a framebuffer to a framebuffer target
    
    Args:
        target: Specifies the framebuffer target of the binding operation
        framebuffer: Specifies the name of the framebuffer object to bind
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_framebuffers(n, framebuffers):
    '''
    delete framebuffer objects
    
    Args:
        n: Specifies the number of framebuffer objects to be deleted
        framebuffers: A pointer to an array containing n framebuffer objects to be deleted
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_framebuffers(n, framebuffers):
    '''
    generate framebuffer object names
    
    Args:
        n: Specifies the number of framebuffer object names to generate
    '''

@accepts(t.enum)
@returns(t.enum)
@binds(dll)
def check_framebuffer_status(target):
    '''
    check the completeness status of a framebuffer
    
    Args:
        target: Specify the target to which the framebuffer is bound for glCheckFramebufferStatus, and the target against which framebuffer completeness of framebuffer is checked for glCheckNamedFramebufferStatus
    '''

@accepts(t.enum, t.enum, t.enum, t.uint, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_texture1_d(target, attachment, textarget, texture, level):
    pass

@accepts(t.enum, t.enum, t.enum, t.uint, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_texture2_d(target, attachment, textarget, texture, level):
    pass

@accepts(t.enum, t.enum, t.enum, t.uint, t.int, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_texture3_d(target, attachment, textarget, texture, level, zoffset):
    pass

@accepts(t.enum, t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def framebuffer_renderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    '''
    attach a renderbuffer as a logical buffer of a framebuffer object
    
    Args:
        target: Specifies the target to which the framebuffer is bound for glFramebufferRenderbuffer
        attachment: Specifies the attachment point of the framebuffer
        renderbuffertarget: Specifies the renderbuffer target
        renderbuffer: Specifies the name of an existing renderbuffer object of type renderbuffertarget to attach
    '''

@accepts(t.enum, t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_framebuffer_attachment_parameteriv(target, attachment, pname, params):
    pass

@accepts(t.enum)
@returns(t.void)
@binds(dll)
def generate_mipmap(target):
    '''
    generate mipmaps for a specified texture object
    
    Args:
        target: Specifies the target to which the texture object is bound for glGenerateMipmap
    '''

@accepts(t.int, t.int, t.int, t.int, t.int, t.int, t.int, t.int, t.bitfield, t.enum)
@returns(t.void)
@binds(dll)
def blit_framebuffer(srcx0, srcy0, srcx1, srcy1, dstx0, dsty0, dstx1, dsty1, mask, filter):
    '''
    copy a block of pixels from one framebuffer object to another
    
    Args:
        srcx0, srcy0, srcx1, srcy1: Specify the bounds of the source rectangle within the read buffer of the read framebuffer
        dstx0, dsty0, dstx1, dsty1: Specify the bounds of the destination rectangle within the write buffer of the write framebuffer
        mask: The bitwise OR of the flags indicating which buffers are to be copied
        filter: Specifies the interpolation to be applied if the image is stretched
    '''

@accepts(t.enum, t.sizei, t.enum, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def renderbuffer_storage_multisample(target, samples, internalformat, width, height):
    '''
    establish data storage, format, dimensions and sample count of a renderbuffer object's image
    
    Args:
        target: Specifies a binding target of the allocation for glRenderbufferStorageMultisample function
        samples: Specifies the number of samples to be used for the renderbuffer object's storage
        internalformat: Specifies the internal format to use for the renderbuffer object's image
        width: Specifies the width of the renderbuffer, in pixels
        height: Specifies the height of the renderbuffer, in pixels
    '''

@accepts(t.enum, t.enum, t.uint, t.int, t.int)
@returns(t.void)
@binds(dll)
def framebuffer_texture_layer(target, attachment, texture, level, layer):
    '''
    attach a single layer of a texture object as a logical buffer of a framebuffer object
    
    Args:
        target: Specifies the target to which the framebuffer is bound for glFramebufferTextureLayer
        attachment: Specifies the attachment point of the framebuffer
        texture: Specifies the name of an existing texture object to attach
        level: Specifies the mipmap level of the texture object to attach
        layer: Specifies the layer of the texture object to attach
    '''

INVALID_FRAMEBUFFER_OPERATION = 0x0506
FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
FRAMEBUFFER_DEFAULT = 0x8218
FRAMEBUFFER_UNDEFINED = 0x8219
DEPTH_STENCIL_ATTACHMENT = 0x821A
MAX_RENDERBUFFER_SIZE = 0x84E8
DEPTH_STENCIL = 0x84F9
UNSIGNED_INT_24_8 = 0x84FA
DEPTH24_STENCIL8 = 0x88F0
TEXTURE_STENCIL_SIZE = 0x88F1
TEXTURE_RED_TYPE = 0x8C10
TEXTURE_GREEN_TYPE = 0x8C11
TEXTURE_BLUE_TYPE = 0x8C12
TEXTURE_ALPHA_TYPE = 0x8C13
TEXTURE_DEPTH_TYPE = 0x8C16
UNSIGNED_NORMALIZED = 0x8C17
FRAMEBUFFER_BINDING = 0x8CA6
DRAW_FRAMEBUFFER_BINDING = 0x8CA6
RENDERBUFFER_BINDING = 0x8CA7
READ_FRAMEBUFFER = 0x8CA8
DRAW_FRAMEBUFFER = 0x8CA9
READ_FRAMEBUFFER_BINDING = 0x8CAA
RENDERBUFFER_SAMPLES = 0x8CAB
FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
FRAMEBUFFER_COMPLETE = 0x8CD5
FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
FRAMEBUFFER_UNSUPPORTED = 0x8CDD
MAX_COLOR_ATTACHMENTS = 0x8CDF
COLOR_ATTACHMENT0 = 0x8CE0
COLOR_ATTACHMENT1 = 0x8CE1
COLOR_ATTACHMENT2 = 0x8CE2
COLOR_ATTACHMENT3 = 0x8CE3
COLOR_ATTACHMENT4 = 0x8CE4
COLOR_ATTACHMENT5 = 0x8CE5
COLOR_ATTACHMENT6 = 0x8CE6
COLOR_ATTACHMENT7 = 0x8CE7
COLOR_ATTACHMENT8 = 0x8CE8
COLOR_ATTACHMENT9 = 0x8CE9
COLOR_ATTACHMENT10 = 0x8CEA
COLOR_ATTACHMENT11 = 0x8CEB
COLOR_ATTACHMENT12 = 0x8CEC
COLOR_ATTACHMENT13 = 0x8CED
COLOR_ATTACHMENT14 = 0x8CEE
COLOR_ATTACHMENT15 = 0x8CEF
COLOR_ATTACHMENT16 = 0x8CF0
COLOR_ATTACHMENT17 = 0x8CF1
COLOR_ATTACHMENT18 = 0x8CF2
COLOR_ATTACHMENT19 = 0x8CF3
COLOR_ATTACHMENT20 = 0x8CF4
COLOR_ATTACHMENT21 = 0x8CF5
COLOR_ATTACHMENT22 = 0x8CF6
COLOR_ATTACHMENT23 = 0x8CF7
COLOR_ATTACHMENT24 = 0x8CF8
COLOR_ATTACHMENT25 = 0x8CF9
COLOR_ATTACHMENT26 = 0x8CFA
COLOR_ATTACHMENT27 = 0x8CFB
COLOR_ATTACHMENT28 = 0x8CFC
COLOR_ATTACHMENT29 = 0x8CFD
COLOR_ATTACHMENT30 = 0x8CFE
COLOR_ATTACHMENT31 = 0x8CFF
DEPTH_ATTACHMENT = 0x8D00
STENCIL_ATTACHMENT = 0x8D20
FRAMEBUFFER = 0x8D40
RENDERBUFFER = 0x8D41
RENDERBUFFER_WIDTH = 0x8D42
RENDERBUFFER_HEIGHT = 0x8D43
RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
STENCIL_INDEX1 = 0x8D46
STENCIL_INDEX4 = 0x8D47
STENCIL_INDEX8 = 0x8D48
STENCIL_INDEX16 = 0x8D49
RENDERBUFFER_RED_SIZE = 0x8D50
RENDERBUFFER_GREEN_SIZE = 0x8D51
RENDERBUFFER_BLUE_SIZE = 0x8D52
RENDERBUFFER_ALPHA_SIZE = 0x8D53
RENDERBUFFER_DEPTH_SIZE = 0x8D54
RENDERBUFFER_STENCIL_SIZE = 0x8D55
FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
MAX_SAMPLES = 0x8D57
INDEX = 0x8222
TEXTURE_LUMINANCE_TYPE = 0x8C14
TEXTURE_INTENSITY_TYPE = 0x8C15
FRAMEBUFFER_SRGB = 0x8DB9
HALF_FLOAT = 0x140B
@accepts(t.enum, t.intptr, t.sizeiptr, t.bitfield)
@returns(t.void)
@binds(dll)
def map_buffer_range(target, offset, length, access):
    '''
    map all or part of a buffer object's data store into the client's address space
    
    Args:
        target: Specifies the target to which the buffer object is bound for glMapBufferRange, which must be one of the buffer binding targets in the following table:
        offset: Specifies the starting offset within the buffer of the range to be mapped
        length: Specifies the length of the range to be mapped
        access: Specifies a combination of access flags indicating the desired access to the mapped range
    '''

@accepts(t.enum, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def flush_mapped_buffer_range(target, offset, length):
    '''
    indicate modifications to a range of a mapped buffer
    
    Args:
        target: Specifies the target to which the buffer object is bound for glFlushMappedBufferRange, which must be one of the buffer binding targets in the following table:
        offset: Specifies the start of the buffer subrange, in basic machine units
        length: Specifies the length of the buffer subrange, in basic machine units
    '''

MAP_READ_BIT = 0x0001
MAP_WRITE_BIT = 0x0002
MAP_INVALIDATE_RANGE_BIT = 0x0004
MAP_INVALIDATE_BUFFER_BIT = 0x0008
MAP_FLUSH_EXPLICIT_BIT = 0x0010
MAP_UNSYNCHRONIZED_BIT = 0x0020
COMPRESSED_RED_RGTC1 = 0x8DBB
COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
COMPRESSED_RG_RGTC2 = 0x8DBD
COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
RG = 0x8227
RG_INTEGER = 0x8228
R8 = 0x8229
R16 = 0x822A
RG8 = 0x822B
RG16 = 0x822C
R16F = 0x822D
R32F = 0x822E
RG16F = 0x822F
RG32F = 0x8230
R8I = 0x8231
R8UI = 0x8232
R16I = 0x8233
R16UI = 0x8234
R32I = 0x8235
R32UI = 0x8236
RG8I = 0x8237
RG8UI = 0x8238
RG16I = 0x8239
RG16UI = 0x823A
RG32I = 0x823B
RG32UI = 0x823C
@accepts(t.uint)
@returns(t.void)
@binds(dll)
def bind_vertex_array(array):
    '''
    bind a vertex array object
    
    Args:
        array: Specifies the name of the vertex array to bind
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_vertex_arrays(n, arrays):
    '''
    delete vertex array objects
    
    Args:
        n: Specifies the number of vertex array objects to be deleted
        arrays: Specifies the address of an array containing the n names of the objects to be deleted
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_vertex_arrays(n, arrays):
    '''
    generate vertex array object names
    
    Args:
        n: Specifies the number of vertex array object names to generate
        arrays: Specifies an array in which the generated vertex array object names are stored
    '''

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_vertex_array(array):
    '''
    determine if a name corresponds to a vertex array object
    
    Args:
        array: Specifies a value that may be the name of a vertex array object
    '''

VERTEX_ARRAY_BINDING = 0x85B5
CLAMP_VERTEX_COLOR = 0x891A
CLAMP_FRAGMENT_COLOR = 0x891B
ALPHA_INTEGER = 0x8D97