import os
import platform
from setuptools import Extension, setup

PLATFORMS = {'windows', 'linux', 'darwin'}

target = platform.system().lower()

for known in PLATFORMS:
    if target.startswith(known):
        target = known
        break

extra_compile_args = []
extra_link_args = []
include_dirs = []
library_dirs = []
libraries = []

if target == 'windows':
    include_dirs.append(os.path.join(os.getenv('VULKAN_SDK'), 'Include'))
    library_dirs.append(os.path.join(os.getenv('VULKAN_SDK'), 'Lib'))
    libraries.append('shaderc_combined')

if target == 'linux':
    extra_compile_args.append('-fpermissive')
    libraries.append('shaderc_combined')

glnext_compiler = Extension(
    name='glnext_compiler',
    sources=['./glnext_compiler.cpp'],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    libraries=libraries,
)

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='glnext_compiler',
    version='0.3.0',
    ext_modules=[glnext_compiler],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cprogrammer1994/glnext_compiler',
    author='Szabolcs Dombi',
    author_email='cprogrammer1994@gmail.com',
    license='MIT',
)
