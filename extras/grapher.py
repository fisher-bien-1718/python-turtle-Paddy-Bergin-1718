import turtle


screenwidth = 500
screenheight = 500
width = 30
height = 30
subdivisions = 5
window = turtle.Screen()
window.setup(screenwidth, screenheight)
t = turtle.Turtle()
t.speed(0)



def getx(x):
    return x * ((screenwidth / 2) / width)


def gety(y):
    return y * ((screenheight / 2) / height)


def graph(x):
    y = 0.2 * (x * x * x) - 2 * (x * x) + x - 2
    return gety(y)


def setup():
    t.penup()
    t.penup()
    t.goto(-(screenwidth / 2), 0)
    t.pendown()
    t.goto(screenwidth / 2, 0)
    t.penup()
    t.goto(0, -(screenheight / 2))
    t.pendown()
    t.goto(0, (screenheight / 2))
    t.penup()
    t.goto(-screenwidth / 2, graph(-width))
    t.pendown()


setup()
for i in range(-width, width):
    for j in range(0, subdivisions):
        t.goto(getx(i + (j / subdivisions)), graph(i + (j / subdivisions)))


window.mainloop()
