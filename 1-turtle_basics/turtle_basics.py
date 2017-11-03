import turtle

window = turtle.Screen()
t = turtle.Turtle()


t.speed(0)

for x in range(0, 8):
    t.left(45)
    for x in range(0, 4):
        t.forward(100)
        t.left(90)

window.mainloop()