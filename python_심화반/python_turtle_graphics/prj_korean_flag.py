import turtle

#--setting--
kor = turtle.Turtle()
kor.hideturtle()
kor.pensize(2)

#moved to first picturing location
kor.penup()
kor.circle(80,60)
kor.pendown()

#upper circle - red part
kor.fillcolor('red')
kor.begin_fill()
kor.circle(80,180)
kor.end_fill()

#lower circle - blue part
kor.fillcolor('blue')
kor.begin_fill()
kor.circle(80,180)
kor.circle(40,180)
kor.end_fill()

# upper circle (remaining) - red part
kor.fillcolor('red')
kor.begin_fill()
kor.circle(-40,180)
kor.end_fill()

#goes to the location 'keon'
kor.penup()
kor.goto(-140,200)
kor.pendown()

def paint_full_black() :
    kor.begin_fill()
    kor.forward(-90)
    kor.left(90)
    kor.forward(10)
    kor.left(90)
    kor.forward(-90)
    kor.left(90)
    kor.forward(10)
    kor.end_fill()

kor.fillcolor('black')
paint_full_black()

for i in range(0,2): # repeat two times
    kor.penup()
    kor.forward(-20)
    kor.pendown()

    kor.left(90)
    paint_full_black()

#----------------------- geon finished

# goes to the location 'kon'
kor.penup()
kor.goto(140,200)
kor.right(30)
kor.pendown()

#paint_half_black
def paint_half_black() :
    kor.begin_fill()
    kor.forward(40)
    kor.left(90)
    kor.forward(10)
    kor.left(90)
    kor.forward(40)
    kor.left(90)
    kor.forward(10)
    kor.end_fill()

paint_half_black()

kor.penup()
kor.left(90)
kor.forward(50)
kor.pendown()

paint_half_black()

kor.penup()
kor.left(-90)
kor.forward(50)
kor.left(-90)
kor.forward(30)
kor.left(90)
kor.pendown()

paint_full_black()

kor.penup()
kor.forward(10)
kor.left(-90)
kor.pendown()

paint_half_black()

kor.penup()
kor.left(90)
kor.forward(50)
kor.pendown()

paint_half_black()

#----------------------------------------- kon finished 

#goes to the location kam
kor.penup()
kor.goto(-140,-40)
kor.right(90)
kor.pendown()

kor.begin_fill()
kor.forward(90)
kor.left(90)
kor.forward(10)
kor.left(90)
kor.forward(90)
kor.left(90)
kor.forward(10)
kor.end_fill()

kor.penup()
kor.left(180)
kor.forward(20)
kor.right(90)
kor.pendown()

paint_half_black()

kor.penup()
kor.left(90)
kor.forward(50)
kor.pendown()

paint_half_black()

kor.penup()
kor.right(90)
kor.forward(50)
kor.right(90)
kor.forward(20)
kor.right(90)
kor.pendown()

kor.begin_fill()
kor.forward(90)
kor.left(90)
kor.forward(10)
kor.left(90)
kor.forward(90)
kor.left(90)
kor.forward(10)
kor.end_fill()

#-------------------------- gam finished

#goes to the location lee
kor.penup()
kor.goto(140,-40)
kor.left(30)
kor.forward(90)
kor.left(180)
kor.pendown()

def double_paint_half_black():
    paint_half_black()

    kor.penup()
    kor.left(90)
    kor.forward(50)
    kor.pendown()

    paint_half_black()

double_paint_half_black()

kor.penup()
kor.right(90)
kor.forward(50)
kor.right(90)
kor.forward(20)
kor.right(90)
kor.pendown()

double_paint_half_black()

kor.penup()
kor.right(90)
kor.forward(50)
kor.right(90)
kor.forward(20)
kor.right(90)
kor.pendown()

double_paint_half_black()

turtle.done()