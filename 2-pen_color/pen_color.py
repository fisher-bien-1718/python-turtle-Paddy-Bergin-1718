import turtle

window = turtle.Screen()
t = turtle.Turtle()

for _ in range(0, 4):
    for _ in range(0, 5):
        t.forward(100)
        t.left(216)

window.mainloop()