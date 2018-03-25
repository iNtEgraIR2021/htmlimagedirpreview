#!/usr/bin/env python3

"""
This script serves to generate a browser based preview of all images in a directory.
"""

import jinja2
from functools import partial
import inspect
import sys
import os

from ipydex import IPS


IMAGE_EXTENSIONS = [".svg", ".png", ".jpg", ".jpeg", ".gif", ".bmp"]
RESULT_FNAME = "000_preview.html"

def get_template_path():
    mod = sys.modules.get(__name__)
    if mod is not None and hasattr(mod, '__file__'):
        modpath = os.path.dirname(os.path.abspath(mod.__file__))
        templatepath = os.path.join(modpath, "templates", "base.html")
    else:
        msg = "Could not find the path of the module".fomat(__name__)
        raise ValueError(msg)

    if not os.path.isfile(templatepath):
        msg = "Could not find the template at path {}".format(templatepath)
        raise FileNotFoundError(msg)

    return templatepath


def render(tpl_path, context):
    # source: http://matthiaseisen.com/pp/patterns/p0198/
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def is_image_file(path, fname):
    if not os.path.isfile(os.path.join(path, fname)):
        return False

    for ext in IMAGE_EXTENSIONS:
        if fname.lower().endswith(ext):
            return True

def get_all_image_fnames(path="."):
    dircontent = os.listdir(path)

    imagelist = sorted(filter(partial(is_image_file, path), dircontent))

    return list(imagelist)



#app = Flask(__name__)
#@app.route('/')

def main():

    dirpath = os.path.abspath(os.path.curdir)
    imglist = get_all_image_fnames()[:30]

    dbg = dirpath
    dbg += "\nlen={}".format(len(imglist))


    #url = url_for('REPLACEME', filename=imglist[0])
    #tmp = '<img src="{}">'.format(url)
    #dbg += "\n<br>url={}".format(tmp)

    templatepath = get_template_path()
    context = dict(imglist=imglist, dirpath=dirpath, dbg=dbg)

    res = render(templatepath, context)
    #res = ""

    with open(RESULT_FNAME, "w") as resfile:
       resfile.write(res)

    print("file written: {}".format(RESULT_FNAME))

if __name__ == "__main__":
    pass
    #main()
