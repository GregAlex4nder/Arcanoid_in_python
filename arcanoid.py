#Druga gra, własny projekt
import turtle
import time

wn = turtle.Screen()
wn.title("Arcanoid by @G.W.")
wn.bgcolor('black')
wn.setup(width=1200, height=800)
wn.tracer(0)

# Życia i punkty:
life = 30
y = 0


# Funkcje

def hit_1(x,y):
    if (ball.xcor() >= x.xcor() - 60 and (ball.xcor() <= x.xcor() + 60)) and (ball.ycor() == 350):
        ball.sety(350)
        ball.dy *= -1
        x.goto(2000, 2000)
        y += 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))

def hit_2(x,y):
    if (ball.xcor() >= x.xcor() - 60 and (ball.xcor() <= x.xcor() + 60)) and (ball.ycor() == 280):
        ball.sety(280)
        ball.dy *= -1
        x.goto(2000, 2000)
        y += 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))
    if (ball.xcor() >= x.xcor() - 60 and (ball.xcor() <= x.xcor() + 60)) and (ball.ycor() == 320):
        ball.sety(320)
        ball.dy *= -1
        x.goto(2000, 2000)
        y += 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))
def hit_3(x,y):
    if (ball.xcor() >= x.xcor() - 60 and (ball.xcor() <= x.xcor() + 60)) and (ball.ycor() == 210):
        ball.sety(210)
        ball.dy *= -1
        x.goto(2000, 2000)
        y += 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))
    if (ball.xcor() >= x.xcor() - 60 and (ball.xcor() <= x.xcor() + 60)) and (ball.ycor() == 250):
        ball.sety(250)
        ball.dy *= -1
        x.goto(2000, 2000)
        y += 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))
# Paletka

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=0.5, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# Piłka
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Klocki
# Rząd nr 1
block_1 = turtle.Turtle()
block_1.speed(0)
block_1.shape('square')
block_1.color('white')
block_1.shapesize(stretch_wid=2, stretch_len=4)
block_1.penup()
block_1.goto(-540, 370)

block_2 = turtle.Turtle()
block_2.speed(0)
block_2.shape('square')
block_2.color('white')
block_2.shapesize(stretch_wid=2, stretch_len=4)
block_2.penup()
block_2.goto(-420, 370)

block_3 = turtle.Turtle()
block_3.speed(0)
block_3.shape('square')
block_3.color('white')
block_3.shapesize(stretch_wid=2, stretch_len=4)
block_3.penup()
block_3.goto(-300, 370)

block_4 = turtle.Turtle()
block_4.speed(0)
block_4.shape('square')
block_4.color('white')
block_4.shapesize(stretch_wid=2, stretch_len=4)
block_4.penup()
block_4.goto(-180, 370)

block_5 = turtle.Turtle()
block_5.speed(0)
block_5.shape('square')
block_5.color('white')
block_5.shapesize(stretch_wid=2, stretch_len=4)
block_5.penup()
block_5.goto(-60, 370)

block_6 = turtle.Turtle()
block_6.speed(0)
block_6.shape('square')
block_6.color('white')
block_6.shapesize(stretch_wid=2, stretch_len=4)
block_6.penup()
block_6.goto(60, 370)

block_7 = turtle.Turtle()
block_7.speed(0)
block_7.shape('square')
block_7.color('white')
block_7.shapesize(stretch_wid=2, stretch_len=4)
block_7.penup()
block_7.goto(180, 370)

block_8 = turtle.Turtle()
block_8.speed(0)
block_8.shape('square')
block_8.color('white')
block_8.shapesize(stretch_wid=2, stretch_len=4)
block_8.penup()
block_8.goto(300, 370)

block_9 = turtle.Turtle()
block_9.speed(0)
block_9.shape('square')
block_9.color('white')
block_9.shapesize(stretch_wid=2, stretch_len=4)
block_9.penup()
block_9.goto(420, 370)

block_10 = turtle.Turtle()
block_10.speed(0)
block_10.shape('square')
block_10.color('white')
block_10.shapesize(stretch_wid=2, stretch_len=4)
block_10.penup()
block_10.goto(540, 370)

# Rząd nr 2
block_11 = turtle.Turtle()
block_11.speed(0)
block_11.shape('square')
block_11.color('white')
block_11.shapesize(stretch_wid=2, stretch_len=4)
block_11.penup()
block_11.goto(-540, 300)

block_12 = turtle.Turtle()
block_12.speed(0)
block_12.shape('square')
block_12.color('white')
block_12.shapesize(stretch_wid=2, stretch_len=4)
block_12.penup()
block_12.goto(-420, 300)

block_13 = turtle.Turtle()
block_13.speed(0)
block_13.shape('square')
block_13.color('white')
block_13.shapesize(stretch_wid=2, stretch_len=4)
block_13.penup()
block_13.goto(-300, 300)

block_14 = turtle.Turtle()
block_14.speed(0)
block_14.shape('square')
block_14.color('white')
block_14.shapesize(stretch_wid=2, stretch_len=4)
block_14.penup()
block_14.goto(-180, 300)

block_15 = turtle.Turtle()
block_15.speed(0)
block_15.shape('square')
block_15.color('white')
block_15.shapesize(stretch_wid=2, stretch_len=4)
block_15.penup()
block_15.goto(-60, 300)

block_16 = turtle.Turtle()
block_16.speed(0)
block_16.shape('square')
block_16.color('white')
block_16.shapesize(stretch_wid=2, stretch_len=4)
block_16.penup()
block_16.goto(60, 300)

block_17 = turtle.Turtle()
block_17.speed(0)
block_17.shape('square')
block_17.color('white')
block_17.shapesize(stretch_wid=2, stretch_len=4)
block_17.penup()
block_17.goto(180, 300)

block_18 = turtle.Turtle()
block_18.speed(0)
block_18.shape('square')
block_18.color('white')
block_18.shapesize(stretch_wid=2, stretch_len=4)
block_18.penup()
block_18.goto(300, 300)

block_19 = turtle.Turtle()
block_19.speed(0)
block_19.shape('square')
block_19.color('white')
block_19.shapesize(stretch_wid=2, stretch_len=4)
block_19.penup()
block_19.goto(420, 300)

block_20 = turtle.Turtle()
block_20.speed(0)
block_20.shape('square')
block_20.color('white')
block_20.shapesize(stretch_wid=2, stretch_len=4)
block_20.penup()
block_20.goto(540, 300)

# Rząd nr 3
block_21 = turtle.Turtle()
block_21.speed(0)
block_21.shape('square')
block_21.color('white')
block_21.shapesize(stretch_wid=2, stretch_len=4)
block_21.penup()
block_21.goto(-540, 230)

block_22 = turtle.Turtle()
block_22.speed(0)
block_22.shape('square')
block_22.color('white')
block_22.shapesize(stretch_wid=2, stretch_len=4)
block_22.penup()
block_22.goto(-420, 230)

block_23 = turtle.Turtle()
block_23.speed(0)
block_23.shape('square')
block_23.color('white')
block_23.shapesize(stretch_wid=2, stretch_len=4)
block_23.penup()
block_23.goto(-300, 230)

block_24 = turtle.Turtle()
block_24.speed(0)
block_24.shape('square')
block_24.color('white')
block_24.shapesize(stretch_wid=2, stretch_len=4)
block_24.penup()
block_24.goto(-180, 230)

block_25 = turtle.Turtle()
block_25.speed(0)
block_25.shape('square')
block_25.color('white')
block_25.shapesize(stretch_wid=2, stretch_len=4)
block_25.penup()
block_25.goto(-60, 230)

block_26 = turtle.Turtle()
block_26.speed(0)
block_26.shape('square')
block_26.color('white')
block_26.shapesize(stretch_wid=2, stretch_len=4)
block_26.penup()
block_26.goto(60, 230)

block_27 = turtle.Turtle()
block_27.speed(0)
block_27.shape('square')
block_27.color('white')
block_27.shapesize(stretch_wid=2, stretch_len=4)
block_27.penup()
block_27.goto(180, 230)

block_28 = turtle.Turtle()
block_28.speed(0)
block_28.shape('square')
block_28.color('white')
block_28.shapesize(stretch_wid=2, stretch_len=4)
block_28.penup()
block_28.goto(300, 230)

block_29 = turtle.Turtle()
block_29.speed(0)
block_29.shape('square')
block_29.color('white')
block_29.shapesize(stretch_wid=2, stretch_len=4)
block_29.penup()
block_29.goto(420, 230)

block_30 = turtle.Turtle()
block_30.speed(0)
block_30.shape('square')
block_30.color('white')
block_30.shapesize(stretch_wid=2, stretch_len=4)
block_30.penup()
block_30.goto(540, 230)

# Tablica
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,-390)
pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))


# Poruszanie paletką

def paddle_left():
    x = paddle.xcor()
    x -= 10
    paddle.setx(x)
def paddle_right():
    x = paddle.xcor()
    x += 10
    paddle.setx(x)

# Bindy na klawiaturze

wn.listen()
wn.onkeypress(paddle_left, 'Left')
wn.onkeypress(paddle_right, 'Right')


# Pętla gry:
while True:
    wn.update()
    # Ruch piłki:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Granica:
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
    if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1
        life -= 1
        pen.clear()
        pen.write("Life left: {}  Points: {}".format(life, y), align='center', font=('Courier', 16, 'bold'))
    if ball.xcor() > 590:
        ball.setx(590)
        ball.dx *= -1
    if ball.xcor() < -590:
        ball.setx(-590)
        ball.dx *= -1
    # Odbicie piłki od paletki
    if (paddle.xcor() - 60 < ball.xcor() and paddle.xcor() + 60 > ball.xcor()) \
            and (ball.ycor() < -345 and ball.ycor() >-350):
        ball.sety(-345)
        ball.dy *= -1
    # Usuwanie klocków
    # Rząd pierwszy
    hit_1(block_1,y)
    hit_1(block_2,y)
    hit_1(block_3,y)
    hit_1(block_4,y)
    hit_1(block_5,y)
    hit_1(block_6,y)
    hit_1(block_7,y)
    hit_1(block_8,y)
    hit_1(block_9,y)
    hit_1(block_10,y)


    # Rząd drugi
    hit_2(block_11,y)
    hit_2(block_12,y)
    hit_2(block_13,y)
    hit_2(block_14,y)
    hit_2(block_15,y)
    hit_2(block_16,y)
    hit_2(block_17,y)
    hit_2(block_18,y)
    hit_2(block_19,y)
    hit_2(block_20,y)

    # Rząd trzeci
    hit_3(block_21,y)
    hit_3(block_22,y)
    hit_3(block_23,y)
    hit_3(block_24,y)
    hit_3(block_25,y)
    hit_3(block_26,y)
    hit_3(block_27,y)
    hit_3(block_28,y)
    hit_3(block_29,y)
    hit_3(block_30,y)



    if life == 0:
        ball.goto(2000,2000)
        ball.dx = 0
        ball.dy = 0
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color('white')
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 0)
        pen2.write("GAME OVER!", align='center', font=('Courier', 40, 'bold'))
        time.sleep(5)
        break


    # if hit_1(block_1,y) == True and hit_1(block_2,y) == True and hit_1(block_3,y) == True and hit_1(block_4,y) == True \
    # and hit_1(block_5,y) == True and hit_1(block_6,y) == True and hit_1(block_7,y) == True and hit_1(block_8,y) == True \
    # and hit_1(block_9, y) == True and hit_1(block_10,y) == True and hit_2(block_11,y) == True and hit_2(block_12,y) == True \
    # and hit_2(block_13, y) == True and hit_2(block_14,y) == True and hit_2(block_15,y) == True and hit_2(block_16,y) == True \
    # and hit_2(block_17, y) == True and hit_2(block_18,y) == True and hit_2(block_19,y) == True and hit_2(block_20,y) == True \
    # and hit_3(block_21, y) == True and hit_3(block_22, y) == True and hit_3(block_23, y) == True and hit_3(block_24, y) == True \
    # and hit_3(block_25, y) == True and hit_3(block_26, y) == True and hit_3(block_27, y) == True and hit_3(block_28, y) == True \
    # and hit_3(block_29, y) == True and hit_3(block_30, y) == True:
    if block_1.xcor == 2000 and block_1.ycor == 2000 and block_2.xcor == 2000 and block_2.ycor == 2000 and block_3.xcor == 2000 and block_3.ycor == 2000 \
    and block_4.xcor == 2000 and block_4.ycor == 2000 and block_5.xcor == 2000 and block_5.ycor == 2000 and block_6.xcor == 2000 and block_6.ycor == 2000 \
    and block_7.xcor == 2000 and block_7.ycor == 2000 and block_8.xcor == 2000 and block_8.ycor == 2000 and block_9.xcor == 2000 and block_9.ycor == 2000 \
    and block_10.xcor == 2000 and block_10.ycor == 2000 and block_11.xcor == 2000 and block_11.ycor == 2000 and block_12.xcor == 2000 and block_12.ycor == 2000 \
    and block_13.xcor == 2000 and block_13.ycor == 2000 and block_14.xcor == 2000 and block_14.ycor == 2000 and block_15.xcor == 2000 and block_15.ycor == 2000 \
    and block_16.xcor == 2000 and block_16.ycor == 2000 and block_17.xcor == 2000 and block_17.ycor == 2000 and block_18.xcor == 2000 and block_18.ycor == 2000 \
    and block_19.xcor == 2000 and block_19.ycor == 2000 and block_20.xcor == 2000 and block_20.ycor == 2000 and block_21.xcor == 2000 and block_21.ycor == 2000 \
    and block_22.xcor == 2000 and block_22.ycor == 2000 and block_23.xcor == 2000 and block_23.ycor == 2000 and block_24.xcor == 2000 and block_24.ycor == 2000 \
    and block_25.xcor == 2000 and block_25.ycor == 2000 and block_26.xcor == 2000 and block_26.ycor == 2000 and block_27.xcor == 2000 and block_27.ycor == 2000 \
    and block_28.xcor == 2000 and block_28.ycor == 2000 and block_29.xcor == 2000 and block_29.ycor == 2000 and block_30.xcor == 2000 and block_30.ycor == 2000:
        ball.goto(2000, 2000)
        ball.dx = 0
        ball.dy = 0
        pen3 = turtle.Turtle()
        pen3.speed(0)
        pen3.color('white')
        pen3.penup()
        pen3.hideturtle()
        pen3.goto(0, 0)
        pen3.write("YOU WON!", align='center', font=('Courier', 40, 'bold'))
        time.sleep(5)
        break


