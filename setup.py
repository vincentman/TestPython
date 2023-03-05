from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name='wrap_c', sources=['tmpProject.cpp', 'test_wrap_c.pyx'])
setup(ext_modules=cythonize(ext))

