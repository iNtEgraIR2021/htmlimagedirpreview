# -*- coding: utf-8 -*-

from setuptools import setup
from imagedirpreview.release import __version__

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup(
    name='imagedirpreview',
    version=__version__,
    author='Carsten Knoll',
    author_email='...',
    packages=['imagedirpreview'],
    package_data={'imagedirpreview': ['templates/*']},
    url='...',
    license='BSD3',
    description='Script for previewing the image-content of directories on the file system',
    long_description="""
    Script for previewing the image-content of directories on the file system.
    Generates a html outputfile at current directory.
    """,
    keywords='image preview, helper script',
    install_requires=requirements,
    entry_points={'console_scripts': ['imagedirpreview=imagedirpreview:main']}
)
