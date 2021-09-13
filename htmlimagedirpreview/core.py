#!/usr/bin/env python3

"""
This script serves to generate a browser based preview of all images in a directory.
"""

from functools import partial
import sys
import os
import jinja2

IMAGE_EXTENSIONS = [".svg", ".png", ".jpg", ".jpeg", ".gif", ".bmp"]
RESULT_FNAME = "000_preview.html"


def get_template_path():
    """
    Find out the path of the template. This is not trivial if installed
    via pip.
    """

    mod = sys.modules.get(__name__)
    if mod is not None and hasattr(mod, '__file__'):
        modpath = os.path.dirname(os.path.abspath(mod.__file__))
        templatepath = os.path.join(modpath, "templates", "base.html")
    else:
        msg = "Could not find the path of the module: {}".format(__name__)
        raise ValueError(msg)

    if not os.path.isfile(templatepath):
        msg = "Could not find the template at path {}".format(templatepath)
        raise FileNotFoundError(msg)

    return templatepath


def render(tpl_path, context):
    """
    Renders the template at tpl_path with the context (dict-like)
    """
    # source: http://matthiaseisen.com/pp/patterns/p0198/
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def is_image_file(path, fname):
    """
    Determine if the file is an image
    """
    if not os.path.isfile(os.path.join(path, fname)):
        return False

    for ext in IMAGE_EXTENSIONS:
        if fname.lower().endswith(ext):
            return True
    return False


def get_all_image_fnames(path="."):
    """
    Return a list of file names: images in current directory
    """
    dircontent = os.listdir(path)

    imagelist = sorted(filter(partial(is_image_file, path), dircontent))

    return list(imagelist)


def main():
    """
    Main function. serves as entry point for the bash script.
    See setup.py
    """

    dirpath = os.path.abspath(os.path.curdir)
    imglist = get_all_image_fnames()

    dbg = dirpath
    dbg += "\nlen={}".format(len(imglist))


    templatepath = get_template_path()
    blocksize = 200

    # no need to add 1 here due to 0-indexing of blocks in the template
    blocknumber = len(imglist)//blocksize
    context = dict(imglist=imglist, dirpath=dirpath, dbg=None,
                   blocksize=blocksize, blocknumber=blocknumber)

    res = render(templatepath, context)
    # res = ""

    with open(RESULT_FNAME, "w") as resfile:
        resfile.write(res)

    print("file written: {}".format(RESULT_FNAME))


if __name__ == "__main__":
    pass
    # main()
