from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,location):
        super().__init__()
        self.goto(location)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.move_speed = 0.1


    def left(self):
        self.new_x = self.xcor() - 20
        self.goto(self.new_x, self.ycor())

    def right(self):
        self.new_x = self.xcor() + 20
        self.goto(self.new_x, self.ycor())