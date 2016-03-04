#BEWARE: automatically generated code
#This code was generated by opengl/gl/generate/__main__.py

from opengl.gl.raw.bindings import *

MAX_VERTEX_ATTRIB_STRIDE = 0x82E5
PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 0x8221
TEXTURE_BUFFER_BINDING = 0x8C2A
@accepts(t.enum, t.sizeiptr, t.void, t.bitfield)
@returns(t.void)
@binds(dll)
def buffer_storage(target, size, data, flags):
    '''
    creates and initializes a buffer object's immutable data store
    
    Args:
        target: Specifies the target to which the buffer object is bound for glBufferStorage, which must be one of the buffer binding targets in the following table:
        size: Specifies the size in bytes of the buffer object's new data store
        data: Specifies a pointer to data that will be copied into the data store for initialization, or NULL if no data is to be copied
        flags: Specifies the intended usage of the buffer's data store
    '''

MAP_READ_BIT = 0x0001
MAP_WRITE_BIT = 0x0002
MAP_PERSISTENT_BIT = 0x0040
MAP_COHERENT_BIT = 0x0080
DYNAMIC_STORAGE_BIT = 0x0100
CLIENT_STORAGE_BIT = 0x0200
CLIENT_MAPPED_BUFFER_BARRIER_BIT = 0x00004000
BUFFER_IMMUTABLE_STORAGE = 0x821F
BUFFER_STORAGE_FLAGS = 0x8220
@accepts(t.uint, t.int, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def clear_tex_image(texture, level, format, type, data):
    '''
    fills all a texture image with a constant value
    
    Args:
        texture: The name of an existing texture object containing the image to be cleared
        level: The level of texture containing the region to be cleared
        format: The format of the data whose address in memory is given by data
        type: The type of the data whose address in memory is given by data
        data: The address in memory of the data to be used to clear the specified region
    '''

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def clear_tex_sub_image(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
    '''
    fills all or part of a texture image with a constant value
    
    Args:
        texture: The name of an existing texture object containing the image to be cleared
        level: The level of texture containing the region to be cleared
        xoffset: The coordinate of the left edge of the region to be cleared
        yoffset: The coordinate of the lower edge of the region to be cleared
        zoffset: The coordinate of the front of the region to be cleared
        width: The width of the region to be cleared
        height: The height of the region to be cleared
        depth: The depth of the region to be cleared
        format: The format of the data whose address in memory is given by data
        type: The type of the data whose address in memory is given by data
        data: The address in memory of the data to be used to clear the specified region
    '''

CLEAR_TEXTURE = 0x9365
LOCATION_COMPONENT = 0x934A
TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
TRANSFORM_FEEDBACK_BUFFER_INDEX = 0x934B
TRANSFORM_FEEDBACK_BUFFER_STRIDE = 0x934C
@accepts(t.enum, t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_buffers_base(target, first, count, buffers):
    '''
    bind one or more buffer objects to a sequence of indexed buffer targets
    
    Args:
        target: Specify the target of the bind operation
        count: Specify the number of contiguous binding points to which to bind buffers
        buffers: A pointer to an array of names of buffer objects to bind to the targets on the specified binding point, or NULL
    '''

@accepts(t.enum, t.uint, t.sizei, POINTER(t.uint), POINTER(t.intptr), POINTER(t.sizeiptr))
@returns(t.void)
@binds(dll)
def bind_buffers_range(target, first, count, buffers, offsets, sizes):
    '''
    bind ranges of one or more buffer objects to a sequence of indexed buffer targets
    
    Args:
        target: Specify the target of the bind operation
        count: Specify the number of contiguous binding points to which to bind buffers
        buffers: A pointer to an array of names of buffer objects to bind to the targets on the specified binding point, or NULL
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_textures(first, count, textures):
    '''
    bind one or more named textures to a sequence of consecutive texture units
    
    Args:
        first: Specifies the first texture unit to which a texture is to be bound
        count: Specifies the number of textures to bind
        textures: Specifies the address of an array of names of existing texture objects
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_samplers(first, count, samplers):
    '''
    bind one or more named sampler objects to a sequence of consecutive sampler units
    
    Args:
        first: Specifies the first sampler unit to which a sampler object is to be bound
        count: Specifies the number of samplers to bind
        samplers: Specifies the address of an array of names of existing sampler objects
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_image_textures(first, count, textures):
    '''
    bind one or more named texture images to a sequence of consecutive image units
    
    Args:
        first: Specifies the first image unit to which a texture is to be bound
        count: Specifies the number of textures to bind
        textures: Specifies the address of an array of names of existing texture objects
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint), POINTER(t.intptr), POINTER(t.sizei))
@returns(t.void)
@binds(dll)
def bind_vertex_buffers(first, count, buffers, offsets, strides):
    '''
    attach multiple buffer objects to a vertex array object
    
    Args:
        first: Specifies the first vertex buffer binding point to which a buffer object is to be bound
        count: Specifies the number of buffers to bind
        buffers: Specifies the address of an array of names of existing buffer objects
        offsets: Specifies the address of an array of offsets to associate with the binding points
        buffers: Specifies the address of an array of strides to associate with the binding points
    '''

QUERY_BUFFER = 0x9192
QUERY_BUFFER_BARRIER_BIT = 0x00008000
QUERY_BUFFER_BINDING = 0x9193
QUERY_RESULT_NO_WAIT = 0x9194
MIRROR_CLAMP_TO_EDGE = 0x8743
STENCIL_INDEX = 0x1901
STENCIL_INDEX8 = 0x8D48
UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B