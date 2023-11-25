import turtle
from snake_utils import *
from time import sleep
import os
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
    if snake_head.direction != "down":
        snake_head.direction = "up"


def change_dir_to_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def change_dir_to_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def change_dir_to_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


main_screen.listen()
main_screen.onkeypress(change_dir_to_up, "Up")
main_screen.onkeypress(change_dir_to_down, "Down")
main_screen.onkeypress(change_dir_to_left, "Left")
main_screen.onkeypress(change_dir_to_right, "Right")


root.protocol("WM_DELETE_WINDOW", close)

score = 0
if os.path.exists("score.txt"):
    with open("score.txt", "r") as file:
        high_score = int(file.read())
else:
    high_score = 0
scoreboard = create_object("square", "purple")
scoreboard.goto(0, 260)
scoreboard.hideturtle()
scoreboard.write(f'Score:{score}, highScore:{high_score}', align="center", font=("Arial", 22))

snake_tails = []

running = True
while running:
    main_screen.update()
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        score += 1
        new_tail = create_object("square", "darkgreen")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(-1 * snake_head.xcor())
    if snake_head.ycor() >230:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(230)

    scoreboard.clear()
    scoreboard.write(f'Score:{score}, highScore:{high_score}', align="center", font=("Arial", 22))


    move()

    for tail in snake_tails:
        if tail.distance(snake_head) < 20:
            if score > high_score:
                high_score = score
                with open("score.txt","w") as file:
                    file.write(str(high_score))
            score = 0
            snake_head.home()
            snake_head.direction = ""
            for tail in snake_tails:
                tail.ht()
            snake_tails.clear()
            break


    sleep(0.2)
