from turtle import Turtle,Screen
from ball import Ball
from bat import Bat
from dots import Dot
from scoreboard import Scoreb
import time
sc=Screen()
sc.setup(800,600)
sc.bgcolor("black")
sc.listen()
sc.tracer(0)
batl=Bat(-350,0)
batr=Bat(350,0)

sc.onkeypress(batl.up,"w")
sc.onkeypress(batl.down,"s")
sc.onkeypress(batr.up,"Up")
sc.onkeypress(batr.down,"Down") # Down arrow is used to move the right bat downwards
ball1=Ball()
d=Dot()
s1=Scoreb()
s2=Scoreb()
game_on=True
while game_on:
    time.sleep(0.1) # to adjust the speed of ball
    sc.update()
    ball1.move()
    if ball1.ycor()>280 or ball1.ycor()<-280:
        ball1.bounce_y()
    if ball1.distance(batl)<50 and ball1.xcor()<-320 or ball1.distance(batr)<50 and ball1.xcor()>320:
        ball1.bounce_x() #the ball hitted the bat
        # time.sleep(ball1.speed1)

    if ball1.xcor()>400:
        ball1.refresh()
        s1.inc_scores()
        s1.Scoreboard((-100,250))
        # time.sleep(ball1.speed1)

    if ball1.xcor()<-400:
        ball1.refresh()
        s2.inc_scores()
        s2.Scoreboard((100,250))


sc.exitonclick()