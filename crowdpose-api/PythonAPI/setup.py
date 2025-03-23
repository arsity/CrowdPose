from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
import numpy as np

ext_modules = [
    Extension(
        'crowdposetools._mask',
        sources=['../common/maskApi.c', 'crowdposetools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(ext_modules=cythonize(ext_modules))
