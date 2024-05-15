#Antone Simmons
#5/5/24
#P4Lab1A
#Turtle

import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
tri = turtle.Turtle()

for i in range(4):
    bob.forward(50)
    bob.left(90)

for i in range(3):
    tri.forward(80)
    tri.left(120)
    
wn.mainloop()
