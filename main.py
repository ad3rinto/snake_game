import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.listen()

screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_scores()
        food.refresh()

    # detect collision with wall
    if snake.segments[0].xcor() > 420 or snake.segments[0].xcor() < -420 or snake.segments[0].ycor() > 420 or snake.segments[0].ycor() < -420:
        game_on = False
        scoreboard.game_over()

    # detect colission with own tail
    # lenght_of_snake = len(snake.segments)
    # for i in range(lenght_of_snake):
    #     if snake.segments[0].distance(snake.segments[i]) < 15:
    #         game_on = False
    #         scoreboard.game_over()


screen.exitonclick()
