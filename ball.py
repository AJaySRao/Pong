from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x = 10
        self.y = 10

    def move(self):
        y = self.ycor() + self.y
        x = self.xcor() + self.x
        self.goto(x, y)

    def w_bounce(self):
        self.y *= -1

    def p_bounce(self):
        self.x *= -1
