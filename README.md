# OpenGL.py

OpenGL.py is a raw ctypes wrapper over opengl. Access to gl commands, enums, and declared types are provided.
gl functions and constants have been defined in the module opengl.

## Why use OpenGL.py?

The reasons for this package's existance was simple, after having a brief stint into PyOpenGL, I was frustrated by
the lack of documentation on the binding and the true to gl naming conventions without being true to the call signatures.
These were big grumbles, my gl code was noisy, banging its `camelCase` hands together, attracting untoward attention while
coding. When I did need to interact with gl, my editor's completion functionality wasn't especially informative.
OpenGL.py sets out to resolve these issues.

### Write PEP 8 code
We aren't morons, we can quickly and easily translate PEP 8 names into their counterparts.

OpenGL.py transforms the spec from the gl registry for PEP 8 naming conventions.
Below, is some code that demonstrates the usage of gl types, enums and commands under OpenGL.py:

```python
from opengl import gl

buffers = (gl.uint * 1)()
gl.gen_buffers(1, buffers)
gl.bind_buffer(gl.ARRAY_BUFFER, buffers[0])
```

All OpenGL.py functions conform to this convention, regardless of weither you are using the 

### OpenGL call signatures
OpenGL.py currently does nothing to protect you, as the coder, from the weirder merky depths of OpenGL.

The only difference between the spec, and OpenGL.py you should observe is:
* The naming conventions follow `words_with_underscores` instead of `camelCase`.
* The 'gl' prefix is omitted from command names and type defintions, and the 'GL_' prefixx is removed from enum values.
* Any names that now start with a number (there are a few, I'm not sure I've ever used them though) are prefixed with an underscore.

Aside from the three transformations above, the `opengl.gl.raw` package contains no changes to the spec.
Any changes added to the `opengl.gl` package should be constructive, however if you are concerned about the call signatures
of the api changing, use this package instead with the directive `from opengl.gl import raw as gl`.

### Docstrings
OpenGL.py also includes docstrings as part of the bindings.
This means if your workflow includes docstrings through a completion editor, your editor should display a short description of the command and its arguments.

Hazzah, no more travelling back to the api documentation just to double check on an esoteric function.

## Future changes
OpenGL.py needs improvement:
* More protection from ctypes quirks.
* Additions to negate gl spec insanity.
* Object orientated access to the api. (The dream of dreams.)
* Docstrings which contain long form descriptions, return values, etc.
* Checking gl.error and throwing an exception.
* Bindings for glu and glut. Presently, these are simple wrappers to PyOpenGL to fix the naming conventions used.
