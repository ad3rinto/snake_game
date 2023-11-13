import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



# with open("my_file.txt",mode="a" ) as file:
#     file.write("MY NEW NAME IS CAPTAIN Brazillia")


screen = Screen()
screen.listen()

screen.setup(width=600, height=600)
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
        snake.extend()

    # detect collision with wall
    if snake.segments[0].xcor() > 420 or snake.segments[0].xcor() < -420 or snake.segments[0].ycor() > 420 or snake.segments[0].ycor() < -420:
        game_on = False
        scoreboard.reset_game()

    # detect collision with own tail
    lenght_of_snake = len(snake.segments)
    for i in range(lenght_of_snake):
        if i == 0:
            pass
        elif snake.segments[0].distance(snake.segments[i]) < 15:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
