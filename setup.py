# -*- coding: utf-8 -*-

from setuptools import setup
from htmlimagedirpreview.release import __version__

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    name='htmlimagedirpreview',
    version=__version__,
    author='Carsten Knoll',
    packages=['htmlimagedirpreview'],
    package_data={'htmlimagedirpreview': ['templates/*']},
    url='https://github.com/iNtEgraIR2021/htmlimagedirpreview/',
    license='BSD3',
    description='Script for previewing the image-content of directories on the file system',
    long_description="""
    Script for previewing the image-content of directories on the file system.
    Generates a html outputfile at current directory.
    
    Based on `imagedirpreview` under copyright by Carsten Knoll.
    """,
    keywords='image preview, helper script',
    install_requires=requirements,
    entry_points={'console_scripts': ['htmlimagedirpreview=htmlimagedirpreview:main']}
)
