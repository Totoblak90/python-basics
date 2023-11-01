from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle_r.go_up)
screen.onkey(key="Down", fun=paddle_r.go_down)
screen.onkey(key="w", fun=paddle_l.go_up)
screen.onkey(key="s", fun=paddle_l.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    
    if ball.xcor() < -320 and  ball.distance(paddle_l) < 50 or ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_player_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_player_score()
        ball.reset_position()

screen.exitonclick()
