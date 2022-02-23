import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
guess = screen.textinput(title="Turtle race by kio, 21Feb2022", prompt="Guess what color of turtle wins? Make your bet ! : ")
turtle_num = 7
color = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
all_turtles = []

for num in range(turtle_num):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[num])
    new_turtle.pu()
    new_turtle.setpos(x=-240, y=(400 / 2) - 20 - ((int(380 / turtle_num)) * num))
    all_turtles.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:
    pick_turtle = random.randint(0,turtle_num-1)
    all_turtles[pick_turtle].forward(random.randint(0,5))
    if all_turtles[pick_turtle].xcor() >= (500/2-10):
        is_race_on = False
        winner_turtle = all_turtles[pick_turtle].pencolor()

if guess == winner_turtle:
    print(f"You win! the winner turtle is {winner_turtle}.")
else:
    print(f"You lose! the winner turtle is {winner_turtle}.")


screen.exitonclick()

