import sys
sys.path.append('.')

from setuptools import setup
from cmake_extension import CMakeBuild, CMakeExtension

setup(
    name='my_package',
    version='0',
    ext_modules=[
        CMakeExtension('my_package'),
        CMakeExtension('noxitu.my_package')
    ],
    cmdclass=dict(build_ext=CMakeBuild('src')),
)
