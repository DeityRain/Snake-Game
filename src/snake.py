from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.all_bodypart = []
        self.create_snake()
        self.head = self.all_bodypart[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            #time.sleep(0.13)
            self.add_part(position)
    
    
    def add_part(self, position):
        body_part = Turtle(shape="square")
        body_part.color("Gray10")
        body_part.penup()
        body_part.goto(position)
        self.all_bodypart.append(body_part)

    def reset(self):
        for seg in self.all_bodypart:
            seg.hideturtle()
        self.all_bodypart.clear()
        self.create_snake()
        self.head = self.all_bodypart[0]



    def extend(self):
        self.add_part(self.all_bodypart[-1].position())
    
    def move(self):
            for part_num in range(len(self.all_bodypart) - 1, 0, -1):
                new_x = self.all_bodypart[part_num -1].xcor()
                new_y = self.all_bodypart[part_num -1].ycor()
                self.all_bodypart[part_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)