#Antone Simmons
#5/5/24
#P4Lab1B
#Initials

import turtle
from turtle import *

  

a = turtle.Turtle()
a.color('blue')
a.pensize(5)

a.penup()
a.goto(-250,100)
a.pendown()

a.forward(80)
a.right(45)
a.forward(50)
a.backward(100)

a.right(90)
a.forward(100)

b = turtle.Turtle()
b.color('green')
b.pensize(5)

b.penup()
b.goto(100, 0)
b.pendown()

b.forward(30)
b.backward(30)

b.forward(40)
b.circle(50, 180)
b.circle(-50, 180)
b.forward(40)
