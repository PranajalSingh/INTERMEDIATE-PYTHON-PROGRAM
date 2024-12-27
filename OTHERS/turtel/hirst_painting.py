import colorgram
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(0)
turtle.colormode(255)

def extract_colors(image):
    rgb_color = []
    img_colors = colorgram.extract(image, 30)

    for color in img_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_color.append(new_color)

    return rgb_color

colors = extract_colors('hirst_painting.jpeg')

##############################    # this part of code is responsible for starting the drawing from corner
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100



for i in range(1,num_of_dots+1):
    num_of_dots += 1
    # timmy.pendown()
    timmy.dot(20, random.choice(colors))
    # timmy.penup()
    timmy.forward(50)
    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
