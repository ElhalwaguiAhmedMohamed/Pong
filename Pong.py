import turtle
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)                           #To stop the window from updating to make the game faster

score_a = 0
score_b = 0


#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)



#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)



#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("player_A = 0 | player_B = 0",align="center",font="courier")


#paddle_movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")






while (True):             #Main game loop
    wn.update()
    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #collision
    if (ball.ycor() > 290):
        ball.sety(288)
        ball.dy *= -1
    
    if (ball.ycor() < -290):
        ball.sety(-288)
        ball.dy *= -1
    if (ball.xcor() > 400):
        ball.goto(0,0)
        score_a += 1
        pen.clear()
        pen.write("player_A = {} | player_B = {}".format(score_a,score_b),align="center",font="courier")
    if (ball.xcor() < -400):
        ball.goto(0,0)
        score_b += 1
        pen.clear()
        pen.write("player_A = {} | player_B = {}".format(score_a,score_b),align="center",font="courier")
    #ball & paddle_b collision
    if (ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor()+25) and (ball.ycor() > paddle_b.ycor()-25) and (ball.xcor() < 350) :
        ball.setx(340)
        ball.dx *= -1    
    #ball & paddle_a collision
    if (ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor()+25) and (ball.ycor() > paddle_a.ycor()-25) and (ball.xcor() > -350) :
        ball.setx(-340)
        ball.dx *= -1 
    if (score_a == 5) or (score_b == 5):
        break
