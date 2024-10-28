import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("light green")

screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(3)

t1 = turtle.Turtle()
t1.speed(0)
t1.width(3)

t2 = turtle.Turtle()
t2.speed(0)
t2.width(3)

t3 = turtle.Turtle()
t3.speed(0)
t3.width(3)

th = turtle.Turtle()
th.speed(0)
th.width(3)

tr = turtle.Turtle()
tr.speed(0)
tr.width(3)

tb = turtle.Turtle()
tb.speed(0)
tb.width(3)

t4 = turtle.Turtle()
t4.speed(0)
t4.width(3)

t5 = turtle.Turtle()
t5.speed(0)
t5.width(3)

t6 = turtle.Turtle()
t6.speed(0)
t6.width(3)

t7 = turtle.Turtle()
t7.speed(0)
t7.width(3)

t8 = turtle.Turtle()
t8.speed(0)
t8.width(3)

t9 = turtle.Turtle()
t9.speed(0)
t9.width(3)

t10 = turtle.Turtle()
t10.speed(0)
t10.width(3)

t11 = turtle.Turtle()
t11.speed(0)
t11.width(3)

t.hideturtle()
t1.hideturtle()
t2.hideturtle()
th.hideturtle()
tr.hideturtle()
tb.hideturtle()
t4.hideturtle()
t5.hideturtle()
t6.hideturtle()
t7.hideturtle()
t8.hideturtle()
t9.hideturtle()
t10.hideturtle()
t11.hideturtle()

def car1():
    t.fillcolor("orange")
    t.begin_fill()
    for side in range(2):
        t.forward(100)
        t.left(90)
        t.forward(30)
        t.left(90)
        
    t.end_fill()
    th.fillcolor("yellow")
    th.begin_fill()

    for side in range(2):
        th.forward(50)
        th.left(90)
        th.forward(20)
        th.left(90)

    th.end_fill()

def car2():
    t4.fillcolor("blue")
    t4.begin_fill()
    for e in range(2):
        t4.forward(100)
        t4.left(90)
        t4.forward(30)
        t4.left(90)

    t4.end_fill()
    t5.fillcolor("green")
    t5.begin_fill()

    for e in range(2):
        t5.forward(50)
        t5.left(90)
        t5.forward(20)
        t5.left(90)

    t5.end_fill()

def truck():
    t8.fillcolor("orange")
    t8.begin_fill()

    t8.forward(100)
    t8.left(90)
    t8.forward(60)
    t8.left(90)
    t8.forward(100)
    t8.left(90)
    t8.forward(60)
    t8.left(90)
    
    t8.end_fill()
    t9.fillcolor("black")
    t9.begin_fill()

    t9.forward(20)
    t9.left(90)
    t9.forward(20)
    t9.left(90)
    t9.forward(20)
    t9.left(90)
    t9.forward(20)
    t9.left(90)

    t9.end_fill()
    
    
def odraw1():
    t1.fillcolor("black")
    t1.begin_fill()
    t1.circle(10)
    t1.end_fill()

def odraw2():
    t2.fillcolor("black")
    t2.begin_fill()
    t2.circle(10)
    t2.end_fill()

def odraw3():
    t6.fillcolor("black")
    t6.begin_fill()
    t6.circle(10)
    t6.end_fill()

def odraw4():
    t7.fillcolor("black")
    t7.begin_fill()
    t7.circle(10)
    t7.end_fill()

def odraw5():
    t10.fillcolor("black")
    t10.begin_fill()
    t10.circle(10)
    t10.end_fill()

def odraw6():
    t11.fillcolor("black")
    t11.begin_fill()
    t11.circle(10)
    t11.end_fill()
    
def road():
    tr.goto(-800, -100)
    tr.fillcolor("brown")
    tr.begin_fill()
    tr.forward(1700)
    tr.left(90)
    tr.forward(200)
    tr.left(90)
    tr.forward(1700)
    tr.left(90)
    tr.forward(200)
    tr.left(90)
    tr.end_fill()
    tr.goto(-800, 0)
    tr.pencolor("yellow")
    tr.forward(1700)

def sum():
    t3.penup()
    t3.goto(400, 300)
    t3.pendown()
    t3.fillcolor("yellow")
    t3.begin_fill()
    t3.circle(100)
    t3.end_fill()

def building():
    tb.penup()
    tb.goto(99, 100)
    tb.pendown()
    tb.fillcolor("grey")
    tb.begin_fill()
    tb.forward(50)
    tb.left(90)
    tb.forward(150)
    tb.left(90)
    tb.forward(50)
    tb.left(90)
    tb.forward(150)
    tb.end_fill()

    
t.penup()
t.goto(-350, 0)
t.pendown()

t1.penup()
t1.goto(-330, -10)
t1.pendown()

t2.penup()
t2.goto(-270, -10)
t2.pendown()

th.penup()
th.goto(-320, 30)
th.pendown()

t4.penup()
t4.goto(350, -50)
t4.pendown()

t7.penup()
t7.goto(430, -60)
t7.pendown()

t6.penup()
t6.goto(370, -60)
t6.pendown()

t5.penup()
t5.goto(380, -20)
t5.pendown()

t8.penup()
t8.goto(-200, 0)
t8.pendown()

t10.penup()
t10.goto(-180, -10)
t10.pendown()

t11.penup()
t11.goto(-120, -10)
t11.pendown()

t9.penup()
t9.goto(-140, 60)
t9.pendown()

road()
sum()
building()

while True:
    t.clear()
    t1.clear()
    t2.clear()
    th.clear()
    t4.clear()
    t5.clear()
    t6.clear()
    t7.clear()
    t8.clear()
    t9.clear()
    t10.clear()
    t11.clear()

    car1()
    car2()
    truck()
    odraw1()
    odraw2()
    odraw3()
    odraw4()
    odraw5()
    odraw6()

    screen.update()
    t.forward(0.2)
    t1.forward(0.2)
    t2.forward(0.2)
    th.forward(0.2)
    t4.forward(-0.2)
    t5.forward(-0.2)
    t6.forward(-0.2)
    t7.forward(-0.2)
    t8.forward(0.2)
    t9.forward(0.2)
    t10.forward(0.2)
    t11.forward(0.2)
