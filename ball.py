from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        #self.shapesize(0.5,0.5)#usually the size of a turtle object is 20X20. We are reducing it to 10X10
        self.penup()
        self.move_dist_x=10  #the distance to be moved in each step along x direction is 10 pixels
        self.move_dist_y=10

        # self.speed1=1
    def move(self):
        newx=self.xcor()+self.move_dist_x
        newy=self.ycor()+self.move_dist_y #the ball's x and y coordinates should increase by 10 pixels on
                                          #each move
        self.goto(newx,newy)
    def bounce_y(self):
        self.move_dist_y*=-1 #to reverse direction of ball along y direction(or vertical direction)
        # self.speed1*=0.5
    def bounce_x(self):
        self.move_dist_x*=-1
    def refresh(self):
        self.goto((0,0))
        self.bounce_x()
        # self.speed1=1
