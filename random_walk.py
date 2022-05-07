import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
nemo = Turtle()
nemo.shape("turtle")
nemo.pensize(15)
nemo.speed(0)
n = 0
k = [0,90,180,270]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

while n != 1000:
    n += 1
    color= random_color()
    nemo.color(color)
    for _ in range(0, n):
        nemo.forward(30)
        nemo.setheading(random.choice(k))


screen = Screen()

screen.exitonclick()
