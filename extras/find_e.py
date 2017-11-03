# Calculates e

iterations = 1000

def factorial(x):
    value = 1
    for x in range(1, x):
        value *= x
    return value

e = 0
for x in range(1, iterations):
    e += 1 / factorial(x)
print("Value of e to " + str(iterations) + " iterations: " + str(e))