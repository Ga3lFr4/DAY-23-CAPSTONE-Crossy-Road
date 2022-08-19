from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-150, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. You made it to level {self.level}.", align=ALIGNMENT, font=FONT)

    def gain_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
