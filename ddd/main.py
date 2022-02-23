import random
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")

for poly in range(3, 11):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.pencolor(R, G, B)
    for _ in range(poly):
        tim.forward(100)
        tim.right(360 / poly)`

screen = Screen()
screen.exitonclick()