# __Author__ __Lencof__
# Ping_pong.py

import turtle as t
import os

# Score varibales

player_a_score = 0
player_b_score = 0

win = t.Screen() # creating a window
win.title("Ping-Pong Game") # Giving name to the game.
win.bgcolor('black') # providing color to the HomeScreen
win.setup(width=800,height=600) # Size of the game panel
win.tracer(0) # which speed up's the game

# Creating left paddie for the game

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Creating a ringht paddie for the game

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350,0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5 # Setting up the pixels for the ball movement.
all_by = 1.5

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))


#
