import turtle


def create_object(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle
