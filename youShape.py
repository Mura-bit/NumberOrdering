import turtle
import random

turtle.speed(0)

def drawStar(sideLen, color):
    turtle.color(color)
    for _ in range (5):
        turtle.forward(sideLen)
        turtle.right(144)

turtle.pensize(5)
len = 50 
for color in ["black", "red", "yellow", "green", "purple"]:
    drawStar(len, color)
    len += 50

turtle.done()