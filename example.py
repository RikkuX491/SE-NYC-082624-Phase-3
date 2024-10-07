import ipdb

# print("Hello Flatiron!")

name = "Alice"
# print(name)

# name = "Bob"
# print(name)

number1 = 7

# ipdb.set_trace()

number2 = "4"

# ipdb.set_trace()

# print(number1 + number2)

# number3 = 45.34

# print(type(number1))
# print(type(number2))
# print(type(number3))

location = "park"

# print(f'{name} went to the {location} today')

# print(True)
# print(False)
# print(type(True))
# print(type(False))

# print(not not "")
# print(not not 0)
# print(not "hello")
# print(not not "hello")
# print(not True)
# print(not False)

# print(7 or 14)
# print(not not 7)
# print(0 or 14)
# print(not not 0)

# print(7 and 14)
# print(not not 7)

# print(not not "")
# print("" and 34)

# print(not not None)
# print(None and 34)

# print(4 + 5 * 7)
# print((4 + 5) * 7)

# print(name == "Bob")

# print([1, 2, 3] == [1, 2, 3])
# print([1, 2, 3] is [1, 2, 3])

# name = "Eve"

# if name == "Bob":
#     print(f"Hi {name}!")
# elif name == "Alice":
#     print(f"Good morning, {name}!")
# else:
#     print("Goodbye!")

# if name == "Alice" or name == "Bob":
#     print(f"Hi {name}!")
# else:
#     print("Goodbye!")

# if name in ["Alice", "Bob"]:
#     print(f"Hi {name}!")
# else:
#     print("Goodbye!")

# counter = 10

# while counter > 0:
    # print(counter)
    # counter -= 1

# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

def greet_user(username):
    print(f"Hello {username}!")

# greet_user("John")
# greet_user("Alice")

def get_username_and_greeting(username):
    return f"Hello {username}!"

# username_with_greeting = get_username_and_greeting("Bob")
# print(username_with_greeting)

def test_function():
    sum = 4 + 5

# print(test_function())

# number3 = "hello"
# number4 = "world"

# number3 = 34.4
# number4 = 2

# if(type(number3) == int or type(number3) == float) and (type(number4) == int or type(number4) == float):
#     print(number3 + number4)
# else:
#     raise TypeError("number3 and number4 must both be integers or floats!")

# if(type(number3) in [int, float]) and (type(number4) in [int, float]):
#     print(number3 + number4)
# else:
#     raise TypeError("number3 and number4 must both be integers or floats!")

def add_and_print_sum(number3, number4):
    if(type(number3) in [int, float]) and (type(number4) in [int, float]):
        print(number3 + number4)
    else:
        # raise Exception("number3 and number4 must both be integers or floats!")
        raise TypeError("number3 and number4 must both be integers or floats!")
    
# add_and_print_sum(2, 3)
# add_and_print_sum(2.6, 7.2)
# add_and_print_sum("2.6", 7)
# add_and_print_sum("hello", "world")

def create_user(username):
    if not (type(username) == str):
        raise TypeError("username must be a string!")
    elif len(username) < 2:
        raise ValueError("username must be at least 2 characters long!")
    else:
        print(f"User successfully created! Welcome {username}!")


# create_user("Alex")
# create_user("")
# create_user("A")
# create_user(34)

value1 = 78
value2 = "hello"

try:
    print(value1 + value2)
except:
    print("value1 and value2 must both be integers or floats!")


print("Reached the end of the program!")