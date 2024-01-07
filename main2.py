import random
import turtle
import arcade
sould = arcade.load_sound('D:\\newmain\\we-wish-you-a-merry-christmas-with-lyrics-christmas-carol-and-song.mp3')
arcade.play_sound(sould)
screen = turtle.Screen()
screen.setup(1350,790)
screen.bgpic('abc.gif')
turtle.pensize(3)
turtle.speed(4000)
def snowRain():
    for funa in range(0,5):
        b = random.randrange(1,4)
        if(b == 1):
            turtle.color('red')
        elif(b == 2):
            turtle.color('blue')
        elif(b == 3):
            turtle.color('white')
        turtle.penup()
        turtle.goto(random.randint(-300,300),random.randint(-300,300))
        a = random.randint(10,100)+10
        c = random.randint(10,50)
        turtle.pendown()
        for snow1 in range(0,8):
            turtle.forward(a)
            turtle.backward(a*0.3)
            turtle.left(45)
            turtle.pendown()
            turtle.forward((a*0.3)/2)
            turtle.backward((a*0.3)/2)
            turtle.right(90)
            turtle.forward((a*0.3)/2)
            turtle.backward((a*0.3)/2)
            turtle.left(45)
            turtle.backward(a*0.7)
            turtle.left(45)
        turtle.penup()
        turtle.goto(random.randint(-300,300),random.randint(-300,300))
        turtle.pendown()
        for snow2 in range(0,8):
            turtle.forward(c)
            turtle.backward(c*0.3)
            turtle.left(45)
            turtle.pendown()
            turtle.forward((c*0.3)*2+5)
            turtle.backward((c*0.3)*2+5)
            turtle.right(90)
            turtle.forward((c*0.3)*2+5)
            turtle.backward((c*0.3)*2+5)
            turtle.left(45)
            turtle.backward(c*0.7)
            turtle.left(45)
        turtle.penup
        turtle.goto(random.randint(-300,300),random.randint(-300,300))
        turtle.pendown()
def addText(messasage,color,x,y,size):
    turtle.pendown()
    turtle.goto(x,y)
    turtle.penup()
    turtle.color(color)
    style = ('Courier',size,'italic')
    turtle.write(messasage,font = style, align = 'center')
addText("Marry Christmas","#FD151B",0,0,40)
addText("Wonderfull Christmas","#CBF3F0",0,-30,20)
snowRain()
screen.update()
screen.exitonclick()