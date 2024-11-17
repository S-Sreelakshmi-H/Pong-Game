from turtle import Turtle
from ball import Ball
class Scoreb(Turtle):
    def __init__(self):
        super().__init__()
        self.scores=0
        self.color("white")
    def inc_scores(self):
        self.scores+=1
    def Scoreboard(self,postn):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(postn)
        self.write(f"{self.scores}",False,"left",("Arial",24,"bold"))