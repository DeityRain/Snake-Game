from turtle import Turtle

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(2)
        self.pencolor("Gray10")
        self.penup()
        self.goto(-310,310)
        self.pendown()
        for _ in range(4):
            self.forward(620)
            self.right(90)

