# htmlimagedirpreview
based on imagedirpreview [![PyPI version](https://badge.fury.io/py/imagedirpreview.svg)](https://badge.fury.io/py/imagedirpreview) -> copyright: Carsten Knoll

Simple script to generate a browser based html preview page of all 🖼️ images (`.svg`, `.png`, `.jpg`, ...) in a 📁directory.
This might be useful to get an quick overview over a lots of images (like icon sets).
In fact, the creation of this script was motivated by curiosity about the contents of
[papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/).

## Installation
```bash
pip install git+https://github.com/iNtEgraIR2021/htmlimagedirpreview.git
```

## Usage
Simply run `imagedirpreview` in the directory where the images are in.
A html-file will be created, which includes all images.
Note that the browser might take some time to load all images.
Tested with a ca. 1500 svg-icons (64x64).
