## Setup
You've seen a few examples of *variables *in our previous code.
Variables are a way to store a value, and change it overtime. Declaring
a variable is easy. Just use the format `name = value`. We can then use
operators to change it's value.
```python
num = 10  # Make a new variable called "num" and set it to 10
num = num * 5  # Multiply "num" by 5 then store it back into "num"
num = num + 10  # Add 10 to "num" then store it back into "num"
print(num)  # print the value of "num"
```
> 60

We can also get input from the user using `input("prompt")`.
```python
firstmultiply = input("First number?")
secondmultiply = input("Second number?")

product = firstmultiply * secondmultiply
print(product)
```
Try running this code, you'll get an error
>TypeError: can't multiply sequence by non-int of type 'str'

Python does lots of things behind the scenes. When you use `input()` the
input is stored as a *string*. A string is a just a chunk of letters.
Examples of strings:
```python
name = "John"
fullname = "John Smith"
favoritefood = input("Favorite food?")
```
Notice how we surround strings with `"` quotes. Now let's take a look at
numbers.
```python
age = 34
money = 5232.32
password = 1234
```
Now when we try to multiply a string and a number, python isn't sure
what to do. So we have to explicitly tell python to *convert* the input
to a number.
```python
firstmultiply = int(input("First number?"))
secondmultiply = int(input("Second number?"))
```
Python now converts the input (a string) into a integer. An integer has
to be a whole number, so use `float()` when you want to store decimal
numbers.

## Reference

| Code          | Description   |
| :------------ |:------------- |
| `float(x)`  | converts x to a float  |
| `int(x)` | converts x to an integer |
| `str(x)`    | converts x to a string|
| `input("prompt")`     | takes input, stores as a string |

## Goal
1. Write any turtle program that makes use of user input