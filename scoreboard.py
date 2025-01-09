from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.pu()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-260, 260)
        self.level_write()

    def level_write(self):
        self.write(f"Level: {self.level}", font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.level_write()

    def game_over(self):
        #self.clear()
        self.goto(0,0)
        self.write(f"Game Over!",align='center',font=FONT)

