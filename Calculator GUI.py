# __Author__ __Lencof__
# Calculator GUI.py
 from tkinter import *
  from operator import add, sub, mul, truediv
  
  OPFUNC = {'+': add, '-': sub, '*': mul, '/': truediv}
  
  class ParseErr(Exception):
    pass
  
  # I will continue the project
