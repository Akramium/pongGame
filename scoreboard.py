from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.l_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()
