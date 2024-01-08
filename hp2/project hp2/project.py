from random import choice
from turtle import *
import arcade
import turtle
from freegames import floor, vector
playerspeed = 50
#sould = arcade.load_sound('D:\PHUC GIA in p1\python\SNLTW\hp2\project hp2\man-theme-remix-by-arsenic1987.mp3')
#arcade.play_sound(sould)
pacman = turtle.Turtle()
ghost1 = turtle.Turtle()
ghost2 = turtle.Turtle()
ghost3 = turtle.Turtle()
ghost4 = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
screen.bgpic('D:\hp2\project hp2\R.gif')
screen.addshape('pac-man.gif')
turtle.shape('pac-man.gif')
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