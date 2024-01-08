from random import choice
from turtle import *
import arcade
import turtle
from freegames import floor, vector
turtle.penup() 
playerspeed = 5
screen = turtle.Screen()
screen.screensize(1000,500)
screen.setup(600,600)
screen.bgpic('D:\pac-man\R.gif')
screen.addshape('D:\pac-man\s.gif')
turtle.shape('D:\pac-man\s.gif')
def eaten():
    screen
def moveLeft():
    x = turtle.xcor()
    x -= playerspeed
    if x < -200:
        x = -200
    turtle.setx(x)
def moveRight():
    x = turtle.xcor()
    x += playerspeed
    if x > 200:
        x =200
    turtle.setx(x)
def moveUp():
    y = turtle.ycor()
    y += playerspeed
    if y > 200:
        y =200
    turtle.sety(y)
def moveDown():
    y = turtle.ycor()
    y -= playerspeed
    if y < -200:
        y = -200
    turtle.sety(y)
screen.update()
screen.onkeypress(moveLeft,"Left")
screen.onkeypress(moveRight,"Right")
screen.onkeypress(moveUp,"Up")
screen.onkeypress(moveDown,"Down")
screen.listen()
screen.mainloop()
screen.exitonclick()