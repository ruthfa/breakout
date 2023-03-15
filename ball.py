from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,-230)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0.1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_y()
