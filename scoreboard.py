from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(-15, 260)
        self.lifes = 3
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level} Score: {self.score} Lives: {self.lifes}", align= ALIGNMENT, font= FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def decrease_lifes(self):
        self.lifes -= 1
        self.clear()
        self.update_scoreboard()

    def level_up(self):
        self.level +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align= "center", font= FONT)