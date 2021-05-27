import workout_another_module

print(workout_another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")
timmy.forward(100)
print(timmy)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

