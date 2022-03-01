from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.ls = 0
        self.rs = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 210)
        self.write(f"{self.ls}", align='center', font=('Retro Gaming', 60, 'normal'))
        self.goto(100, 210)
        self.write(f"{self.rs}", align='center', font=('Retro Gaming', 60, 'normal'))

    def update_leftscore(self):
        self.ls += 1
        self.update_score()

    def update_rightscore(self):
        self.rs += 1
        self.update_score()
