import turtle
import math

tt = turtle.Turtle()

def polygon(side, length):
    angle = 360 / side
    for n in range(side):
        tt.fd(length)
        tt.left(angle)

def square(length):
    polygon(4, length)

def circle(r):
    c = 2 * math.pi * r
    side = int(c / 3)
    length = c / side
    polygon(side, length)

square(100)
polygon(6, 100)
circle(100)
