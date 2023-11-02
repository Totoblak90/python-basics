import turtle
from country import Country
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

us_df = pd.read_csv("50_states.csv")

score = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name? ")
    if answer_state is None:
        game_is_on = False
    elif score == 50:
        turtle.write(arg="You win!", align="center", font=("Courier", 24, "normal"))
    else:
        filtered_state = us_df[us_df["state"] == answer_state.title()]
        if len(filtered_state):
            score += 1
            state_name: str = filtered_state["state"].iloc[0]
            x_coord = int(filtered_state["x"].iloc[0])
            y_coord = int(filtered_state["y"].iloc[0])
            country = Country(state_name.lower(), x_coord, y_coord)
