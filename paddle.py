from turtle import Turtle

POSITIONS = [[350, 0], [-350, 0]]
PADDLES = []


class Paddle:

    def __init__(self):
        for i in range(2):
            self.paddle = Turtle(shape='square')
            self.paddle.penup()
            self.paddle.speed('fastest')
            self.paddle.color('white')
            self.paddle.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle.goto(x=POSITIONS[i][0], y=POSITIONS[i][1])
            PADDLES.append(self.paddle)
            self.new_y = 0

    def paddle_1_go_up(self):
        self.new_y = PADDLES[0].ycor() + 20
        PADDLES[0].goto(PADDLES[0].xcor(), self.new_y)

    def paddle_1_go_down(self):
        self.new_y = PADDLES[0].ycor() - 20
        PADDLES[0].goto(PADDLES[0].xcor(), self.new_y)

    def paddle_2_go_up(self):
        self.new_y = PADDLES[1].ycor() + 20
        PADDLES[1].goto(PADDLES[1].xcor(), self.new_y)

    def paddle_2_go_down(self):
        self.new_y = PADDLES[1].ycor() - 20
        PADDLES[1].goto(PADDLES[1].xcor(), self.new_y)



