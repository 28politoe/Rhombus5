import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t=turtle.Turtle()



t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.goto(100,100)
t.goto(200,0)
t.goto(100,-100)
t.goto(0,-0)
t.end_fill()


t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("cyan")
t.begin_fill()
t.goto(-100,100)
t.goto(-200,0)
t.goto(-100,-100)
t.goto(0,0 )
t.end_fill()


t.hideturtle()













turtle.done()