from turtle import Turtle

NO_SEGMENTS = [1,2,3]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x=0
        for _ in range(len(NO_SEGMENTS)):
            t = Turtle()
            t.shape("square")
            t.color("white")
            self.segments.append(t)
            t.penup()
            t.goto(x=x,y=0)
            x -= 20

    def move(self):
        for i in range(len(NO_SEGMENTS) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)