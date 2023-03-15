from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.color(color)

