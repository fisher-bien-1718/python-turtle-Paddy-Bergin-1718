## Setup

Turtle comes with a lot of functions that can change the way it draws.
For instance, you can change the width of the pen by calling
`t.pensize(x)`

```python
#  Draw a triangle with increasing stroke size
t.pensize(1)
t.forward(100)
t.left(120)
t.pensize(5)
t.forward(100)
t.left(120)
t.pensize(10)
t.forward(100)
```

`t.pencolor("color")` will change the pen color to your choice. Make
sure to use a common name, or just pass in number as `rgb` values.

```python
#  Draw a red triangle
t.pencolor(1.0, 0, 0) # RGB values
t.forward(100)
t.left(120)
t.pencolor("red") # Common name
t.forward(100)
t.left(120)
t.pencolor("#ff0000") # Hex code
t.forward(100)
```
Need to move the turtle but not draw? You can use `penup()` and
 `pendown()` to control the pen.

```
#  Draw an open box
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.penup() #  Lift the pen up
t.forward(100)
t.pendown() #  Put it back down
t.left(90)
t.forward(100)
```
Notice all the `'#'` lines around the code. These are called *comments*
and are ignored when the program is compiled. Use them to describe and
organize your work.
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
1. Draw a yellow sun with rays