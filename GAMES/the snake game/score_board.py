from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 278)
        self.hideturtle()
        self.dot = Turtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        self.title_frame()

    def title_frame(self):
        self.dot.hideturtle()
        self.dot.pencolor("white")
        self.dot.pensize(5)
        self.dot.color("white")
        self.dot.penup()
        self.dot.goto(300, 275)
        self.dot.pendown()
        self.dot.backward(591)
        self.dot.penup()
        self.dot.backward(2)
        self.dot.pendown()
        self.dot.right(90)
        self.dot.pensize(1)
        self.dot.forward(600)