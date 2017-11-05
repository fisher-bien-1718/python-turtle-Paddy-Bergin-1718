# There are two syntax errors and one logical error in this code
# The out put should be a large spiral
import turtl


window = turtle.Screen()
tur = turtle.Turtle()

tur.speed(0)

speed = 0
for _ in range(1, 300):
    tur.forward(speed)
    tur.goleft(20)
speed += 0.1
