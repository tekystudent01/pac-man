from random import choice
from turtle import *
import turtle as player
from freegames import floor, vector
playerspeed = 50
screen = player.Screen()
screen.setup(600,600)
screen.bgpic('D:\\PHUC GIA in p1\\python\\SNLTW\\hp2\\lesson7\\R.gif')
screen.addshape('D:\\PHUC GIA in p1\\python\\SNLTW\\hp2\\lesson7\\pac-man.gif')
player.shape('D:\\PHUC GIA in p1\\python\\SNLTW\\hp2\\lesson7\\pac-man.gif')
#player.onkeypress(for)
screen.update()
screen.exitonclick()
def moveLeft():
    x = player.xcor()
    x -= playerspeed
    if x < -200:
        x = -200
    player.setx(x)
def moveRight():
    x = player.xcor()
    x += playerspeed
    if x > 200():
        x =200
    player.setx(x)
moveLeft()