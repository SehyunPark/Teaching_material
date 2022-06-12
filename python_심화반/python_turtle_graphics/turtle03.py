import turtle
import math

siri = turtle.Turtle()
siri.hideturtle()
siri.color('red', 'yellow')
siri.speed(0)

siri.begin_fill()
for i in range(50):
    siri.forward(i*8)
    siri.left(170)
    siri.forward(20)

siri.end_fill()


turtle.done()