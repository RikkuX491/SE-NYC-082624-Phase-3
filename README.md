# Lecture # 2 - Python Data Structures

## Lecture Topics

- Sequences (`list`, `tuple`, `str`)
- Sequence functions and methods
- List Comprehensions and Generator Expressions
- Sets
- Dictionaries

## Introduction

In today's lecture, we will discuss Python Data Structures such as sequences, sets, and Dictionaries. We will also practice using List Comprehensions to generate new lists from lists that we are iterating over.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

3. Run `pytest` from inside of the `SE-NYC-TEMPLATE-Phase-3` directory (if you can see `lib`, `Pipfile`, `Pipfile.lock`, `pytest.ini`, and `README.md` in your current working directory, then you are in the correct directory) to run the tests, and begin working to pass the tests. You can also run `pytest -x` to run one test at a time.

## Deliverables

Write your solution code in `lib/app.py` (the `app.py` file which is in the `lib` directory / folder).

1. The `combine_sequences()` function should return a single sequence of the elements of `seq1` followed by the elements of `seq2`.

2. The `sequence_n_times()` function should return a single sequence of `seq` repeated `n` times.

3. The `average()` function should return the average of the numbers in `seq`, the input sequence.

4. The `append_n_times()` function should return a list with an element append to it `n` times. The list is contained within the `input_list` parameter.

5. In `app.py`, there is a list of dictionaries representing different `foods`:

``` python
foods = [
    {
        "name": "Flatburger",
        "price": 9.50
    },
    {
        "name": "French Fries",
        "price": 1.25
    },
    {
        "name": "Burrito",
        "price": 7.25
    }
]
```

Make a List Comprehension that constructs a list containing the names of the foods from the `foods` variable. Store the result of this List Comprehension into a variable called `food_names`.

``` python
food_names
# => ["Flatburger", "French Fries", "Burrito"]
```

6. Make a List Comprehension that constructs a list of the prices of the foods from the `foods` variable. Store the result of this List Comprehension into a variable called `food_prices`. Then, get the average price of the prices in the list stored in the `food_prices` variable and store that result in a variable called `average_price`.

``` python
food_prices
# => [9.5, 1.25, 7.25]
```

``` python
average_price
# => 6.0
```

- Hint: You can use the `average()` function from Deliverable # 3 to help solve this deliverable.

7. In `app.py`, there is a list of dictionaries representing different `animals`.

``` python
animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]
```

Make a List Comprehension that constructs a list such that each item in the list with be in the following format: `{name} is a {animal_type}`, where `{name}` references the name of the animal, and `{animal_type}` references the animal_type of the animal. Store the result of this List Comprehension into a variable called `animal_descriptions`.

``` python
animal_descriptions
# => ["Fido is a Dog", "Kitty is a Cat", "Fluffy is a Guinea Pig"]
```