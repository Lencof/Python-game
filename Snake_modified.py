# __Author__ __Lencof__
# Snake_modified.py

import turtle
import random
import pygame

# head orientation
h = [0]

# score
a = [0]
b = [0]

# food coord
fcoord = [0,0,0]

# position
pos = []

def home(x,y): # create def home(x,y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    h[0] = 0
    fcoord[2] = 0
    pos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("black")
    turtle.goto(0,0)
    turtle.write("PLay")
    turtle.title("Snake")
    turtle.onscreenclick(start)
    turtle.mainloop()
    
def level_1(): # create def level_1():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("grey")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)
    
# before writing the code
   
