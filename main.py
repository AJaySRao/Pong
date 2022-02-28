from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
import turtle
import random

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong')
s.tracer(0)

# turtle.colormode(255)
# t = Turtle()
# t.penup()
# t.setheading(90)
# t.forward(280)
# t.setheading(270)
#
# for i in range(30):
#     t.dot(15, (255, 255, 255))
#     t.shapesize(stretch_wid=2, stretch_len=0.5)
#     t.forward(20)

p1 = Paddle(360)
p2 = Paddle(-360)
b = Ball()


s.listen()
s.onkey(key='Up', fun=p1.move_up)
s.onkey(key='w', fun=p2.move_up)
s.onkey(key='Down', fun=p1.move_down)
s.onkey(key='s', fun=p2.move_down)

game = True

while game:
    s.update()
    time.sleep(0.1)
    b.move()

    if b.ycor() > 280 or b.ycor() < -280:
        b.w_bounce()

    if b.distance(p1) < 50 and b.xcor() > 340 or b.distance(p2) < 50 or b.xcor() < -340:
        b.p_bounce()

    if b.xcor() > 395 or b.xcor() < -385:
        game = False

s.exitonclick()