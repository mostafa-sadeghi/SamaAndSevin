import turtle
from snake_utils import *
from time import sleep
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(600, 600)
main_screen.title("~~~Snake~~Game~~~")
main_screen.tracer(False)
root = main_screen._root
snake_head = create_object("square", "green")
snake_head.direction = ""
snake_food = create_object("circle", "red")
change_position(snake_food)
# TODO Add poison apple


def close():
    global running
    running = False


def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def change_dir_to_up():
    """
    This function is used to change snake direction to up
    """
    if snake_head.direction != "down":
        snake_head.direction = "up"
# TODO  تعریف تابع برای سایر جهت ها


main_screen.listen()
main_screen.onkeypress(change_dir_to_up, "Up")
# صدازدن تابع برای سایر جهت ها

root.protocol("WM_DELETE_WINDOW", close)
running = True
while running:
    main_screen.update()
    move()
    sleep(0.2)
