from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
c=["red","yellow","purple","orange"]
#t.screen.tracer(0,0)
t.speed(0)
t.penup()
t.goto(0,-50)
t.pendown()
for x in range(300):
    t.color(c[x%4])
    t.fd(x)
    t.left(59)
    #t.left(135)#star
t.hideturtle()


