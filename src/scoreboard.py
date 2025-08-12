from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("./data.txt") as data:
            saving = int(data.read())
        self.high_score = saving
        self.penup()
        self.goto(x=0, y=312)
        self.score = 0
        self.color("Gray10")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()
        
