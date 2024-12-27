from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color : ")

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(6):
      timmy = Turtle(shape = "turtle")
      timmy.color(colors[i])
      timmy.penup()
      timmy.goto(x = -230, y = y_pos[i])
      all_turtles.append(timmy)

if user_bet:
      is_race_on = True

while is_race_on:
      for turtle in all_turtles:
            if is_race_on:
                  random_distance = random.randint(0, 10)
                  turtle.forward(random_distance)
                  if turtle.xcor() > 230:
                        is_race_on = False
                        winning_turtle = turtle.pencolor()
                        if winning_turtle == user_bet:
                              print(f"you've won, The {winning_turtle} turtle is the winner.")
                        else:
                              print(f"you've lost, The {winning_turtle} turtle is the winner.")

screen.exitonclick()
