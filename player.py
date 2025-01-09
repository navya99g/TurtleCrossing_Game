from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.setheading(90)
        self.start_pos()

    def start_pos(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.start_pos()
            return True
        else:
            return False


