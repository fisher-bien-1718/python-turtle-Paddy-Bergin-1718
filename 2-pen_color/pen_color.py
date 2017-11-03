import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.pencolor(1.0, 0, 0) # RGB values
t.forward(100)
t.left(120)
t.pencolor("red") # Common name
t.forward(100)
t.left(120)
t.pencolor("#ff0000") # Hex code
t.forward(100)

window.mainloop()