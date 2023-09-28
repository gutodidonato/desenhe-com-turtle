from turtle import *

timot = Turtle()
timot.state = ""

def pen():
    if timot.state == "pendown":
        timot.state = "penup"
        timot.penup()
    else:
        timot.state = "pendown"
        timot.pendown()

def move_forward():
    timot.forward(10)
    
def move_backward():
    timot.backward(10)

def right():
    timot.right(15)

def left():
    timot.left(15)




screen = Screen()
screen.listen()
screen.onkey(pen, "p")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(right, "d")  
screen.onkey(left, "a")
screen.exitonclick()
