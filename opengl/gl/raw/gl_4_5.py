#BEWARE: automatically generated code
#This code was generated by /generate/__main__.py

from opengl.gl.raw.bindings import *

CONTEXT_LOST = 0x0507
@accepts(t.enum, t.enum)
@returns(t.void)
@binds(dll)
def clip_control(origin, depth):
    '''
    control clip coordinate to window coordinate behavior.
    
    gl.clip_control controls the clipping volume behavior and the clip
    coordinate to window coordinate transformation behavior.
    
    Args:
        origin: the clip control origin.
        depth: the clip control depth mode.
    '''

LOWER_LEFT = 0x8CA1
UPPER_LEFT = 0x8CA2
NEGATIVE_ONE_TO_ONE = 0x935E
ZERO_TO_ONE = 0x935F
CLIP_ORIGIN = 0x935C
CLIP_DEPTH_MODE = 0x935D
QUERY_WAIT_INVERTED = 0x8E17
QUERY_NO_WAIT_INVERTED = 0x8E18
QUERY_BY_REGION_WAIT_INVERTED = 0x8E19
QUERY_BY_REGION_NO_WAIT_INVERTED = 0x8E1A
MAX_CULL_DISTANCES = 0x82F9
MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 0x82FA
@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_transform_feedbacks(n, ids):
    '''
    create transform feedback objects.
    
    gl.create_transform_feedbacks returns n previously unused transform feedback
    object names in ids, each representing a new transform feedback object
    initialized to the default state.
    
    Args:
        n: number of transform feedback objects to create.
        ids: an array in which names of the new transform feedback objects are
            stored.
    '''

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def transform_feedback_buffer_base(xfb, index, buffer):
    '''
    bind a buffer object to a transform feedback buffer object.
    
    gl.transform_feedback_buffer_base binds the buffer object buffer to the
    binding point at index index of the transform feedback object xfb.
    
    Args:
        xfb: name of the transform feedback buffer object.
        index: index of the binding point within xfb.
        buffer: name of the buffer object to bind to the specified binding
            point.
    '''

@accepts(t.uint, t.uint, t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def transform_feedback_buffer_range(xfb, index, buffer, offset, size):
    '''
    bind a range within a buffer object to a transform feedback buffer object.
    
    gl.transform_feedback_buffer_range binds a range of the buffer object buffer
    represented by offset and size to the binding point at index index of the
    transform feedback object xfb.
    
    Args:
        xfb: name of the transform feedback buffer object.
        index: index of the binding point within xfb.
        buffer: name of the buffer object to bind to the specified binding
            point.
        offset: the starting offset in basic machine units into the buffer
            object.
        size: the amount of data in basic machine units that can be read from or
            written to the buffer object while used as an indexed target.
    '''

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_transform_feedbackiv(xfb, pname, param):
    pass

@accepts(t.uint, t.enum, t.uint, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_transform_feedbacki_v(xfb, pname, index, param):
    pass

@accepts(t.uint, t.enum, t.uint, POINTER(t.int64))
@returns(t.void)
@binds(dll)
def get_transform_feedbacki64_v(xfb, pname, index, param):
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_buffers(n, buffers):
    '''
    create buffer objects.
    
    gl.create_buffers returns n previously unused buffer names in buffers, each
    representing a new buffer object initialized as if it had been bound to an
    unspecified target.
    
    Args:
        n: the number of buffer objects to create.
        buffers: an array in which names of the new buffer objects are stored.
    '''

@accepts(t.uint, t.sizeiptr, t.void, t.bitfield)
@returns(t.void)
@binds(dll)
def named_buffer_storage(buffer, size, data, flags):
    pass

@accepts(t.uint, t.sizeiptr, t.void, t.enum)
@returns(t.void)
@binds(dll)
def named_buffer_data(buffer, size, data, usage):
    pass

@accepts(t.uint, t.intptr, t.sizeiptr, t.void)
@returns(t.void)
@binds(dll)
def named_buffer_sub_data(buffer, offset, size, data):
    pass

@accepts(t.uint, t.uint, t.intptr, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def copy_named_buffer_sub_data(readbuffer, writebuffer, readoffset, writeoffset, size):
    pass

@accepts(t.uint, t.enum, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def clear_named_buffer_data(buffer, internalformat, format, type, data):
    pass

@accepts(t.uint, t.enum, t.intptr, t.sizeiptr, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def clear_named_buffer_sub_data(buffer, internalformat, offset, size, format, type, data):
    pass

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def map_named_buffer(buffer, access):
    pass

@accepts(t.uint, t.intptr, t.sizeiptr, t.bitfield)
@returns(t.void)
@binds(dll)
def map_named_buffer_range(buffer, offset, length, access):
    pass

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def unmap_named_buffer(buffer):
    pass

@accepts(t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def flush_mapped_named_buffer_range(buffer, offset, length):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_named_buffer_parameteriv(buffer, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int64))
@returns(t.void)
@binds(dll)
def get_named_buffer_parameteri64v(buffer, pname, params):
    pass

@accepts(t.uint, t.enum, t.void)
@returns(t.void)
@binds(dll)
def get_named_buffer_pointerv(buffer, pname, params):
    pass

@accepts(t.uint, t.intptr, t.sizeiptr, t.void)
@returns(t.void)
@binds(dll)
def get_named_buffer_sub_data(buffer, offset, size, data):
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_framebuffers(n, framebuffers):
    '''
    create framebuffer objects.
    
    gl.create_framebuffers returns n previously unused framebuffer names in
    framebuffers, each representing a new framebuffer object initialized to the
    default state.
    
    Args:
        n: number of framebuffer objects to create.
    '''

@accepts(t.uint, t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def named_framebuffer_renderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer):
    pass

@accepts(t.uint, t.enum, t.int)
@returns(t.void)
@binds(dll)
def named_framebuffer_parameteri(framebuffer, pname, param):
    pass

@accepts(t.uint, t.enum, t.uint, t.int)
@returns(t.void)
@binds(dll)
def named_framebuffer_texture(framebuffer, attachment, texture, level):
    pass

@accepts(t.uint, t.enum, t.uint, t.int, t.int)
@returns(t.void)
@binds(dll)
def named_framebuffer_texture_layer(framebuffer, attachment, texture, level, layer):
    pass

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def named_framebuffer_draw_buffer(framebuffer, buf):
    pass

@accepts(t.uint, t.sizei, POINTER(t.enum))
@returns(t.void)
@binds(dll)
def named_framebuffer_draw_buffers(framebuffer, n, bufs):
    pass

@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def named_framebuffer_read_buffer(framebuffer, src):
    pass

@accepts(t.uint, t.sizei, POINTER(t.enum))
@returns(t.void)
@binds(dll)
def invalidate_named_framebuffer_data(framebuffer, numattachments, attachments):
    pass

@accepts(t.uint, t.sizei, POINTER(t.enum), t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def invalidate_named_framebuffer_sub_data(framebuffer, numattachments, attachments, x, y, width, height):
    pass

@accepts(t.uint, t.enum, t.int, POINTER(t.int))
@returns(t.void)
@binds(dll)
def clear_named_framebufferiv(framebuffer, buffer, drawbuffer, value):
    pass

@accepts(t.uint, t.enum, t.int, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def clear_named_framebufferuiv(framebuffer, buffer, drawbuffer, value):
    pass

@accepts(t.uint, t.enum, t.int, POINTER(t.float))
@returns(t.void)
@binds(dll)
def clear_named_framebufferfv(framebuffer, buffer, drawbuffer, value):
    pass

@accepts(t.uint, t.enum, t.int, t.float, t.int)
@returns(t.void)
@binds(dll)
def clear_named_framebufferfi(framebuffer, buffer, drawbuffer, depth, stencil):
    pass

@accepts(t.uint, t.uint, t.int, t.int, t.int, t.int, t.int, t.int, t.int, t.int, t.bitfield, t.enum)
@returns(t.void)
@binds(dll)
def blit_named_framebuffer(readframebuffer, drawframebuffer, srcx0, srcy0, srcx1, srcy1, dstx0, dsty0, dstx1, dsty1, mask, filter):
    pass

@accepts(t.uint, t.enum)
@returns(t.enum)
@binds(dll)
def check_named_framebuffer_status(framebuffer, target):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_named_framebuffer_parameteriv(framebuffer, pname, param):
    pass

@accepts(t.uint, t.enum, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_named_framebuffer_attachment_parameteriv(framebuffer, attachment, pname, params):
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_renderbuffers(n, renderbuffers):
    '''
    create renderbuffer objects.
    
    gl.create_renderbuffers returns n previously unused renderbuffer object
    names in renderbuffers, each representing a new renderbuffer object
    initialized to the default state.
    
    Args:
        n: number of renderbuffer objects to create.
        renderbuffers: an array in which names of the new renderbuffer objects
            are stored.
    '''

@accepts(t.uint, t.enum, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def named_renderbuffer_storage(renderbuffer, internalformat, width, height):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def named_renderbuffer_storage_multisample(renderbuffer, samples, internalformat, width, height):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_named_renderbuffer_parameteriv(renderbuffer, pname, params):
    pass

@accepts(t.enum, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_textures(target, n, textures):
    '''
    create texture objects.
    
    gl.create_textures returns n previously unused texture names in textures,
    each representing a new texture object of the dimensionality and type
    specified by target and initialized to the default values for that texture
    type.
    
    Args:
        target: the effective texture target of each created texture.
        n: number of texture objects to create.
        textures: an array in which names of the new texture objects are stored.
    '''

@accepts(t.uint, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def texture_buffer(texture, internalformat, buffer):
    pass

@accepts(t.uint, t.enum, t.uint, t.intptr, t.sizeiptr)
@returns(t.void)
@binds(dll)
def texture_buffer_range(texture, internalformat, buffer, offset, size):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei)
@returns(t.void)
@binds(dll)
def texture_storage1_d(texture, levels, internalformat, width):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def texture_storage2_d(texture, levels, internalformat, width, height):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def texture_storage3_d(texture, levels, internalformat, width, height, depth):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei, t.sizei, t.boolean)
@returns(t.void)
@binds(dll)
def texture_storage2_d_multisample(texture, samples, internalformat, width, height, fixedsamplelocations):
    pass

@accepts(t.uint, t.sizei, t.enum, t.sizei, t.sizei, t.sizei, t.boolean)
@returns(t.void)
@binds(dll)
def texture_storage3_d_multisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations):
    pass

@accepts(t.uint, t.int, t.int, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def texture_sub_image1_d(texture, level, xoffset, width, format, type, pixels):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def texture_sub_image2_d(texture, level, xoffset, yoffset, width, height, format, type, pixels):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.enum, t.void)
@returns(t.void)
@binds(dll)
def texture_sub_image3_d(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
    pass

@accepts(t.uint, t.int, t.int, t.sizei, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def compressed_texture_sub_image1_d(texture, level, xoffset, width, format, imagesize, data):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.sizei, t.sizei, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def compressed_texture_sub_image2_d(texture, level, xoffset, yoffset, width, height, format, imagesize, data):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def compressed_texture_sub_image3_d(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imagesize, data):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei)
@returns(t.void)
@binds(dll)
def copy_texture_sub_image1_d(texture, level, xoffset, x, y, width):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def copy_texture_sub_image2_d(texture, level, xoffset, yoffset, x, y, width, height):
    pass

@accepts(t.uint, t.int, t.int, t.int, t.int, t.int, t.int, t.sizei, t.sizei)
@returns(t.void)
@binds(dll)
def copy_texture_sub_image3_d(texture, level, xoffset, yoffset, zoffset, x, y, width, height):
    pass

@accepts(t.uint, t.enum, t.float)
@returns(t.void)
@binds(dll)
def texture_parameterf(texture, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def texture_parameterfv(texture, pname, param):
    pass

@accepts(t.uint, t.enum, t.int)
@returns(t.void)
@binds(dll)
def texture_parameteri(texture, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def texture_parameter_iiv(texture, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def texture_parameter_iuiv(texture, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def texture_parameteriv(texture, pname, param):
    pass

@accepts(t.uint)
@returns(t.void)
@binds(dll)
def generate_texture_mipmap(texture):
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def bind_texture_unit(unit, texture):
    '''
    bind an existing texture object to the specified texture unit.
    
    gl.bind_texture_unit binds an existing texture object to the texture unit
    numbered unit.
    
    Args:
        unit: the texture unit, to which the texture object should be bound to.
        texture: the name of a texture.
    '''

@accepts(t.uint, t.int, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def get_texture_image(texture, level, format, type, bufsize, pixels):
    pass

@accepts(t.uint, t.int, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def get_compressed_texture_image(texture, level, bufsize, pixels):
    pass

@accepts(t.uint, t.int, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_texture_level_parameterfv(texture, level, pname, params):
    pass

@accepts(t.uint, t.int, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_texture_level_parameteriv(texture, level, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_texture_parameterfv(texture, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_texture_parameter_iiv(texture, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_texture_parameter_iuiv(texture, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_texture_parameteriv(texture, pname, params):
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_vertex_arrays(n, arrays):
    '''
    create vertex array objects.
    
    gl.create_vertex_arrays returns n previously unused vertex array object
    names in arrays, each representing a new vertex array object initialized to
    the default state.
    
    Args:
        n: number of vertex array objects to create.
        arrays: an array in which names of the new vertex array objects are
            stored.
    '''

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def disable_vertex_array_attrib(vaobj, index):
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def enable_vertex_array_attrib(vaobj, index):
    pass

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_element_buffer(vaobj, buffer):
    '''
    configures element array buffer binding of a vertex array object.
    
    gl.vertex_array_element_buffer binds a buffer object with id buffer to the
    element array buffer bind point of a vertex array object with id vaobj. If
    buffer is zero, any existing element array buffer binding to vaobj is
    removed.
    
    Args:
        vaobj: the name of the vertex array object.
        buffer: the name of the buffer object to use for the element array
            buffer binding.
    '''

@accepts(t.uint, t.uint, t.uint, t.intptr, t.sizei)
@returns(t.void)
@binds(dll)
def vertex_array_vertex_buffer(vaobj, bindingindex, buffer, offset, stride):
    pass

@accepts(t.uint, t.uint, t.sizei, POINTER(t.uint), POINTER(t.intptr), POINTER(t.sizei))
@returns(t.void)
@binds(dll)
def vertex_array_vertex_buffers(vaobj, first, count, buffers, offsets, strides):
    pass

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_attrib_binding(vaobj, attribindex, bindingindex):
    pass

@accepts(t.uint, t.uint, t.int, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_attrib_format(vaobj, attribindex, size, type, normalized, relativeoffset):
    pass

@accepts(t.uint, t.uint, t.int, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_attrib_i_format(vaobj, attribindex, size, type, relativeoffset):
    pass

@accepts(t.uint, t.uint, t.int, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_attrib_l_format(vaobj, attribindex, size, type, relativeoffset):
    pass

@accepts(t.uint, t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_array_binding_divisor(vaobj, bindingindex, divisor):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_vertex_arrayiv(vaobj, pname, param):
    '''
    retrieve parameters of a vertex array object.
    
    gl.get_vertex_arrayiv can be used to retrieve ID of a buffer object that
    will be bound to the gl.ELEMENT_ARRAY_BUFFER binding point whenever the
    queried vertex array object is bound to the rendering context. The binding
    can be changed for an active vertex array object with a gl.bind_buffer call.
    
    Args:
        vaobj: the name of the vertex array object to use for the query.
        pname: name of the property to use for the query.
        param: returns the requested value.
    '''

@accepts(t.uint, t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_vertex_array_indexediv(vaobj, index, pname, param):
    pass

@accepts(t.uint, t.uint, t.enum, POINTER(t.int64))
@returns(t.void)
@binds(dll)
def get_vertex_array_indexed64iv(vaobj, index, pname, param):
    pass

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_samplers(n, samplers):
    '''
    create sampler objects.
    
    gl.create_samplers returns n previously unused sampler names in samplers,
    each representing a new sampler object initialized to the default state.
    
    Args:
        n: number of sampler objects to create.
        samplers: an array in which names of the new sampler objects are stored.
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_program_pipelines(n, pipelines):
    '''
    create program pipeline objects.
    
    gl.create_program_pipelines returns n previously unused program pipeline
    names in pipelines, each representing a new program pipeline object
    initialized to the default state.
    
    Args:
        n: number of program pipeline objects to create.
        pipelines: an array in which names of the new program pipeline objects
            are stored.
    '''

@accepts(t.enum, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def create_queries(target, n, ids):
    '''
    create query objects.
    
    gl.create_queries returns n previously unused query object names in ids,
    each representing a new query object with the specified target.
    
    Args:
        target: the target of each created query object.
        n: number of query objects to create.
        ids: an array in which names of the new query objects are stored.
    '''

@accepts(t.uint, t.uint, t.enum, t.intptr)
@returns(t.void)
@binds(dll)
def get_query_buffer_objecti64v(id, buffer, pname, offset):
    pass

@accepts(t.uint, t.uint, t.enum, t.intptr)
@returns(t.void)
@binds(dll)
def get_query_buffer_objectiv(id, buffer, pname, offset):
    pass

@accepts(t.uint, t.uint, t.enum, t.intptr)
@returns(t.void)
@binds(dll)
def get_query_buffer_objectui64v(id, buffer, pname, offset):
    pass

@accepts(t.uint, t.uint, t.enum, t.intptr)
@returns(t.void)
@binds(dll)
def get_query_buffer_objectuiv(id, buffer, pname, offset):
    pass

TEXTURE_TARGET = 0x1006
QUERY_TARGET = 0x82EA
TEXTURE_BINDING_1D = 0x8068
TEXTURE_BINDING_1D_ARRAY = 0x8C1C
TEXTURE_BINDING_2D = 0x8069
TEXTURE_BINDING_2D_ARRAY = 0x8C1D
TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
TEXTURE_BINDING_3D = 0x806A
TEXTURE_BINDING_BUFFER = 0x8C2C
TEXTURE_BINDING_CUBE_MAP = 0x8514
TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
TEXTURE_BINDING_RECTANGLE = 0x84F6
@accepts(t.bitfield)
@returns(t.void)
@binds(dll)
def memory_barrier_by_region(barriers):
    pass

BACK = 0x0405
@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def get_texture_sub_image(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufsize, pixels):
    '''
    retrieve a sub-region of a texture image from a texture object.
    
    gl.get_texture_sub_image returns a texture subimage into pixels.
    
    Args:
        texture: the name of the source texture object.
        level: the level-of-detail number.
        xoffset: a texel offset in the x direction within the texture array.
        yoffset: a texel offset in the y direction within the texture array.
        zoffset: a texel offset in the z direction within the texture array.
        width: the width of the texture subimage.
        height: the height of the texture subimage.
        depth: the depth of the texture subimage.
        format: the format of the pixel data.
        type: the data type of the pixel data.
        bufsize: the size of the buffer to receive the retrieved pixel data.
        pixels: returns the texture subimage.
    '''

@accepts(t.uint, t.int, t.int, t.int, t.int, t.sizei, t.sizei, t.sizei, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def get_compressed_texture_sub_image(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufsize, pixels):
    '''
    retrieve a sub-region of a compressed texture image from a compressed
    texture object.
    
    gl.get_compressed_texture_sub_image can be used to obtain a sub-region of a
    compressed texture image instead of the whole image, as long as the
    compressed data are arranged into fixed-size blocks of texels. texture is
    the name of the texture object, and must not be a buffer or multisample
    texture. The effective target is the value of gl.TEXTURE_TARGET for texture.
    level and pixels have the same meaning as the corresponding arguments of
    gl.compressed_tex_sub_image3D.
    
    Args:
        texture: the name of the source texture object.
        level: the level-of-detail number.
        xoffset: a texel offset in the x direction within the texture array.
        yoffset: a texel offset in the y direction within the texture array.
        zoffset: a texel offset in the z direction within the texture array.
        width: the width of the texture subimage.
        height: the height of the texture subimage.
        depth: the depth of the texture subimage.
        bufsize: the size of the buffer to receive the retrieved pixel data.
        pixels: returns the texture subimage.
    '''

@accepts()
@returns(t.enum)
@binds(dll)
def get_graphics_reset_status():
    '''
    check if the rendering context has not been lost due to software or hardware
    issues.
    '''

@accepts(t.enum, t.int, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_compressed_tex_image(target, lod, bufsize, pixels):
    pass

@accepts(t.enum, t.int, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_tex_image(target, level, format, type, bufsize, pixels):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def getn_uniformdv(program, location, bufsize, params):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def getn_uniformfv(program, location, bufsize, params):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def getn_uniformiv(program, location, bufsize, params):
    pass

@accepts(t.uint, t.int, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def getn_uniformuiv(program, location, bufsize, params):
    pass

@accepts(t.int, t.int, t.sizei, t.sizei, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def readn_pixels(x, y, width, height, format, type, bufsize, data):
    pass

NO_ERROR = 0
GUILTY_CONTEXT_RESET = 0x8253
INNOCENT_CONTEXT_RESET = 0x8254
UNKNOWN_CONTEXT_RESET = 0x8255
RESET_NOTIFICATION_STRATEGY = 0x8256
LOSE_CONTEXT_ON_RESET = 0x8252
NO_RESET_NOTIFICATION = 0x8261
CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
CONTEXT_LOST = 0x0507
@accepts(t.enum, t.enum, t.sizei, POINTER(t.double))
@returns(t.void)
@binds(dll)
def getn_mapdv(target, query, bufsize, v):
    pass

@accepts(t.enum, t.enum, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def getn_mapfv(target, query, bufsize, v):
    pass

@accepts(t.enum, t.enum, t.sizei, POINTER(t.int))
@returns(t.void)
@binds(dll)
def getn_mapiv(target, query, bufsize, v):
    pass

@accepts(t.enum, t.sizei, POINTER(t.float))
@returns(t.void)
@binds(dll)
def getn_pixel_mapfv(map, bufsize, values):
    pass

@accepts(t.enum, t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def getn_pixel_mapuiv(map, bufsize, values):
    pass

@accepts(t.enum, t.sizei, POINTER(t.ushort))
@returns(t.void)
@binds(dll)
def getn_pixel_mapusv(map, bufsize, values):
    pass

@accepts(t.sizei, POINTER(t.ubyte))
@returns(t.void)
@binds(dll)
def getn_polygon_stipple(bufsize, pattern):
    pass

@accepts(t.enum, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_color_table(target, format, type, bufsize, table):
    pass

@accepts(t.enum, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_convolution_filter(target, format, type, bufsize, image):
    pass

@accepts(t.enum, t.enum, t.enum, t.sizei, t.void, t.sizei, t.void, t.void)
@returns(t.void)
@binds(dll)
def getn_separable_filter(target, format, type, rowbufsize, row, columnbufsize, column, span):
    pass

@accepts(t.enum, t.boolean, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_histogram(target, reset, format, type, bufsize, values):
    pass

@accepts(t.enum, t.boolean, t.enum, t.enum, t.sizei, t.void)
@returns(t.void)
@binds(dll)
def getn_minmax(target, reset, format, type, bufsize, values):
    pass

@accepts()
@returns(t.void)
@binds(dll)
def texture_barrier():
    '''
    controls the ordering of reads and writes to rendered fragments across
    drawing commands.
    '''

CONTEXT_RELEASE_BEHAVIOR = 0x82FB
NONE = 0
CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC