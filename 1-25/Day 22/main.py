import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreborad import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()



right_paddle = Paddle(350)
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

left_paddle = Paddle(-350)
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = Ball(0,0)

game_on = True
screen.tracer(0)
score = Score()

while game_on :
    time.sleep(0.1)
    screen.update()
    ball.move()
    score.score_update()
    if ball.ycor() >= 285 or ball.ycor() <= -285 :
        ball.bounce_walls()

    if (ball.xcor() > 330 and ball.distance(right_paddle) < 50) or (ball.xcor() < -330 and ball.distance(left_paddle) < 50):
        ball.bounce_paddles()

    if ball.xcor() >= 380 :
        ball.reset_position()
        score.r_point()

    if ball.xcor() <= -380 :
        ball.reset_position()
        score.l_point()





screen.exitonclick()