from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win a race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, 125 - i*50)
    tim.color(colors[i])
    turtles.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for i in turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        i.forward(randint(0,10))


screen.exitonclick()
