from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos, 0)

    def move_up(self):
        y = self.ycor()
        if y < 240:
            self.sety(y + 20)

    def move_down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - 20)
