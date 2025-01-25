import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0)
screen.title("My Snake Game")



snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food = Food()
score = Scoreboard()

game_on = True

while game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10 :
        food.refresh()
        score.win()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        score.game_over()

    for segments in snake.snakes_segment[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()