import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

x_cord = 0
sleep_duration = 0.1
game_on = True
while game_on:
    time.sleep(sleep_duration)

    if scoreboard.winner():
        game_on = False
    else:
        screen.update()
        ball.move()


        # collision with top/bottom walls
        if ball.ycor() > 280 or ball.ycor() < -275:
            ball.bounce()

        # collision with paddles
        if ball.xcor() > x_cord and 330 <= ball.xcor() <= 340 and ball.distance(r_paddle) < 50 or ball.xcor() < x_cord and -340 <= ball.xcor() <= -330 and ball.distance(l_paddle) < 50:
            ball.paddle_bounce()
            sleep_duration *= 0.95

        # detect r_paddle miss
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
            sleep_duration = 0.1

        # detect l_paddle miss
        elif ball.xcor() < -390:
            ball.reset_position()
            scoreboard.r_point()
            sleep_duration = 0.1

        x_cord = ball.xcor()



screen.exitonclick()