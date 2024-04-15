import turtle
import random

# Set up the turtle screen
turtle.bgcolor("black")
turtle.speed(0)

# Set up the initial position and color of the turtle
turtle.pencolor("green")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

# Start drawing the spiral
a = 0
b = 0
while True:
    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1
    if b == 200:
        break

# Move the turtle to a new position and write text
turtle.goto(0, -100)
turtle.pencolor("white")
font_style = ("Courier", 35, "bold")
turtle.write("Corona Virus", align="center", font=font_style)

# Finish the drawing
turtle.exitonclick()