import turtle

t=turtle.Turtle()
t.speed(100)
t.pu()
t.goto(-170,200)
t.pd()

t.color('black','black')
t.begin_fill()
for r in range(10):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(30,220)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(30,180)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)        
t.end_fill()

t.pu()
t.goto(-150,220)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)        
t.end_fill()

t.pu()
t.goto(-150,180)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()


t.pu()
t.goto(-150,220)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)

t.pu()
t.goto(-170,240)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-190,240)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-190,240)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.goto(-190,240)
t.rt(90)
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.begin_fill()
for r in range(4):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-210,160)
t.pd()

t.begin_fill()
for r in range(5):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-190,40)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-170,40)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-170,60)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.lt(90)
t.pu()
t.goto(-170,40)
t.pd()

t.begin_fill()
for r in range(11):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.rt(90)
t.pu()
t.goto(50,40)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.lt(90)
t.pu()
t.goto(70,20)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.lt(90)
t.pu()
t.goto(110,20)
t.pd()
t.begin_fill()
for r in range(5):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(90,120)
t.pd()
t.begin_fill()
for r in range(6):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.lt(90)
t.pu()
t.goto(70,260)
t.pd()
t.begin_fill()
for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

def square():
        t.begin_fill()
        for x in range(4):
                t.fd(20)
                t.lt(90)
        t.end_fill()

t.pu()
t.goto(-150,20)
t.pd()
square()

t.pu()
t.goto(70,20)
t.pd()
square()

t.pu()
t.goto(-130,0)
t.pd()
square()

t.pu()
t.goto(50,0)
t.pd()
square()

t.pu()
t.goto(-150,-40)
t.pd()
t.rt(180)
t.begin_fill()
for r in range(8):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-170,-40)
t.pd()
square()

t.pu()
t.goto(-190,-60)
t.pd()
square()

t.pu()
t.goto(-210,-40)
t.pd()
t.rt(90)
t.begin_fill()
for r in range(6):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-210,-180)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(3):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()


t.pu()
t.goto(-130,-180)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(5):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-130,-180)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-150,-200)
t.pd()
t.lt(90)
square()


t.pu()
t.goto(-150,-220)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(4):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(-50,-200)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-50,-160)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-50,-160)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-50,-200)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-30,-220)
t.pd()
t.lt(90)
square()

t.rt(180)
t.pu()
t.goto(-50,-220)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(4):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(50,-220)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(7):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(70,-160)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(70,-160)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(90,-180)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(110,-180)
t.pd()
t.lt(90)
t.begin_fill()
for r in range(5):
    t.pu()
    t.fd(20)
    t.pd()
    for x in range(4):
        t.fd(20)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(70,-20)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(70,-40)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-190,-120)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(-150,-120)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(70,-100)
t.pd()
t.lt(90)
square()

t.pu()
t.goto(70,-100)
t.pd()
t.lt(90)
square()
turtle.done()
