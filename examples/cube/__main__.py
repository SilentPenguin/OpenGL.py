'''
This program demonstrates a multi-coloured cube spinning in space.

It is designed to be run using the command 'python cube' from the examples 
directory.

This is presented as an example for the OpenGL.py binding, and is intended to
be as pure as possible. This is not intended to act as a lesson in OpenGL.
'''

from sys import path

path.append('..')

from opengl import gl, glut
from time import sleep
from math import cos, sin

class Application():
    run = glut.main_loop

    def __init__(self):
        # set up our application
        self.initialise_glut()
        self.configure_gl()

        # create our cube object
        self.cube = Cube()

    def initialise_glut(self):
        # initialise a window in glut
        glut.init()
        glut.init_display_mode(glut.DOUBLE | glut.RGB | glut.DEPTH | glut.MULTISAMPLE | glut._3_2_CORE_PROFILE)
        glut.init_window_size(500,500)
        glut.create_window("example")

        # bind the glut callbacks
        glut.display_func(self.display)
        glut.wm_close_func(self.close)
        
    def configure_gl(self):
        # set the frame clear parameters
        gl.clear_color(1,1,1,1)
        gl.clear_depth(1)
        # enable depth test and anti-aliasing
        gl.enable(gl.MULTISAMPLE)
        gl.enable(gl.DEPTH_TEST)
        gl.depth_func(gl.LESS)
        

    def display(self):
        # clear the screen
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)

        # render
        self.cube.render()
        
        #finish the frame and release control to the cpu
        glut.swap_buffers()
        glut.post_redisplay()
        sleep(0)

    def close(self):
        quit()

class Cube:

    vertex_data = gl.float[8*3](
         1, 1,  1,
         1,-1,  1,
        -1, 1,  1,
        -1,-1,  1,
         1, 1, -1,
         1,-1, -1,
        -1, 1, -1,
        -1,-1, -1
    )

    color_data = gl.float[8*3](
        0, 0, 0,
        1, 0, 0,
        0, 1, 0,
        0, 0, 1,
        0, 1, 1,
        1, 0, 1,
        1, 1, 0,
        1, 1, 1,
    )

    index_data = gl.uint[6*3*2](
        0, 1, 2,    1, 2, 3,
        4, 5, 6,    5, 6, 7,
        0, 1, 4,    1, 4, 5,
        2, 3, 6,    3, 6, 7,
        0, 2, 4,    2, 4, 6,
        1, 3, 5,    3, 5, 7
    )

    vert_shader_code = """
    #version 330
    in vec3 in_vertex;
    in vec3 in_vertex_color;
    out vec4 vert_color;
    uniform mat4 in_transform;
    void main ()
    {
        mat4 world = mat4(0.25);
        world[3] = vec4(0, 0, 0, 1);
        vec4 pos = world * in_transform * vec4(in_vertex, 1.0);
        gl_Position = pos;
        vert_color = vec4(in_vertex_color, 1.0);
    }
    """

    frag_shader_code = """
    #version 330
    in vec4 vert_color;
    uniform vec4 in_color;
    out vec4 out_color;
    void main()
    {
        out_color = vert_color * in_color;
    }
    """

    def __init__(self):
        self.create_program()
        self.create_buffers()
        self.buffer_data()
        self.t = 0

    def create_buffers(self):
        # generate our vao
        uint_array = gl.uint[3]()
        gl.gen_vertex_arrays(1, uint_array)
        self.vao = uint_array[0]
        # generate our buffer objects
        gl.gen_buffers(3, uint_array)
        self.vbo, self.ebo, self.cbo = uint_array

    def create_program(self):
        # create our program, shaders, then attach, and link them to the program 
        self.shader_program = gl.create_program()
        vert_shader = self.create_shader(gl.VERTEX_SHADER, self.vert_shader_code)
        frag_shader = self.create_shader(gl.FRAGMENT_SHADER, self.frag_shader_code)
        gl.attach_shader(self.shader_program, vert_shader)
        gl.attach_shader(self.shader_program, frag_shader)
        gl.link_program(self.shader_program)

        # check to make sure the link was successful
        buf_size = gl.int()
        gl.get_programiv(self.shader_program, gl.INFO_LOG_LENGTH, buf_size)
        message = gl.char[buf_size.value]()
        gl.get_program_info_log(self.shader_program, buf_size, None, message)
        message = message.value
        if message:
            print message
            quit()
        
        # get our attributes and uniforms and assign them into our program for convinience
        self.shader_program.in_vertex = gl.uint(gl.get_attrib_location(self.shader_program, "in_vertex").value) #appears to not return gl.uint, regardless of binding
        self.shader_program.in_vertex_color = gl.uint(gl.get_attrib_location(self.shader_program, "in_vertex_color").value) #appears to not return gl.uint, regardless of binding
        self.shader_program.in_color = gl.get_uniform_location(self.shader_program, "in_color")
        self.shader_program.in_transform = gl.get_uniform_location(self.shader_program, "in_transform")

    def create_shader(self, type, code):
        # create our shader, upload the code and compile
        code = gl.char_p[1](code)
        shader = gl.create_shader(type)
        gl.shader_source(shader, 1, code, None)
        gl.compile_shader(shader)

        # check that creating our shader was successful
        buf_size = gl.int()
        gl.get_shaderiv(shader, gl.INFO_LOG_LENGTH, buf_size)
        message = gl.char[buf_size.value]()
        gl.get_shader_info_log(shader, buf_size, None, message)
        message = message.value
        if message:
            print message
            quit()
        return shader

    def buffer_data(self):
        gl.bind_vertex_array(self.vao)
        self.send_buffer_data(self.vbo, self.vertex_data, gl.FLOAT, gl.ARRAY_BUFFER, self.shader_program.in_vertex)
        self.send_buffer_data(self.cbo, self.color_data, gl.FLOAT, gl.ARRAY_BUFFER, self.shader_program.in_vertex_color)
        self.send_buffer_data(self.ebo, self.index_data, gl.UNSIGNED_INT, gl.ELEMENT_ARRAY_BUFFER)

    def send_buffer_data(self, buffer, data, datatype, type, pointer = None):
        gl.bind_buffer(type, buffer)
        if pointer != None: gl.vertex_attrib_pointer(pointer, 3, datatype, False, 0, None)
        gl.buffer_data(type, gl.sizeof(data), data, gl.STATIC_DRAW)
        
    def render(self):
        # keep track of time for our animation
        t = self.t = self.t + 0.025;

        # create a transformation matrix for our current time
        transform = gl.float[16](
            cos(t), -sin(t) * sin(t*0.5), -sin(t) * cos(t*0.5), 0,
            0, cos(t*0.5), -sin(t*0.5), 0,
            sin(t), cos(t) * sin(t*0.5),  cos(t) * cos(t*0.5), 0,
            0, 0, 0, 1
        )

        # prepare for rendering by setting the program, enabling our attributes, and uploading our uniforms 
        gl.bind_vertex_array(self.vao)
        gl.use_program(self.shader_program)
        gl.uniform4f(self.shader_program.in_color, 1, 1, 1, 1)
        gl.uniform_matrix4fv(self.shader_program.in_transform, 1, False, transform)
        gl.enable_vertex_attrib_array(self.shader_program.in_vertex)
        gl.enable_vertex_attrib_array(self.shader_program.in_vertex_color)

        # draw our cube using the indicies uploaded to the ebo.
        gl.draw_elements(gl.TRIANGLES, len(self.index_data), gl.UNSIGNED_INT, None)

        # remove states previously set before rendering
        gl.disable_vertex_attrib_array(self.shader_program.in_vertex)
        gl.disable_vertex_attrib_array(self.shader_program.in_vertex_color)
        gl.use_program(0)
        gl.bind_vertex_array(0)

if __name__ == '__main__': Application().run()