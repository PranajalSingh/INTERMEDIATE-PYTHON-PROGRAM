from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.new_y = None
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.goto(pos)
        self.go_up()
        self.go_down()

    def go_up(self):
        if self.ycor() < 250:
            self.new_y = self.ycor() + 28
            self.goto(self.xcor(), self.new_y)


    def go_down(self):
        if -250 < self.ycor():
            self.new_y = self.ycor() - 28
            self.goto(self.xcor(), self.new_y)



