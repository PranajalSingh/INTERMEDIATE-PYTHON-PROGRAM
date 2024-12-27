import turtle
from turtle import Turtle, Screen

colors = [
      (250, 244, 248), (241, 244, 248), (236, 172, 164), (133, 223, 208),
      (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119),
      (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20),
      (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29),
      (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180),
      (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158),
      (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6),
         ]

screen = Screen()
timmy = Turtle()
timmy.speed(0)
turtle.colormode(255)

def move_backwards():
    timmy.backward(10)
def move_forwards():
    timmy.forward(10)
def turn_left():
    timmy.left(10)
def turn_right():
    timmy.right(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()
