import turtle
import random


def create_object(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.color(color)

    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = random.randint(-270, 270)
    y = random.randint(-270, 230)
    object.goto(x, y)
