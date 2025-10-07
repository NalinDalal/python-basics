# Getting Started

Alright let's start with python

install python

## Hello World

```python
print('hello world')
```

## Variables

### Variables & Data Types

In Python, variables are used to store data. You don’t need to declare a variable type — Python infers it automatically.

```python
name = "Nalin"
age = 20
height = 5.9
is_student = True
```

### Working With Strings

Strings are sequences of characters enclosed in quotes.

```python
greeting = "Hello"
name = "World"
print(greeting + " " + name)
print(greeting.lower())
print(greeting.upper())
print(len(greeting))
```

### Working With Numbers

Python supports integers, floats, and complex numbers.

```python
num = 5
print(num + 3)
print(num * 2)
print(num ** 2)  # exponentiation
```

### Getting Input From Users

```python
name = input("Enter your name: ")
print("Hello " + name)
```

### Building a Basic Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 + num2)
```

### Mad Libs Game

```python
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```

### Lists

they are similar to vector in cpp i guess

```python
friends = ["Kevin", "Karen", "Jim"]
print(friends[0])
print(friends[-1])
friends[1] = "Mike"
```

### List Functions

```python
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)
```

### Tuples

```python
coordinates = (4, 5)
print(coordinates[0])
```

### Functions

```python
def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")
```

### Return Statement

```python
def cube(num):
    return num ** 3

print(cube(3))
```

### If Statements

```python
is_male = True
if is_male:
    print("You are a male.")
else:
    print("You are not a male.")
```

### If Statements & Comparisons

```python
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
```

### Building a Better Calculator

```python
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
```

### Dictionaries

```python
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Mar"])
```

### While Loop

```python
i = 1
while i <= 5:
    print(i)
    i += 1

print("Done")
```

### Building a Guessing Game

```python
secret_word = "giraffe"
guess = ""
while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")
```

### For Loops

```python
for letter in "Python":
    print(letter)
```

### Exponent Function

```python
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(2, 3))
```

### 2D Lists & Nested Loops

```python
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)
```

### Building a Translator

```python
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))
```

### Comments

```python
# This is a single-line comment
```

### Try / Except

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
```

### Reading Files

```python
file = open("employees.txt", "r")
print(file.read())
file.close()
```

### Writing to Files

```python
file = open("employees.txt", "a")
file.write("\nToby - HR")
file.close()
```

### Modules & Pip

```bash
pip install requests
```

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

### Classes & Objects

```python
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
```

### Building a Multiple Choice Quiz

```python
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
```

### Object Functions

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def on_honor_roll(self):
        return self.gpa >= 3.5
```

### Inheritance

```python
class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")
```

### Core Topics Recap

- **Functions & Variables**
- **Conditionals**
- **Loops**
- **Exceptions**
- **Libraries**
- **Unit Tests**
- **File I/O**
- **Regular Expressions**
- **Object-Oriented Programming**
- **Et Cetera**
