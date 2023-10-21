import turtle
from snake_utils import *

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(600, 600)
main_screen.title("~~~Snake~~Game~~~")
main_screen.tracer(False)
root = main_screen._root

snake_head = create_object("square", "green")
snake_food = create_object("circle", "red")
change_position(snake_food)
# TODO Add poison apple


def close():
    global running
    running = False


root.protocol("WM_DELETE_WINDOW", close)

running = True
while running:
    main_screen.update()
