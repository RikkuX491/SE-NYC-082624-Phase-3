import ipdb

# Deliverable # 1 solution code
def combine_sequences(seq1, seq2):
    return seq1 + seq2

# Deliverable # 2 solution code
def sequence_n_times(seq, n):
    return seq * n

# Deliverable # 3 solution code
def average(seq):
    return sum(seq) / len(seq)

# Deliverable # 4 solution code
def append_n_times(input_list, element, n):
    for i in range(n):
        input_list.append(element)
    return input_list

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

# Deliverable # 5 solution code
food_names = [element['name'] for element in foods]

# Deliverable # 6 solution code
food_prices = [element['price'] for element in foods]
average_price = average(food_prices)

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

# Deliverable # 7 solution code
animal_descriptions = [f"{element['name']} is a {element['animal_type']}" for element in animals]