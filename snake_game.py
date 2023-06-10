import turtle
import time
import random

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y = y + 20
        snake_head.sety(y)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x = x + 20
        snake_head.setx(x)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y = y - 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x = x - 20
        snake_head.setx(x)

def make_turtle(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.speed('fastest')
    my_turtle.color(color)
    my_turtle.penup()
    return my_turtle


def check_collision(item1 , item2):
    if item1.distance(item2)<20:
        return True

def change_food_position():
    random_x = random.randint(-270,270)
    random_y = random.randint(-270,270)
    food.goto(random_x,random_y)

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
food.goto(100,100)



window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")
window.onkeypress(go_down, "Down")

while True:
    window.update()
    if check_collision(snake_head, food) == True:
        change_food_position()
    move_snake()
    time.sleep(0.15)
