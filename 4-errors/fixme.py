# There are two syntax errors and one logical error in this code
# The output should be a large spiral
import turtl


window = turtle.Screen()
tur = turtle.Turtle()

tur.speed(0)

speed = 0
speed = speed + 0.1 #A faster way to write an addition equation like this is: speed += 0.1
for _ in range(1, 300):
    tur.forward(speed)
    tur.goleft(20)

