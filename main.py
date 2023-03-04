import time
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


paddle = Paddle()

screen.listen()
screen.onkey(paddle.paddle_1_go_up, "Up")
screen.onkey(paddle.paddle_1_go_down, "Down")
screen.onkey(paddle.paddle_2_go_up, "w")
screen.onkey(paddle.paddle_2_go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()






screen.exitonclick()