from turtle import Turtle

FONT = ('Comic Sans MS', 14, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.print_score(self.score)

    def print_score(self, score):
        self.clear()
        text = f"Score: {self.score}"
        self.write(text, move=False, align='center', font= FONT)

    def game_over(self):
        self.goto(0,250)
        self.write(f"Game Over!",align="center",move=False, font= FONT)