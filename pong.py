import turtle
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("light green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("DodgerBlue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pink Player: 0   Green Player: 0", align='center',font=("Courier" , 18 , "bold"))

# Timer counter
timer = turtle.Turtle()
timer.speed(0)
timer.color("white")
timer.penup()
timer.hideturtle()
timer.goto(380, 260)

# functions
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

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

start_time = time.time()

# main game loop
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 30:
        break

    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Pink Player: {}  Green Player: {}".format(score_a , score_b), align='center',font=("Courier" , 18 , "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Pink Player: {}  Green Player: {}".format(score_a , score_b), align='center',font=("Courier" , 18 , "bold"))

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    # Update timer
    remaining_time = 30 - elapsed_time
    timer.clear()
    timer.write("Time: {:.1f}".format(remaining_time), align="right", font=("Courier", 18, "bold"))

# Calculate final scores
final_score_a = score_a
final_score_b = score_b

# Determine the winner
winner = None
if final_score_a > final_score_b:
    winner = "Pink Player"
elif final_score_b > final_score_a:
    winner = "Green Player"
else:
    winner = "It's a tie"

# Display the winner
pen.clear()
pen.write("Final Score - Pink Player: {}       Green Player: {}\nWinner: {}".format(final_score_a, final_score_b, winner), align='center', font=("Courier", 18, "bold"))

# Keep the screen open until it's closed manually
wn.mainloop()
    