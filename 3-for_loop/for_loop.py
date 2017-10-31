import turtle

window = turtle.Screen()
t = turtle.Turtle()

for _ in range(0, 3):
    for _ in range(0, 3):
        for _ in range(0, 4):
            t.forward(100)
            t.left(90)
        t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(300)
    t.left(180)

window.mainloop()