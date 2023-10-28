import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segment_1 = Turtle(shape="square")
segment_1.color("white")
segment_1.penup()

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.penup()
segment_2.goto(x=-20, y=0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.penup()
segment_3.goto(x=-40, y=0)

screen.update()

segments = [segment_1, segment_2, segment_3]
game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()
