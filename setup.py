#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name = 'Phone-Pipe',
    version = '0.1',
    install_requires = ['simplejson'],
    scripts = ['phone'],
)
