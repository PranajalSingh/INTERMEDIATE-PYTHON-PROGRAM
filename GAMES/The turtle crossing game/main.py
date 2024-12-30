from turtle import Turtle, Screen
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("THE TURTLE CROSSING GAME")
screen.tracer(0)

timmy = Turtle()
timmy.penup()
timmy.shape("turtle")
timmy.color("white")
timmy.setheading(90)
timmy.goto(0,-230)

cars = Cars()
scoreboard = Scoreboard()

def move():
    timmy.forward(10)

screen.listen()
screen.onkey(move, "Up")

sleep_duration = 0.1

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(sleep_duration)
    cars.is_new()
    cars.move()

    if timmy.ycor() >= 230:
        timmy.goto(0,-230)
        sleep_duration *= 0.95
        scoreboard.inc_score()

    for car in cars.cars_list:
        y = car.ycor()
        x = car.xcor()
        if x <= -430:
            cars.remove(car)

        if y - 20 < timmy.ycor() < y + 20 and timmy.distance(car) < 30:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()