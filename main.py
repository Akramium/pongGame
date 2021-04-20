from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # detect collision with walls:
    if ball.ycor() >= 290 or ball.ycor() <= - 290:
        ball.bounce_y()
    # detect collision with paddles:
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    # when right paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
    # when left paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
