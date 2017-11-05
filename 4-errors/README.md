## Setup
There are a number of errors in `fixme.py`. Some are *syntax* errors and
some are *logical* errors. A syntax error is pretty easy to spot. Python
will read out an error, and show you where it went wrong.
```python
import turtle

tur = turtle.Turtle()

tur.forward(100)
tur.leeft(90)
```

Python complains:
> Traceback (most recent call last):
>
> File "fixme.py", line 6, in <module>
>    tur.leeft(90)
>
> AttributeError: 'Turtle' object has no attribute 'leeft'

Here we can tell that the function "leeft()" does not exist, and can fix
our typo. Sometimes they can be more subtle:

```python
tur.forward(100)
tur.left()
```

>TypeError: left() missing 1 required positional argument: 'angle'

Here we forgot to specify what angle to rotate, so Python complains.

A logical error is different. Python won't complain when you make a
logical error, instead you will receive an unexpected output.

```python
x = 6
y = 8
print("The average of 6 and 8 is:")
print(x+y/2)
```

>The average of 6 and 8 is:
>
>10.0

This is an example of forgetting order of operations. Python follows
PEMDAS and does division before addition. So it reads `x+y/2` as
 `x+(y/2)`. We can fix this by adding in our own parenthesis.
```python
print((x+y)/2)
```
> 7.0

Now that you've seen some examples, try opening up `fixme.py` and fixing
the errors. There's no harm in running the file to help locate the
errors.