import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        'crowdposetools._mask',
        sources=['../common/maskApi.c', 'crowdposetools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name="crowdposetools",
    version="2.0.1",
    description="Modernized crowdposetools with bugfix.",
    ext_modules=cythonize(ext_modules),
)
