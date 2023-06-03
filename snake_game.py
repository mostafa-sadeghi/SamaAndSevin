import turtle
import time


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y = y + 20
        snake_head.sety(y)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x = x + 20
        snake_head.setx(x)


window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.speed('fastest')
snake_head.penup()
snake_head.direction = ""

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_right, "Right")

while True:
    window.update()
    move_snake()
    time.sleep(0.1)
