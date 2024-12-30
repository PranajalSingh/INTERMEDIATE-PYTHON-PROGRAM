from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh()
scoreboard = Scoreboard()
scoreboard.title_frame()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    # detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 270 or snake.head.ycor() < -290):
        snake.reset_snake()
        scoreboard.reset_score()
        # game_is_on = False
        # scoreboard.game_over()

    # collision with tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 1:
            snake.reset_snake()
            scoreboard.reset_score()
            # game_is_on = False
            # scoreboard.game_over()

screen.exitonclick()