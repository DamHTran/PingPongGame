from turtle import Turtle


class Paddle:

    def __init__(self, position):
        self.paddle = Turtle(shape='square')
        self.paddle.penup()
        self.paddle.speed('fastest')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(x=position[0], y=position[1])
        self.new_y = 0

    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)




