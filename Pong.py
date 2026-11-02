from logging import root
import turtle as t
import time
import tkinter as tk
player_a_score = 0
player_b_score = 0
bounce_num=0
speed_multiplier = 2.0
root = tk.Tk()
    


window=t.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)


leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("blue")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("red")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

ball=t.Turtle()
ball.speed(0.08)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(5,5)
ballxdirection=0.15
ballydirection=0.15

ball.setx(ball.xcor() + ballxdirection)
ball.sety(ball.ycor() + ballydirection)



pen=t.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0               Player B: 0", align="center", font=('Comic Sans', 24, 'normal'))

def lpaddleup():

    y = leftpaddle.ycor() +90
    leftpaddle.sety(min(y,250))



def rpaddleup():
   y = rightpaddle.ycor() +90
   rightpaddle.sety(min(y,250))

def lpaddledown():
    y = leftpaddle.ycor() -90
    leftpaddle.sety(max(y,-250))


def rpaddledown():
    y = rightpaddle.ycor() -90
    rightpaddle.sety(max(y,-250))

window.listen()
window.onkeypress(lpaddleup,'w')
window.onkeypress(lpaddledown,'s')
window.onkeypress(rpaddleup,'Up')
window.onkeypress(rpaddledown,'Down')




while True:
    window.update()


    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection = ballydirection * -1
        bounce_num += 1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection * -1
        bounce_num += 1



    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}               Player B: {}".format(player_a_score, player_b_score), align="center", font=('Comic Sans', 24, 'normal'))
        ballxdirection = 0.15
        ballydirection = 0.15




    if ball.xcor() < -390:
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}               Player B: {}".format(player_a_score, player_b_score), align="center", font=('Comic Sans', 24, 'normal'))
        ballxdirection = 0.15
        ballydirection = 0.15

        



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection = -ballxdirection
        bounce_num += 1

    
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50:
        ball.setx(340)
        ballxdirection = -ballxdirection
        bounce_num += 1


    if bounce_num >= 3:
        speed_multiplier *= 1.5   # Increase speed by 20%
        ballxdirection *= 1.5  # Increase horizontal speed
        ballydirection *= 1.5  # Increase vertical speed
        bounce_num = 0 
t.done()