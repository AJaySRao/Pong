from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def move(self):
        y = self.ycor() + self.y
        x = self.xcor() + self.x
        self.goto(x, y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1
        self.ball_speed *= 0.9

    def reposition(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_bounce()