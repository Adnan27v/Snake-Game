from turtle import Screen
import time
from snake import Snake

screen = Screen()

screen.setup(width= 600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.update()

snake = Snake()

screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")

game_over = False

while  not game_over:

    snake.move()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()