# glnext-compiler

```sh
pip install glnext-compiler
```

- [Documentation](https://glnext-compiler.readthedocs.io/)
- [glnext-compiler on Github](https://github.com/cprogrammer1994/glnext-compiler)
- [glnext-compiler on PyPI](https://pypi.org/project/glnext-compiler/)

This library is a standalone GLSL compiler for vulkan projects.<br>
The binaries do not require the vulkan-sdk to be installed.<br>
This library uses [shaderc](https://github.com/google/shaderc).

## Example

```py
from glnext_compiler import glsl

spv = glsl('''
    #version 450
    #pragma shader_stage(vertex)

    layout (location = 0) in vec2 in_vert;

    void main() {
        gl_Position = vec4(in_vert, 0.0, 1.0);
    }
''')
```
