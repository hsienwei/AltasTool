from distutils.core import setup
import py2exe

setup(windows=["convert_png_ui.py"] ,
      options = { 
                  "py2exe": { "includes": ["Tkinter"],
                              "packages":"encodings"} })