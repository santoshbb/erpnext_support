# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_support/__init__.py
from erpnext_support import __version__ as version

setup(
	name='erpnext_support',
	version=version,
	description='ERPNext-Support',
	author='biradar',
	author_email='santosh.baburao@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
