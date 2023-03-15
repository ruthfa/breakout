from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=980, height=600)
screen.bgcolor("black")
screen.title("Breakout game")
screen.tracer(0)

wall = []
colors = ["orange", "red", "green", "blue", "yellow"]
x_pos = -465
y_pos = 190
x_var = 65
y_var = 25

def create_wall():
    for a in range(5):
        for i in range(15):
            brick = Brick((x_pos + (x_var * i), y_pos - (y_var * a)), colors[a])
            wall.append(brick)

paddle= Paddle((0, -250))
ball= Ball()
scoreboard = Scoreboard()
create_wall()






screen.listen()
screen.onkey(paddle.right,"Right")
screen.onkey(paddle.left,"Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#Detect colision with the wall
    if ball.ycor() > 300:
        ball.bounce_y()

    if  ball.xcor() > 490 or ball.xcor() < -490:
        ball.bounce_x()

#Detect colision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() < -230:
        ball.bounce_y()

# Detect colision with bricks
    for brick in wall:
        if ball.distance(brick) < 40:
            brick.hideturtle()
            wall.remove(brick)
            scoreboard.increase_score()
            ball.move_speed  -= 0.001
            paddle.move_speed -= 0.001
            ball.bounce_y()
    if wall == []:
        create_wall()
        scoreboard.level_up()
        ball.move_speed = 0.1
        paddle.move_speed = 0.1

 #Detect when player fails
    if ball.ycor() < -300:
        ball.restart()
        scoreboard.decrease_lifes()
        if scoreboard.lifes == 0:
            scoreboard.game_over()
            game_is_on = False











screen.exitonclick()
