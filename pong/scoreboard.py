from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic") -> None:
        super().__init__(shape)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def l_player_score(self):
        self.l_score += 1
        self.update_score()
    
    def r_player_score(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(0, 200)
        self.write("-", align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))
