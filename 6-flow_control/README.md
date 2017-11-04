## Setup
So far our programs have run from top to bottom, executing each line in
order. But what if we need to change the flow? So far, we've learned
about the *for loop*. The for loop repeats code a certain number of
times. Here we'll look at two more examples of flow control, the *if*
and *while* statements. But first, we need to understand how to make
decisions.

#### Booleans
A *boolean* is the most simple type of data possible. It can either be
`True` or `False`. In fact, we can store booleans in a variable.
```python
choice = True
```
We can also use math operators to make booleans. Check below for a full
table.
```python
decision = 10 + 30 > 10 * 30
print(decision)
```
> False

We can also check if things are equal to each other.
```python
password = input("Input password: ")
print(password == "1234")
```
Note that we use a double equal sign here `==`. If the user input the password 1234, the output would be >True. Remember that:
- A single equals `=` is for **assignment**
- A double equals `==` is for **comparison**

Use `and` and `or` to combine multiple booleans.
```python
thing = 5 > 0 or 10 == 5 * 3
print(thing)
```
> True


#### `if` statements
An if statement is very simple, it executes a block of code if a boolean
is `True`. We can also add an `else` to the end of a `if`.
```python
password = input("Input password: ")
if password == "1234":
    print("Access granted")
else:
    print("Access denied")
```
Combine multiple `if`s into a single one using `elif`
```python
age = int(input("How old are you?"))
if age > 16:
    print("Can drive")
elif age == 15:
    print("Can get a permit")
elif age < 15 and age >= 0:
    print("Cannot drive")
else:
    print("Invalid age")
```

#### `while` statements
While statements run a block of code *until* a condition is not `True`.
```python
from random import randint
number = randint(1, 100)
guess = 0
while (guess != number):
    guess = int(input("What's my number? (1-100)"))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("You got it!")
```

## Reference
| Code          | Description   |
| :------------ |:------------- |
| `==`  | equals  |
| `!=` | does not equal |
| `>`    | greater than |
| `>=`     | greater than or equal to |
| `<` | less than |
| `<=` | less than or equal to |
| `and` | `True` if both sides are `True` |
| `or` | `True` if at least one side is `True` |
