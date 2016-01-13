# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from com_tf import version

setup(
        name='file_express',
        version=version,
        description='Togeek file express',
        classifiers=['Programming Language :: Python :: 3.4'],
        packages=find_packages(),
        include_package_data=True,
        install_requires=['psutil'],
        entry_points={'console_scripts': ['fexp=file_express:main']}
)
