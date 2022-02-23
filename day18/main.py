import random
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")

def pen_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color = (R,G,B)
    return color

def draw_spirograph(gap):
    heading = 0
    while heading < 360:
        tim.color(pen_color())
        tim.setheading(heading)
        tim.circle(200)
        heading += gap

draw_spirograph(7)

screen = Screen()
screen.exitonclick()
