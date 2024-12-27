from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE =20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_seg(pos)


    def add_seg(self, pos):
        new_seg = Turtle("circle")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.snake.append(new_seg)

    def extend(self):
        self.add_seg(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270: #down
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90: #up
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0: #right
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180: #left
            self.head.setheading(0)