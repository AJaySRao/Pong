from turtle import Turtle


class Separate(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.forward(300)
        self.setheading(270)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=2)

        for i in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
