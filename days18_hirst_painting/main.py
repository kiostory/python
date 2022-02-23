import random
from turtle import Turtle, Screen
import colorgram
import turtle
turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
picked_color = []
for i in colorgram.extract('aaa.jpg', 5):
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color = (r,g,b)
    picked_color.append(color)

for y in range(-250,250,50):
    for x in range(-350,400,50):
        tim.pu()
        tim.setposition(x,y)
        tim.dot(20,random.choice(picked_color))

tim.hideturtle()
screen = Screen()
screen.exitonclick()
