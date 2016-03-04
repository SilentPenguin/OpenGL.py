#BEWARE: automatically generated code
#This code was generated by /generate/__main__.py

from opengl.gl.raw.bindings import *

MAX_VERTEX_ATTRIB_STRIDE = 0x82E5
PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 0x8221
TEXTURE_BUFFER_BINDING = 0x8C2A
@accepts(t.enum, t.sizeiptr, t.void, t.bitfield)
@returns(t.void)
@binds(dll)
def buffer_storage(target, size, data, flags):
    '''
    creates and initializes a buffer object's immutable data store.
    
    gl.buffer_storage and gl.named_buffer_storage create a new immutable data
    store. For gl.buffer_storage, the buffer object currently bound to target
    will be initialized. For gl.named_buffer_storage, buffer is the name of the
    buffer object that will be configured. The size of the data store is
    specified by size.
    
    Args:
        target: the target to which the buffer object is bound for
            glbufferstorage, which must be one of the buffer binding targets in
            the following table:.
        size: the size in bytes of the buffer object's new data store.
        data: a pointer to data that will be copied into the data store for
            initialization, or null if no data is to be copied.
        flags: the intended usage of the buffer's data store.
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
    fills all a texture image with a constant value.
    
    gl.clear_tex_image fills all an image contained in a texture with an
    application supplied value. texture must be the name of an existing texture.
    Further, texture may not be the name of a buffer texture, nor may its
    internal format be compressed.
    
    Args:
        texture: the name of an existing texture object containing the image to
            be cleared.
        level: the level of texture containing the region to be cleared.
        format: the format of the data whose address in memory is given by data.
        type: the type of the data whose address in memory is given by data.
        data: the address in memory of the data to be used to clear the
            specified region.
    '''

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def clear_tex_sub_image(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
    '''
    fills all or part of a texture image with a constant value.
    
    gl.clear_tex_sub_image fills all or part of an image contained in a texture
    with an application supplied value. texture must be the name of an existing
    texture. Further, texture may not be the name of a buffer texture, nor may
    its internal format be compressed.
    
    Args:
        texture: the name of an existing texture object containing the image to
            be cleared.
        level: the level of texture containing the region to be cleared.
        xoffset: the coordinate of the left edge of the region to be cleared.
        yoffset: the coordinate of the lower edge of the region to be cleared.
        zoffset: the coordinate of the front of the region to be cleared.
        width: the width of the region to be cleared.
        height: the height of the region to be cleared.
        depth: the depth of the region to be cleared.
        format: the format of the data whose address in memory is given by data.
        type: the type of the data whose address in memory is given by data.
        data: the address in memory of the data to be used to clear the
            specified region.
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
    bind one or more buffer objects to a sequence of indexed buffer targets.
    
    gl.bind_buffers_base binds a set of count buffer objects whose names are
    given in the array buffers to the count consecutive binding points starting
    from index index of the array of targets specified by target. If buffers is
    None then gl.bind_buffers_base unbinds any buffers that are currently bound
    to the referenced binding points. Assuming no errors are generated, it is
    equivalent to the following pseudo-code, which calls gl.
    
    Args:
        target: the target of the bind operation.
        count: the number of contiguous binding points to which to bind buffers.
        buffers: a pointer to an array of names of buffer objects to bind to the
            targets on the specified binding point, or null.
    '''

@accepts(t.enum, t.uint, t.sizei, POINTER(t.uint), POINTER(t.intptr), POINTER(t.sizeiptr))
@returns(t.void)
@binds(dll)
def bind_buffers_range(target, first, count, buffers, offsets, sizes):
    '''
    bind ranges of one or more buffer objects to a sequence of indexed buffer
targets.
    
    gl.bind_buffers_range binds a set of count ranges from buffer objects whose
    names are given in the array buffers to the count consecutive binding points
    starting from index index of the array of targets specified by target.
    offsets specifies the address of an array containing count starting offsets
    within the buffers, and sizes specifies the adderess of an array of count
    sizes of the ranges. If buffers is None then offsets and sizes are ignored
    and gl.bind_buffers_range unbinds any buffers that are currently bound to
    the referenced binding points. Assuming no errors are generated, it is
    equivalent to the following pseudo-code, which calls gl.
    
    Args:
        target: the target of the bind operation.
        count: the number of contiguous binding points to which to bind buffers.
        buffers: a pointer to an array of names of buffer objects to bind to the
            targets on the specified binding point, or null.
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_textures(first, count, textures):
    '''
    bind one or more named textures to a sequence of consecutive texture units.
    
    gl.bind_textures binds an array of existing texture objects to a specified
    number of consecutive texture units. count specifies the number of texture
    objects whose names are stored in the array textures. That number of texture
    names are read from the array and bound to the count consecutive texture
    units starting from first. The target, or type of texture is deduced from
    the texture object and each texture is bound to the corresponding target of
    the texture unit.
    
    Args:
        first: the first texture unit to which a texture is to be bound.
        count: the number of textures to bind.
        textures: the address of an array of names of existing texture objects.
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_samplers(first, count, samplers):
    '''
    bind one or more named sampler objects to a sequence of consecutive sampler
units.
    
    gl.bind_samplers binds samplers from an array of existing sampler objects to
    a specified number of consecutive sampler units. count specifies the number
    of sampler objects whose names are stored in the array samplers. That number
    of sampler names is read from the array and bound to the count consecutive
    sampler units starting from first.
    
    Args:
        first: the first sampler unit to which a sampler object is to be bound.
        count: the number of samplers to bind.
        samplers: the address of an array of names of existing sampler objects.
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def bind_image_textures(first, count, textures):
    '''
    bind one or more named texture images to a sequence of consecutive image units.
    
    gl.bind_image_textures binds images from an array of existing texture
    objects to a specified number of consecutive image units. count specifies
    the number of texture objects whose names are stored in the array textures.
    That number of texture names are read from the array and bound to the count
    consecutive texture units starting from first. If the name zero appears in
    the textures array, any existing binding to the image unit is reset.
    
    Args:
        first: the first image unit to which a texture is to be bound.
        count: the number of textures to bind.
        textures: the address of an array of names of existing texture objects.
    '''

@accepts(t.uint, t.sizei, POINTER(t.uint), POINTER(t.intptr), POINTER(t.sizei))
@returns(t.void)
@binds(dll)
def bind_vertex_buffers(first, count, buffers, offsets, strides):
    '''
    attach multiple buffer objects to a vertex array object.
    
    gl.bind_vertex_buffers and gl.vertex_array_vertex_buffers bind storage from
    an array of existing buffer objects to a specified number of consecutive
    vertex buffer binding points units in a vertex array object. For
    gl.bind_vertex_buffers, the vertex array object is the currently bound
    vertex array object. For gl.vertex_array_vertex_buffers, vaobj is the name
    of the vertex array object.
    
    Args:
        first: the first vertex buffer binding point to which a buffer object is
            to be bound.
        count: the number of buffers to bind.
        buffers: the address of an array of strides to associate with the
            binding points.
        offsets: the address of an array of offsets to associate with the
            binding points.
    '''

QUERY_BUFFER = 0x9192
QUERY_BUFFER_BARRIER_BIT = 0x00008000
QUERY_BUFFER_BINDING = 0x9193
QUERY_RESULT_NO_WAIT = 0x9194
MIRROR_CLAMP_TO_EDGE = 0x8743
STENCIL_INDEX = 0x1901
STENCIL_INDEX8 = 0x8D48
UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B