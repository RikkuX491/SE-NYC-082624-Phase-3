# Lecture # 1 - Python Fundamentals

## Lecture Topics

- pipenv install
- pipenv shell
- pytest
- pytest -x
- Debugging with `print()` and `ipdb.set_trace()`
- Python data types (`str`, `int`, `float`, `bool`, `None`)
- Control Flow: Operators, Conditional Statements, Loops
- Functions in Python
- Using `raise Exception` to raise an Exception
- Using `raise TypeError` to raise an TypeError
- Using `raise ValueError` to raise a ValueError
- Handling errors with `try` and `except`

## Introduction

Welcome to Python! In today's lecture, we will discuss the Python Fundamentals including important terminal commands, using `ipdb` for debugging, control flow, functions, using `raise Exception` to raise an Exception, and using `raise ValueError` to raise a ValueError.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required libraries.

2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

3. Run `pytest` from inside of the `SE-NYC-TEMPLATE-Phase-3` directory to run the tests (if you can see `lib`, `Pipfile`, `Pipfile.lock`, `pytest.ini`, and `README.md` in your current working directory, then you are in the correct directory), and begin working to pass the tests. You can also run `pytest -x` to run one test at a time.

## Deliverables

Write your solution code in `lib/app.py` (the `app.py` file which is in the `lib` directory / folder).

1. Use the `print()` function to print the string `"Hello Flatiron! Class is in session!"`

2. Create a function named `add()` that has two parameters named `num1` and `num2`. The value of the two parameters should be either integers or floats. The `add()` function should add the two numbers and return the sum of the two numbers. If the value of either of the two parameters (`num1` and `num2`) is not an integer or float value, the `add()` function should raise a `TypeError` (using `raise TypeError`)

3. Create a function named `subtract()` that has two parameters named `num1` and `num2`. The value of the two parameters should be either integers or floats. The `subtract()` function should subtract the 2nd number from the 1st number and return the difference of the two numbers. In other words, `num1 - num2`. Use `try` and `except` blocks to handle `TypeError` exceptions that may occur if `num1` and/or `num2` are not both integers or floats. Within the `except` block, use the `print()` function to print the string `"Error: num1 and num2 must both be integers or floats!"`

4. Create a function named `multiply()` that has two parameters named `num1` and `num2`. The value of the two parameters should be either integers or floats. The `multiply()` function should multiply the two numbers and return the product of the two numbers. If the value of either of the two parameters (`num1` and `num2`) is not an integer or float value, the `add()` function should raise a `TypeError` (using `raise TypeError`)

5. Create a function named `divide()` that has two parameters named `num1` and `num2`. The value of the two parameters should be either integers or floats, and the value of the second parameter cannot be equal to 0. The `divide()` function should divide the 2nd number from the 1st number and return the quotient of the two numbers. In other words, `num1 / num2`. Use `try` and `except` blocks to handle `TypeError` that may occur if `num1` and/or `num2` are not both integers or floats, and `ZeroDivisionError` exceptions that may occur if `num2` is equal to `0`. There should be two `except` blocks used, one to handle `TypeError`, and the other to handle `ZeroDivisionError`. Within the `except TypeError` block, use the `print()` function to print the string `"Error: num1 and num2 must both be integers or floats!"`. Within the `except ZeroDivisionError` block, use the `print()` function to print the string `"Error: num2 cannot be equal to 0!"`

6. Create a function named `calculator()` that has three parameters named `operator`, `num1`, and `num2`. The value of the first parameter (`operator`) should be a string with the value of `+`, `-`, `*`, or `/` since it represents the operation to be performed on two numbers. The value of the second and third parameters (`num1` and `num2`) should be either integers or floats. The `calculator()` function should perform the operation (`+`, `-`, `*`, or `/`) specified by the value of the first parameter on the second and third parameters (the numbers) and return the result. The `calculator()` function should raise a `Exception` (using `raise Exception`) if the first parameter has any other value that is not equal to `+`, `-`, `*`, or `/`.

7. Create a function named `create_user()` that has one parameter named `username`. The value of the `username` parameter should be a string that is at least 2 characters in length. The `create_user()` should use the `print()` function to print a string in the format: `"User successfully created! Welcome {username}!"`, where `{username}` represents the value of the `username` parameter that should be incorporated into the string using string interpolation or string concatenation. The `create_user()` function should raise a `TypeError` (using `raise TypeError`) if the `username` parameter is not a string. The `create_user()` function should raise a `ValueError` (using `raise ValueError`) if the `username` parameter is a string that has a length that is less than 2 characters.

8. Create a function named `print_greeting_loop()` that has one parameter named `greeting`. The value of the `greeting` parameter should be a string. The `print_greeting_loop()` should print each character of the string separately.

- Hint 1: You can use the `print()` function to print a value.
- Hint 2: You can use a `for` loop to iterate through a string's characters.

---


| Python                                                                                               | Javascript                                                                                   |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| None                      | undefined/null    |
| &&                        | and               |
| \|\|                      | or                |
| True/False                | true/false           |
| ipdb.set_trace()          | debugger          |
| snake_case                | camelCase         |
| f"{interpolate}"    | \`${interpolate}\`       |
| "true result" if "condition" else "default result"   | "condition" ? "true result" : "default result"   |
| if...elif...else    | if...else if...else    |
| try...except... | try...catch...  |
| def:                     | function{}         |
| If a function has parameters you have to pass in arguments for those parameters (otherwise you can set a default) | If a function has parameters JavaScript will not throw errors if you do not pass in arguments for said parameters |
| Variables need to immediately be assigned a value when created | Variables do not need to be immediately assigned a value when created |