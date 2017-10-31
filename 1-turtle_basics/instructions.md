## Setup

We're about to write your first Python program. Python is a programming
language used for making games, software development and even websites.

Python also comes with turtle, a *module*, that we are going to use to
draw things onto a screen with. Let's look at at a quick example of
Python.

```
import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
```

Try running that code, and see what is output to the screen. Now, let's
break it down line by line.

```
import turtle
```

This line imports the "turtle" module, giving us access to it's code.

```
window = turtle.Screen()
t = turtle.Turtle()
```
Here we create both a window and a turtle. We store both of these into a
*variable*. A variable is a way to store data. It could be a number,
a word, or (in our case) a turtle. Now that we've made a turtle, we can
access it using `t`.

```
t.forward(100)
t.left(90)
t.forward(100)
```
Now for the important part of the program. Here we call a *function* of
`t`. This function is another block of code that exists somewhere in the
turtle module. We don't know what it is exactly, but we don't need to.

## Reference

| Code          | Description   |
| :------------ |:------------- |
| `t.forward(x)`  | go forward x units  |
| `t.backward(x)` | go backward x units |
| `t.right(x)`    | turn right x degrees|
| `t.left(x)`     | turn left x degrees |

## Goals
1. Finish drawing the cube
2. Draw a triangle with a right angle
3. Draw a hexagon with 60 degree angles