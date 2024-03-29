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


def check_collision(item1, item2):
    if item1.distance(item2) < 20:
        return True


def change_food_position():
    random_x = random.randint(-270, 270)
    random_y = random.randint(-270, 230)
    food.goto(random_x, random_y)


def reset():
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for body in snake_bodies:
        body.hideturtle()

    snake_bodies.clear()


window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
change_food_position()

score_board = make_turtle("square", "white")
score_board.goto(0, 260)
score_board.hideturtle()
score = 0
high_score = 0

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")
window.onkeypress(go_down, "Down")

def onclose():
    global running
    running = False
root = window._root
root.protocol("WM_DELETE_WINDOW", onclose)


snake_bodies = []
running = True
while running:
    score_board.clear()
    score_board.write(
        f"Score: {score}\tHighScore: {high_score}", align="center", font=("Terminal", 22))

    window.update()
    if check_collision(snake_head, food) == True:
        change_food_position()
        score += 1

        if score > high_score:
            high_score = score

        new_body = make_turtle("square", "grey")
        snake_bodies.append(new_body)

    for i in range(len(snake_bodies) - 1, 0, -1):
        x = snake_bodies[i-1].xcor()
        y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(x, y)

    if len(snake_bodies) > 0:
        head_x = snake_head.xcor()
        head_y = snake_head.ycor()
        snake_bodies[0].goto(head_x, head_y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset()
        score = 0

    move_snake()

    for body in snake_bodies:
        if check_collision(body, snake_head) == True:
            reset()
            score = 0

    time.sleep(0.15)
