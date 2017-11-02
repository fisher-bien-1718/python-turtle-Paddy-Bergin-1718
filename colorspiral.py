import turtle
import colorsys  # Converts between HSV and RGB


window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t._tracer(0, 0)


spirals = int(input("How many spirals? (2 - 10)"))
density = float(input("How dense? (0.5 - 5)"))
count = int(input("How many lines? (10 - 1000)"))

for i in range(500): # this "for" loop will repeat these functions 500 times
    color = colorsys.hsv_to_rgb(float(i % spirals) / spirals, 1, 1)
    t.pencolor(color[0], color[1], color[2])
    t.forward(i / density)
    t.left(360 / spirals - 1)

window.mainloop()