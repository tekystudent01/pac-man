import turtle
import time
screen = turtle.Screen()
screen.bgcolor('white')
turtle.color('blue')
turtle.penup()
turtle.pensize(5)
turtle.goto(-130,50)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.color('black')
turtle.goto(0,50)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.color('red')
turtle.goto(130,50)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.color('yellow')
turtle.goto(-65,0)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.color('green')
turtle.goto(65,0)
turtle.pendown()
turtle.circle(50)
time.sleep(15)