from turtle import *
from random import *

colours = ('red', 'blue', 'green', 'yellow', 'brown')
bob = Turtle()
a = bob
bob.shape('turtle')
bob.color('red')
bob.penup()
bob.goto(-300, 140)
bob.pendown()
bob.forward(300)
for a in range(6):
    bob.left(90)
    bob.forward(150)

for b in range(4):
    bob.forward(150)
    bob.left(90)


