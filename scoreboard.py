from turtle import Turtle

FONT = ('Comic Sans MS', 14, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as HS:
            high_score = int(HS.read())
        self.high_score = high_score

        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.color("white")
        self.print_score(self.score,self.high_score)

    def print_score(self, score, highscore):
        self.clear()
        text = f"Score: {self.score}                     High Score: {self.high_score}"
        self.write(text, move=False, align='center', font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as HS:
                HS.write(str(self.high_score))
        self.score = 0
        self.print_score(self.score, self.high_score)

    def game_over(self):
      self.color("red")
      self.goto(0,0)
      self.write(f"Game Over!",align="center",move=False, font= FONT)