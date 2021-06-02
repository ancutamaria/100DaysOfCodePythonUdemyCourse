# from turtle import *

# import turtle as tr
# timmy_the_turtle = tr.Turtle()

# import heroes
# print(heroes.gen())
import random
import turtle as tr

timmy_the_turtle = tr.Turtle()

timmy_the_turtle.color("pink")
timmy_the_turtle.shape("turtle")


# draw a square
# def walk_and_turn_right():
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
# for _ in range(4):
#     walk_and_turn_right()


# draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# drawing different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side in range(3, 11):
#     timmy_the_turtle.color(random.choice(["pink", "cyan", "green", "yellow"]))
#     draw_shape(shape_side)

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


# # generating a random walk
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
tr.colormode(255)


# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

# drawing a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_spirograph(5)

screen = tr.Screen()
screen.exitonclick()
