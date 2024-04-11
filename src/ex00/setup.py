from setuptools import setup, Extension

"""Запуск python setup.py install"""

module = Extension('calculator', sources=['calculator.c'])
setup(name='calculator',
      version='1.0',
      description='A simple calculator module',
      ext_modules=[module])
