import turtle
from snake_utils import create_object

main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.setup(600, 600)
main_screen.title("~~~Snake~~Game~~~")
root = main_screen._root


def close():
    global running
    running = False


root.protocol("WM_DELETE_WINDOW", close)

running = True
while running:
    main_screen.update()
