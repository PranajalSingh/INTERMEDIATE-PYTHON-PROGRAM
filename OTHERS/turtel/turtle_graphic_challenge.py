import turtle
from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

turn = [0, 90 , 180, 270]
timmy = Turtle()
# timmy.pensize(15)
timmy.speed(0)
turtle.colormode(255)

def draw_spiral(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spiral(5)


# for i in range(random.randint(23,100)):
#     timmy.color(random_color())
#     timmy.forward(random.randint(20,60))
#     timmy.left(random.choice(turn))

# colors = [
#       (250, 244, 248), (241, 244, 248), (236, 172, 164), (133, 223, 208),
#       (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119),
#       (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20),
#       (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29),
#       (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180),
#       (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158),
#       (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6),
#          ]
# turtle.colormode(255)