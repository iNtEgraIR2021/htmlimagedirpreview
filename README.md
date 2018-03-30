# imagedirpreview

Simple script to generate a browser based preview of all images in a directory.
This might be useful to get an quick overview over a lots of images (like icon sets).
In fact, the creation of this script was motivated by curiosity about the contents of
[papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/).

## Installation
`pip install imagedirpreview`

## Usage
Simply run `imagedirpreview` in the directory where the images are in.
A html-file will be created, which includes all images.
Note that the browser might take some time to load all images.
Tested with a ca. 1500 svg-icons (64x64).

[![Video (hosted at VIMEO)](doc/vimeo_screenshot.png)](https://vimeo.com/262475545 "Demo of imagedirpreview")

## TODO

**Note:** These todos will only be realized if considerable need is detected.

- recognition of already handled files (symlinks)
- use flask instead of a local html-file
    - figure out how to display images from the current working directory in flask
    - use grip as guideline
