import os
from setuptools import Extension, setup

ext = Extension(
    name='glnext_compiler',
    sources=['./glnext_compiler.cpp'],
    include_dirs=[os.path.join(os.getenv('VULKAN_SDK'), 'Include')],
    library_dirs=[os.path.join(os.getenv('VULKAN_SDK'), 'Lib')],
    libraries=['shaderc_combined'],
)

setup(
    name='glnext_compiler',
    version='0.1.0',
    ext_modules=[ext],
)
