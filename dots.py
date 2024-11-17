from turtle import Turtle
class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0,280))
        self.right(90)
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
