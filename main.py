from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")

segment_1 = Turtle(shape="square")
segment_1.color("white")

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(x=-20, y=0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(x=-40, y=0)

screen.exitonclick()
