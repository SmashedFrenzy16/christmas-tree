import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.title("Christmas Tree")
s.setup(width=800, height=600)

# Title on the window

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Christmas Tree", align="center",font=("Arial", 24, "normal"))

# Starting position

t.up()

t.rt(90)
t.fd(100)
t.lt(90)

t.down()

# Stump

t.color("brown")
t.begin_fill()
t.fd(40)
t.lt(90)
t.fd(60)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(60)
t.end_fill()
t.up()

# First triangle

t.lt(180)
t.fd(60)
t.lt(90)
t.fd(20)
t.down()
t.color("green")
t.begin_fill()
t.rt(180)
t.fd(80)
t.lt(120)
t.fd(80)
t.lt(120)
t.fd(80)
t.end_fill()
t.up()

# Second Triangle

t.lt(180)
t.fd(80)
t.lt(120)
t.lt(90)
t.fd(20)
t.rt(90)
t.down()
t.begin_fill()
t.fd(35)
t.rt(120)
t.fd(70)
t.rt(120)
t.fd(70)
t.rt(120)
t.fd(35)
t.end_fill()
t.up()

# Thrid Triangle

t.fd(35)
t.rt(120)
t.fd(70)
t.lt(120)
t.lt(90)
t.fd(20)
t.rt(90)
t.down()
t.begin_fill()
t.fd(30)
t.rt(120)
t.fd(60)
t.rt(120)
t.fd(60)
t.rt(120)
t.fd(30)
t.end_fill()
t.up()

# Star

t.fd(30)
t.rt(120)
t.fd(60)
t.lt(120)
t.rt(180)
t.lt(90)
t.fd(15)
t.rt(90)
t.back(20)
t.color("yellow")
t.down()


t.begin_fill()

for i in range(5):
    t.forward(40)
    t.right(144)

t.end_fill()


 


while True:
    s.update()
