from turtle import *
import random

def spiral(size):
    for i in range(360):
        circle(i,size)

def confused_cursor():
    for i in range(100):
        forward(50)
        left(random.randint(1, 180))
        right(random.randint(1, 180))

def race():
    c1 = Turtle()
    c2 = Turtle()
    c1.speed(0)
    c2.speed(0)
    c1.penup()
    c2.penup()
    c1.setpos(-500,0)
    c2.setpos(-500,-100)
    c1.pendown()
    c2.pendown()
    c1.speed(10)
    c2.speed(10)
    for i in range(500):
        c1.forward(random.randint(1,10))
        c2.forward(random.randint(1,10))

def anarchy():
    cursors = [Turtle() for i in range(20)]
    for cursor in cursors:
        cursor.penup()
        cursor.setpos(random.randint(-300, 400), random.randint(-300, 400))
    