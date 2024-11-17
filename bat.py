from turtle import Turtle
class Bat(Turtle):
    def __init__(self,xcord,ycord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        # self.left(90)
        self.y=ycord
        self.x=xcord
        self.goto(xcord,ycord)
    def up(self):
        self.y=self.y+20
        self.goto(self.x,self.y)
    def down(self):
        self.y = self.y - 20
        self.goto(self.x,self.y)
        # self.backward(60)
