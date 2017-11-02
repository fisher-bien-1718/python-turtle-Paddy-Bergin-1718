import turtle

window = turtle.Screen()
t = turtle.Turtle()
firstmultiply = input("First number?")
secondmultiply = input("Second number?")

product = firstmultiply * secondmultiply
print(product)

for i in range(sides):
    t.forward(100)
    t.right(360 / sides)

window.mainloop()