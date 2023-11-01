import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
colors = ("red", "orange", "yellow", "green", "blue", "purple")
y_positions = (-60, -30, 0, 30, 60, 90)
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle_list.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {
                      winning_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
