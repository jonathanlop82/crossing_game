from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.goto(-220,270)
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align='center', font=FONT)

