## Setup

Writing the same set of instructions over and over isn't very efficient.
Python can help use with the *for loop*. The for loop repeats a block of
code a number of times
```
#  Draw a cube in 3 lines
for x in range(0, 4):
    t.forward(100)
    t.left(90)
```

There are a few important parts to a for loop:
1. The `range()` function decides how many times the loop repeats. In
Python, the loop will start at the first number, and end **before** the
last number. So `range(0, 4)` will execute for `0, 1, 2, 3` but not at 4.
2. Everything inside the loop should be indented with a `tab`. Python
knows when your loop ends based on when you stop identing the code.
3. The variable `x` (you can name it anything else) keeps track of what
loop iteration is running. We'll see an example later.

We can use for loops to make a variety of shapes, easily. Try to guess
what this loop does, then run it to see if you were right.

```
for num in range(0, 5):
    t.forward(100)
    t.right(144)
```
Let's try one more. This one makes uses of the *variable* and even some
multiplication using `*`.

```
for x in range(0, 50):
    t.forward(x * 4)
    t.right(90)
```
One last thing about for loops, you can nest them inside one another. So
we can draw multiple squares in a row. Make sure you indent each line
with the correct number of `tab`s!
```
for _ in range (0, 4): # First loop
    for _ in range(0, 4): # Second loop
        t.forward(100)
        t.left(90)
    t.penup() # This line is outside the second loop, and in the first
    t.forward(200)
    t.pendown()
```
By naming the variable a underscore `_` we are saying "I don't care
about this variable, not planning on using it." Nothing is changed, it's
just a way to communicate to other people.
## Reference

| Code          | Description   |
| :------------ |:------------- |
| `t.forward(x)`  | go forward x units  |
| `t.backward(x)` | go backward x units |
| `t.right(x)`    | turn right x degrees|
| `t.left(x)`     | turn left x degrees |
| `t.pencolor("color")` | change the stroke color |
| `t.pensize(x)` | change the stroke width to x |
| `t.penup()` | lift the pen up so it stops drawing |
| `t.pendown()` | put the pen back down |

## Goals
1. Draw a 3x3 grid of squares (Use as few lines as possible, you'll need
up to 3 for loops!)
2. Draw any pattern that uses the for loop's variable