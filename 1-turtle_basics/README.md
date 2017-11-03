## Setup

We're about to a Python program. Python is a programming
language used for making games, software development and can even create
websites.

Python also comes with turtle, a *module*, that we are going to use to
draw things onto a screen with. Let's look at at a quick example of
Python.

```python
import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
```

Try running that code, and watch what happens. Now, let's
break it down line by line.

```python
import turtle
```

This line imports the "turtle" module, giving us access to it's code.

```python
window = turtle.Screen()
t = turtle.Turtle()
```
Here we create both a window and a turtle. We store both of these into a
*variable*. A variable is a way to store data. It could be a number,
a word, or (in our case) a turtle. Now that we've made a turtle, we can
access it using `t`.

```python
t.forward(100)
t.left(90)
t.forward(100)
```
This is the meat of the program, where we move the turtle around and
draw on the screen. Here we call a *function* of `t`. This function is
another block of code that exists somewhere in the turtle module.
Someone else wrote that function for us, and it probably does a lot of
work for us. However, we just need to know what it does.

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