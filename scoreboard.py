from turtle import Turtle, update

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,265)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", font=("Chewy",24,"normal"), align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("GAME OVER :(", font=("Chewy",24,"normal"), align="center" )