from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos, 0)

    def move_up(self):
        y = self.ycor()
        if y < 230:
            self.sety(y+10)

    def move_down(self):
        y = self.ycor()
        if y > -230:
            self.sety(y-10)
