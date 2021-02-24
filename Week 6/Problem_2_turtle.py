#Problem 2 Turtle
#Nelson Koomson
#2/18/21

#This program uses for loop and the turtle module to draw a square
import turtle
Nelson = turtle.Turtle()

Nelson.pencolor("Yellow")


for side in range(4):
    Nelson.forward(100)
    Nelson.right(90)

turtle.done()
