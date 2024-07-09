# import tools to create the C extension
from distutils.core import setup, Extension

module_name = 'geo'
# the files your extension is comprised of
c_files = ['geo.cpp']
include_dirs = ['/usr/include/python3.11/numpy']

extension = Extension(
    module_name,
    c_files,
    include_dirs
)

setup(
    name=module_name,
    version='1.0',
    description='The package description',
    author='',
    author_email='',
    url='',
    ext_modules=[extension]
)