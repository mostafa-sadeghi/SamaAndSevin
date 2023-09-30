# import turtle

# s = turtle.Screen()
# pen = turtle.Pen()
# pen.shape('turtle')
# pen.pensize(2)
# pen.pencolor("red")
# pen.fillcolor("green")


# pen.begin_fill()
# for i in range(3):
#     pen.forward(100)
#     pen.left(120)
# pen.end_fill()

# # exercise 1:
# # کشیدن مربع، مستطیل، پنجضلعی هم تو پر و هم توخالی
# # exercise 2: کشیدن ستاره
# turtle.done()


################################################

# import turtle

# s = turtle.Screen()
# s.bgcolor('black')

# pen = turtle.Pen()
# pen.speed("slowest")
# pen.shape('turtle')
# pen.shapesize(2)

# pen.pensize(2)
# pen.pencolor("red")
# pen.fillcolor("green")

# # pen.setheading(90)
# # pen.forward(100)

# # pen.left(120)
# # pen.forward(150)

# # pen.goto(0,0)
# # pen.circle(50)
# # pen.hideturtle()




# turtle.done()

##########################################################
import turtle

s = turtle.Screen()
s.bgcolor('black')
s.bgpic("back.png")

s.register_shape("strawberry.gif")


pen = turtle.Pen()
pen.speed("slowest")
# pen.shape('turtle')
pen.shape('strawberry.gif')
pen.shapesize(2)

pen.pensize(2)
pen.pencolor("red")
pen.fillcolor("green")

for i in range(3):
    pen.fd(150)
    pen.right(120)
    pen.stamp()



turtle.done()

