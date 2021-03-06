#BEWARE: automatically generated code
#This code was generated by /generate/__main__.py

from opengl.gl.raw.bindings import *

VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
@accepts(t.uint, t.uint, t.uint, t.char_p)
@returns(t.void)
@binds(dll)
def bind_frag_data_location_indexed(program, colornumber, index, name):
    '''
    bind a user-defined varying out variable to a fragment shader color number
    and index.
    
    gl.bind_frag_data_location_indexed specifies that the varying out variable
    name in program should be bound to fragment color colorNumber when the
    program is next linked. index may be zero or one to specify that the color
    be used as either the first or second color input to the blend equation,
    respectively.
    
    Args:
        program: the name of the program containing varying out variable whose
            binding to modify.
        colornumber: the color number to bind the user-defined varying out
            variable to.
        index: the index of the color input to bind the user-defined varying out
            variable to.
        name: the name of the user-defined varying out variable whose binding to
            modify.
    '''

@accepts(t.uint, t.char_p)
@returns(t.int)
@binds(dll)
def get_frag_data_index(program, name):
    '''
    query the bindings of color indices to user-defined varying out variables.
    
    gl.get_frag_data_index returns the index of the fragment color to which the
    variable name was bound when the program object program was last linked. If
    name is not a varying out variable of program, or if an error occurs, -1
    will be returned.
    
    Args:
        program: the name of the program containing varying out variable whose
            binding to query.
        name: the name of the user-defined varying out variable whose index to
            query.
    '''

SRC1_COLOR = 0x88F9
ONE_MINUS_SRC1_COLOR = 0x88FA
ONE_MINUS_SRC1_ALPHA = 0x88FB
MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
ANY_SAMPLES_PASSED = 0x8C2F
@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def gen_samplers(count, samplers):
    '''
    generate sampler object names.
    
    gl.gen_samplers returns n sampler object names in samplers. There is no
    guarantee that the names form a contiguous set of integers; however, it is
    guaranteed that none of the returned names was in use immediately before the
    call to gl.gen_samplers.
    
    Args:
        count: the number of sampler object names to generate.
        samplers: an array in which the generated sampler object names are
            stored.
    '''

@accepts(t.sizei, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def delete_samplers(count, samplers):
    '''
    delete named sampler objects.
    
    gl.delete_samplers deletes n sampler objects named by the elements of the
    array samplers. After a sampler object is deleted, its name is again unused.
    If a sampler object that is currently bound to a sampler unit is deleted, it
    is as though gl.bind_sampler is called with unit set to the unit the sampler
    is bound to and sampler zero. Unused names in samplers are silently ignored,
    as is the reserved name zero.
    
    Args:
        count: the number of sampler objects to be deleted.
        samplers: an array of sampler objects to be deleted.
    '''

@accepts(t.uint)
@returns(t.boolean)
@binds(dll)
def is_sampler(sampler):
    '''
    determine if a name corresponds to a sampler object.
    
    gl.is_sampler returns gl.TRUE if id is currently the name of a sampler
    object. If id is zero, or is a non-zero value that is not currently the name
    of a sampler object, or if an error occurs, gl.is_sampler returns gl.FALSE.
    
    Args:
        sampler: a value that may be the name of a sampler object.
    '''

@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def bind_sampler(unit, sampler):
    '''
    bind a named sampler to a texturing target.
    
    gl.bind_sampler binds sampler to the texture unit at index unit. sampler
    must be zero or the name of a sampler object previously returned from a call
    to gl.gen_samplers. unit must be less than the value of
    gl.MAX_COMBINED_TEXTURE_IMAGE_UNITS.
    
    Args:
        unit: the index of the texture unit to which the sampler is bound.
        sampler: the name of a sampler.
    '''

@accepts(t.uint, t.enum, t.int)
@returns(t.void)
@binds(dll)
def sampler_parameteri(sampler, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def sampler_parameteriv(sampler, pname, param):
    pass

@accepts(t.uint, t.enum, t.float)
@returns(t.void)
@binds(dll)
def sampler_parameterf(sampler, pname, param):
    pass

@accepts(t.uint, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def sampler_parameterfv(sampler, pname, param):
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
def get_sampler_parameteriv(sampler, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.int))
@returns(t.void)
@binds(dll)
def get_sampler_parameter_iiv(sampler, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.float))
@returns(t.void)
@binds(dll)
def get_sampler_parameterfv(sampler, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def get_sampler_parameter_iuiv(sampler, pname, params):
    pass

SAMPLER_BINDING = 0x8919
RGB10_A2UI = 0x906F
TEXTURE_SWIZZLE_R = 0x8E42
TEXTURE_SWIZZLE_G = 0x8E43
TEXTURE_SWIZZLE_B = 0x8E44
TEXTURE_SWIZZLE_A = 0x8E45
TEXTURE_SWIZZLE_RGBA = 0x8E46
@accepts(t.uint, t.enum)
@returns(t.void)
@binds(dll)
def query_counter(id, target):
    '''
    record the GL time into a query object after all previous commands have
    reached the GL server but have not yet necessarily executed..
    
    gl.query_counter causes the GL to record the current time into the query
    object named id. target must be gl.TIMESTAMP. The time is recorded after all
    previous commands on the GL client and server state and the framebuffer have
    been fully realized. When the time is recorded, the query result for that
    object is marked available.
    
    Args:
        id: the name of a query object into which to record the gl time.
        target: the counter to query.
    '''

@accepts(t.uint, t.enum, POINTER(t.int64))
@returns(t.void)
@binds(dll)
def get_query_objecti64v(id, pname, params):
    pass

@accepts(t.uint, t.enum, POINTER(t.uint64))
@returns(t.void)
@binds(dll)
def get_query_objectui64v(id, pname, params):
    pass

TIME_ELAPSED = 0x88BF
TIMESTAMP = 0x8E28
@accepts(t.uint, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_divisor(index, divisor):
    '''
    modify the rate at which generic vertex attributes advance during instanced
    rendering.
    
    gl.vertex_attrib_divisor modifies the rate at which generic vertex
    attributes advance when rendering multiple instances of primitives in a
    single draw call. If divisor is zero, the attribute at slot index advances
    once per vertex. If divisor is non-zero, the attribute advances once per
    divisor instances of the set of vertices being rendered. An attribute is
    referred to as instanced if its gl.VERTEX_ATTRIB_ARRAY_DIVISOR value is non-
    zero.
    
    Args:
        index: the index of the generic vertex attribute.
        divisor: the number of instances that will pass between updates of the
            generic attribute at slot index.
    '''

@accepts(t.uint, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_p1ui(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_p1uiv(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_p2ui(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_p2uiv(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_p3ui(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_p3uiv(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, t.uint)
@returns(t.void)
@binds(dll)
def vertex_attrib_p4ui(index, type, normalized, value):
    pass

@accepts(t.uint, t.enum, t.boolean, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_attrib_p4uiv(index, type, normalized, value):
    pass

INT_2_10_10_10_REV = 0x8D9F
@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_p2ui(type, value):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_p2uiv(type, value):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_p3ui(type, value):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_p3uiv(type, value):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def vertex_p4ui(type, value):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def vertex_p4uiv(type, value):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_coord_p1ui(type, coords):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def tex_coord_p1uiv(type, coords):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_coord_p2ui(type, coords):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def tex_coord_p2uiv(type, coords):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_coord_p3ui(type, coords):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def tex_coord_p3uiv(type, coords):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def tex_coord_p4ui(type, coords):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def tex_coord_p4uiv(type, coords):
    pass

@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def multi_tex_coord_p1ui(texture, type, coords):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def multi_tex_coord_p1uiv(texture, type, coords):
    pass

@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def multi_tex_coord_p2ui(texture, type, coords):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def multi_tex_coord_p2uiv(texture, type, coords):
    pass

@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def multi_tex_coord_p3ui(texture, type, coords):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def multi_tex_coord_p3uiv(texture, type, coords):
    pass

@accepts(t.enum, t.enum, t.uint)
@returns(t.void)
@binds(dll)
def multi_tex_coord_p4ui(texture, type, coords):
    pass

@accepts(t.enum, t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def multi_tex_coord_p4uiv(texture, type, coords):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def normal_p3ui(type, coords):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def normal_p3uiv(type, coords):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def color_p3ui(type, color):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def color_p3uiv(type, color):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def color_p4ui(type, color):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def color_p4uiv(type, color):
    pass

@accepts(t.enum, t.uint)
@returns(t.void)
@binds(dll)
def secondary_color_p3ui(type, color):
    pass

@accepts(t.enum, POINTER(t.uint))
@returns(t.void)
@binds(dll)
def secondary_color_p3uiv(type, color):
    pass
