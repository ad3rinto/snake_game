import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.listen()


screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
screen.exitonclick()
