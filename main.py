import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
screen.exitonclick()
