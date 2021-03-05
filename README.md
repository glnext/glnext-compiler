# glnext-compiler

GLSL compiler for the glnext examples

```sh
pip install glnext-compiler
```

- [Documentation](https://glnext-compiler.readthedocs.io/)
- [glnext-compiler on Github](https://github.com/cprogrammer1994/glnext-compiler)
- [glnext-compiler on PyPI](https://pypi.org/project/glnext-compiler/)

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
