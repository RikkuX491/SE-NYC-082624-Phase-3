import ipdb

# Deliverable # 1 solution code
print("Hello Flatiron! Class is in session!")

# Deliverable # 2 solution code
def add(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 + num2
    else:
        raise TypeError
    
# Deliverable # 3 solution code
def subtract(num1, num2):
    try:
        return num1 - num2
    except TypeError:
        print("Error: num1 and num2 must both be integers or floats!")

# Deliverable # 4 solution code
def multiply(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 * num2
    else:
        raise TypeError
    
# Deliverable # 5 solution code
def divide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        print("Error: num1 and num2 must both be integers or floats!")
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0!")

# Deliverable # 6 solution code
def calculator(operator, num1, num2):
    if(operator == '+'):
        return add(num1, num2)
    elif(operator == '-'):
        return subtract(num1, num2)
    elif(operator == '*'):
        return multiply(num1, num2)
    elif(operator == '/'):
        return divide(num1, num2)
    else:
        raise Exception
    
# Deliverable # 7 solution code
def create_user(username):
    if not (type(username) == str):
        raise TypeError
    elif len(username) < 2:
        raise ValueError
    else:
        print(f"User successfully created! Welcome {username}!")

# Deliverable # 8 solution code
def print_greeting_loop(greeting):
    for char in greeting:
        print(char)