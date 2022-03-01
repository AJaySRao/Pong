from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from separate import Separate


s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong')
s.tracer(0)

p1 = Paddle(360)
p2 = Paddle(-360)
b = Ball()
score = ScoreBoard()
line = Separate()


s.listen()
s.onkey(key='Up', fun=p1.move_up)
s.onkey(key='w', fun=p2.move_up)
s.onkey(key='Down', fun=p1.move_down)
s.onkey(key='s', fun=p2.move_down)

game = True

while game:
    time.sleep(b.ball_speed)
    s.update()
    b.move()

    #when the ball touches the above wall it bounces back in opp direction
    if b.ycor() > 280 or b.ycor() < -280:
        b.y_bounce()

    #when a paddle hit the ball it bounces back in opp direction
    if b.distance(p1) < 60 and b.xcor() > 330 or b.distance(p2) < 60 and b.xcor() < -330:
        b.x_bounce()

    #Right paddle miss
    if b.xcor() > 380:
        b.reposition()
        score.update_leftscore()

    #Left paddle miss
    if b.xcor() < -395:
        b.reposition()
        score.update_rightscore()

s.exitonclick()