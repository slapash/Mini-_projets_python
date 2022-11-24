from turtle import *
win = Screen()
times = win.numinput("E9SSARS","combien d'e9ssars ? :")
tortue = Turtle()
tortue.pendown()
tortue.fillcolor("green")
tortue.begin_fill()
for i in range(5):
    tortue.forward(50)
    tortue.right(144)

tortue.end_fill()
tortue.penup()
tortue.goto(-50,60)
tortue.pendown()
tortue.setheading(0)


for i in range(int(times)):
    tortue.forward(150)
    tortue.right(90)

win.exitonclick()