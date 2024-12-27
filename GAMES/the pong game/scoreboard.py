from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner(self):
        self.goto(0,0)
        if self.l_score == 3:
            winner = "LEFT"
            self.write(f"{winner} WON", align="center", font=("courier", 20, "normal"))
            return True
        elif self.r_score == 3:
            winner = "RIGHT"
            self.write(f"{winner} WON", align="center", font=("courier", 20, "normal"))
            return True



