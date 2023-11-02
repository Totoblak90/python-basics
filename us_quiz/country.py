from turtle import Turtle

class Country(Turtle):
    def __init__(self, country_name, x_coord, y_coord) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=x_coord, y=y_coord)
        self.write(arg=country_name, align="center", font=("Arial", 8, "normal"))