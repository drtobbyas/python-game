import turtle
import os

window = turtle.Screen()
window.title('Pong Game @drtobbyas')
window.bgcolor('black')

window_width = 800
window_height = 600

window.setup(width=window_width, height=window_height)
window.tracer(0)


paddle_offset = 50


# paddle a 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto((-(window_width / 2) + paddle_offset), 0)


# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(((window_width / 2) - paddle_offset), 0)

# ball
ball_width = 20
ball_height = 20

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0, 0)

ball.dx = 0.05
ball.dy = 0.05

# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (window_height / 2) - paddle_offset)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
 
player_a_score = 0
player_b_score = 0


def paddle_a_up(): 
    y = paddle_a.ycor()
    y += 20
    if y <= (window_height / 2) - 50:
      paddle_a.sety(y)
    
def paddle_a_down(): 
    y = paddle_a.ycor()
    y -= 20
    if y >= -(window_height / 2) + 50: 
      paddle_a.sety(y)

def paddle_b_up(): 
    y = paddle_b.ycor()
    y += 20
    if y <= (window_height / 2) - 50:
      paddle_b.sety(y)
    
def paddle_b_down(): 
    y = paddle_b.ycor()
    y -= 20
    if y >= -(window_height / 2) + 50: 
      paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > (window_height / 2) - (ball_height / 2):
        ball.sety((window_height / 2) - (ball_height / 2))
        ball.dy *= -1

    if ball.ycor() < -(window_height / 2) + (ball_height / 2):
        ball.sety(-(window_height / 2) + (ball_height / 2))
        ball.dy *= -1

        

    if ball.xcor() > (window_width / 2) - (ball_width / 2):
        # ball.setx((window_width / 2) - (ball_width / 2))
        ball.goto(0,0)
        player_a_score += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -(window_width / 2) + (ball_width / 2):
        # ball.setx(-(window_width / 2) + (ball_width / 2))
        ball.goto(0,0)
        player_b_score += 1
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Courier", 24, "normal"))


    # paddle collision  
    if ball.xcor() < (-(window_width / 2) + paddle_offset + (ball_width / 2)) and ball.ycor() < paddle_a.ycor() + paddle_offset and ball.ycor() > paddle_a.ycor() - paddle_offset:
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > (window_width / 2) - paddle_offset - (ball_width / 2) and ball.ycor() < paddle_b.ycor() + paddle_offset and ball.ycor() > paddle_b.ycor() - paddle_offset:
        ball.dx *= -1
        os.system("aplay bounce.wav&")
