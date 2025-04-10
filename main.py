from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()

screen.setup(width= 600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.update()

snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

game_over = False
scoreboard = Scoreboard()

while  not game_over:

    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.print_score(scoreboard.score)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()