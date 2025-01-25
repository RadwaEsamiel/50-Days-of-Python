from turtle import Turtle

position_list = [(0, 0), (-10, 0), (-20, 0), (-30, 0)]
DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    def __init__(self):
        self.new_turtle = None
        self.snakes_segment = []
        self.add_new_snake()
        self.head = self.snakes_segment[0]


    def add_new_snake(self):
        for snake_position in position_list:
            self.create_snake(snake_position)


    def create_snake(self,snake_position):
            self.new_turtle = Turtle()
            self.new_turtle.color("white")
            self.new_turtle.shape("square")
            self.new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.new_turtle.penup()
            self.new_turtle.goto(snake_position)
            self.snakes_segment.append(self.new_turtle)

    def extend(self):
        self.create_snake(self.snakes_segment[-1].position())


    def move(self):
        for x in range(len(self.snakes_segment) -1 , 0 ,-1) :
            new_x = self.snakes_segment[x - 1].xcor()
            new_y = self.snakes_segment[x - 1].ycor()
            self.snakes_segment[x].goto(new_x,new_y)

        self.head.forward(DISTANCE)


    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)






