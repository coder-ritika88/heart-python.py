import turtle
import math
import random

# create the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("colorful heart")

# create the turtle
t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

# list of colors
colors=[
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "magenta",
    "pink",
    "white"
]

# draw the heart
for i in range(120):
    t.penup()
    t.goto(0,-40)

    angle = i * (2 * math.pi)/120

    x = 16 * (math.sin(angle)**3)
    y = (
        13*math.cos(angle)
        -5*math.cos(2*angle)
        -2*math.cos(3*angle)
    - math.cos(4*angle)
    )

    x=x*15
    y=y*15
    t.goto(x,y)
    t.color(random.choice(colors))
    t.pendown()

    for j in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()        
