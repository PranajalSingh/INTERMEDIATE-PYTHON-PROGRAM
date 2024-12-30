import turtle
from turtle import Turtle
import random

colors = [
      (250, 244, 248), (241, 244, 248), (236, 172, 164), (133, 223, 208),
      (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119),
      (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20),
      (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29),
      (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180),
      (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158),
      (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6),
         ]
turtle.colormode(255)

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.is_new_list = [True, False, False, False, False]
        self.hideturtle()

    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(colors))
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.penup()
        car.goto(430,random.randint(-200,200))
        car.setheading(180)
        self.cars_list.append(car)

    def move(self):
        for cars in self.cars_list:
            cars.forward(10)

    def remove(self, car):
        del self.cars_list[0]

    def is_new(self):
        if random.choice(self.is_new_list):
            self.new_car()

