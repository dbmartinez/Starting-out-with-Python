# Chapter 2
# Program 15(c)

import turtle

turtle.setup(1100, 900)
turtle.goto(0, 0)
turtle.circle(50)
turtle.penup()
turtle.goto(-10, 300)
turtle.write('North')

turtle.goto(-300, 50)
turtle.write('West')

turtle.goto(300, 50)
turtle.write('East')

turtle.goto(-10, -250)
turtle.write('South')

turtle.goto(0, 50)
turtle.pendown()
turtle.setheading(180)
turtle.forward(300)

turtle.goto(0, 50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(320)

turtle.goto(0, 50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(250)

turtle.goto(0, 50)
turtle.pendown()
turtle.setheading(270)
turtle.forward(290)

turtle.done()