from turtle import Turtle, Screen
import time
from snake_class import Snake
from detect_food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score  = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15 :
        food.refresh()
        score.win()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        score.GAME_OVER()

    for seg in snake.segments[1:] :
        if snake.head.distance(seg) < 10 :
                game_on = False
                score.GAME_OVER()


screen.exitonclick()