from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.end_line = -350
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def new_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(350, random.randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
         for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def hide_cars(self):
        for car in self.cars:
            if car.xcor() < self.end_line:
                car.hideturtle()
                self.cars.remove(car)

    def extend_cars(self):
        if random.randint(1, 6) == 1:
            self.new_car()
        self.move_cars()
        self.hide_cars()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
