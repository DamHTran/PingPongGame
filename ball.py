from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        new_y = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y)

