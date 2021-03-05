glnext-compiler
===============

This library is a standalone GLSL compiler for vulkan projects.
The binaries do not require the vulkan-sdk to be installed.
This library uses `shaderc`_.

.. _shaderc: https://github.com/google/shaderc

There is a single method available:

.. method:: glnext_compiler.glsl(source: str) -> bytes

It compiles the souce into spv and returns it as bytes.
The result can be saved to a file or used directly for glnext pipeline creation.
The result is platform independend and can be shipped instead of the source code.

    "Explicit is better than implicit."

- The glsl version and shader stage must be specified.
- The layout quailfiers are obligatory for all types.

Examples
--------

.. code:: python

    from glnext_compiler import glsl

    spv = glsl('''
        #version 450
        #pragma shader_stage(vertex)

        layout (location = 0) in vec2 in_vert;

        void main() {
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
    ''')
