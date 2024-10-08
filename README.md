# Lecture # 3 - Object Oriented Programming in Python

## Lecture Topics

- Classes
- Instances
- Initializing with attributes using `__init__`
- Instance methods
- Self
- Object properties
- Using the `@property` decorator
- Attribute functions: `get_attr()`, `set_attr()`, `has_attr()`, `del_attr()`
- Modifying the `__repr__` instance method for a class
- Object Inheritance
- `super()`

## Introduction

In today's lecture, we will discuss topics of Object Oriented Programming in Python such as classes, instances, `__init__`, attributes, instance methods, `self`, and object properties.

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Deliverables

Write your code in `lib/car.py` (the `car.py` file in the `lib` directory / folder)

1. Create a `Car` class that takes in values for the following parameters for the `__init__` method: `make`, `model`, `year`. The `__init__` method should also take an optional value for the `horn_volume` parameter (set the default value for `horn_volume` to `1`). Write the code to create the appropriate instance variables and assign the values from the input parameters to the appropriate instance variables.
   - The `Car` class should have the following instance variables and values:
     - An instance variable named `make` that has the value of the `make` parameter from the `__init__` method.
     - An instance variable named `model` that has the value of the `model` parameter from the `__init__` method.
     - An instance variable named `year` that has the value of the `year` parameter from the `__init__` method.
     - An instance variable named `horn_volume` that has the value of the `horn_volume` parameter from the `__init__` method.

2. Create a property for the `year` instance variable. For the setter method, the `year` must be an `int` that is between `1900` and `2024`. If the value is not an `int`, raise a `TypeError` with the message `"Year must be an integer!"`. If the value is not between `1900` and `2024`, raise a `ValueError` with the message `"Year must be between 1900 and 2024!"`

3. Create a property for the `horn_volume` instance variable. For the setter method, the `horn_volume` must be an `int` that is between `1` and `10`. If the value is not an `int`, raise a `TypeError` with the message `"Horn Volume must be an integer!"`. If the value is not between `1` and `10`, raise a `ValueError` with the message `"Horn Volume must be between 1 and 10!"`

4. Create a property for the `make` instance variable. For the setter method, the `make` must be a `str` (string) that is at least 3 characters long. If the value is not a `str`, raise a `TypeError` with the message `"Make must be a string!"`. If the value is less than 3 characters long, raise a `ValueError` with the message `"Make must be at least 3 characters long!"`

5. Make an instance method called `honk_horn` that will print a message in the following format: "BEEP BEEP!". The number of exclamation marks '!' should be dependent on the value for the `horn_volume` instance variable. So if `horn_volume` has the value of `3`. There should be 3 exclamation marks `!` after "BEEP BEEP".

## Bonus Deliverables

Write your code in `lib/animal.py` (the `animal.py` file in the `lib` directory / folder)

1. Define the `Animal` class such that an animal is initialized with a `name` and `age`. These should be saved as attributes within the `__init__()` method for the `Animal` class.

```py
fido = Animal("Fido", 2)

fido.name
# "Fido"

fido.age
# 2
```

2. Create an instance method in the `Animal` class, `make_animal_sound()` that will print the following string to the console: `"Animal Sound!"`

```py
fido = Animal("Fido", 2)

fido.make_animal_sound()
# "Animal Sound!"
```

3. Create and define a `Dog` class that inherits from the `Animal` class.

Note: Try creating a `Dog` instance in an `ipdb.set_trace()` session without passing in any arguments when creating the `Dog` instance. You'll notice that we get the following error, even though we haven't defined an `__init__` method for the `Dog` class:

```sh
TypeError: __init__() missing 2 required positional arguments 'name' and 'age'
```

This occurs because the `Dog` class inherits from the `Animal` class and will use the `Animal` class' `__init__` method by default! Since the `Animal` class requires us to pass in arguments for `name` and `age` when creating new `Animal` instances, we will need to pass in arguments for `name` and `age` when creating new `Dog` instances as well, since `Dog` inherits from the `Animal` class. In the next deliverable, we will be creating an `__init__` method for `Dog`, the child class which will allow for the child class to override the parent class' `__init__` method.

4. Create an `__init__()` method for the `Dog` class such that a `Dog` instance is initialized with a `name`, `age`, `bark_volume`, and `obedience_level`. `bark_volume` should be an optional parameter which has a default value of `1`, and `obedience_level` should be an optional parameter which has a default value of `3`. Use the `super()` function to call on the parent class' `__init__()` method (the `__init__()` method from the `Animal` class) and pass in `name` and `age` as arguments to the parent class' `__init__()` method. From there, the parent class' `__init__()` method will handle saving the `name` and `age` attributes for a new `Dog` instance. Save the `bark_volume` and `obedience_level` attributes within the `__init__` method for the `Dog` class.

```py
fido = Dog("Fido", 3)
buddy = Dog("Buddy", 5, 4, 5)

fido.name
# "Fido"

fido.age
# 3

fido.bark_volume
# 1

fido.obedience_level
# 3

buddy.bark_volume
# 4

buddy.obedience_level
# 5
```

5. Create an instance method in the `Dog` class, `make_animal_sound()` that will print the following string to the console: `"Bark"` followed by some exclamation marks `'!'` where the number of exclamation marks should be dependent on the value of the `bark_volume` for the `Dog` instance. For example, if the `Dog` instance's `bark_volume` is 4, the following string should be printed to the console: `"Bark!!!!"`

```py
fido = Dog("Fido", 2, 4, 5)

fido.make_animal_sound()
# "Bark!!!!"
```

6. Create and define a `Cat` class that inherits from the `Animal` class.

Note: Feel free to try creating `Cat` instances in an `ipdb.set_trace()` session, but remember to pass in arguments for `name` and `age` when creating new `Cat` instances since the `Cat` class inherits from the `Animal` class and will use the `Animal` class' `__init__` method by default!

7. Create an instance method in the `Cat` class, `make_animal_sound()` that will print the following string to the console: `"Meow!"`

```py
kitty = Cat("Kitty", 4)

kitty.make_animal_sound()
# "Meow!"
```