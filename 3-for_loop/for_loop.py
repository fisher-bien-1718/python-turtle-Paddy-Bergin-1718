import turtle

window = turtle.Screen()
t = turtle.Turtle()

for x in range(0, 100):
    t.forward(x * 3)
    t.left(90)

window.mainloop()