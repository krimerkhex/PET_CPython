from setuptools import setup
from Cython.Build import cythonize

"""Запуск python setup.py install"""

setup(
    name='matrix',
    ext_modules=cythonize("multiply.pyx")
)
