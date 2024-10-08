import ipdb
import sys

# Sequences

# Lists []
hotels = ["Marriott", "Hilton"]
# print(hotels)

hotels.append("Four Seasons")
# print(hotels)

# print(hotels[0])

hotels[0] = "Hawaii Resort"
# print(hotels[0])
# print(hotels[1])
# print(hotels)

hotels = hotels + ["Bahamas Resort", "Disney World Resort"]
# print(hotels)
hotels.pop()
# print(hotels)

# print(len(hotels))

# for element in hotels:
#     print(element)

# first_characters_list = []
# for element in hotels:
#     first_characters_list.append(element[0])
# first_characters_list = [element[0] for element in hotels]
# first_characters_list = [element for element in hotels if element[0] == "H"]
# first_characters_list = [element[0] for element in hotels if element[0] == "H"]
# print(first_characters_list)

# return_first_character = lambda hotel_name: hotel_name[0]

# map_result = map(lambda hotel_name: hotel_name[0], hotels)
# map_result = map(return_first_character, hotels)
# new_list = list(map_result)
# print(new_list)

# first_character_is_H = lambda hotel_name: hotel_name[0] == "H"

# filter_result = filter(lambda hotel_name: hotel_name[0] == "H", hotels)
# filter_result = filter(first_character_is_H, hotels)
# new_list = list(filter_result)
# print(new_list)

# Converting a list to a tuple
# print(tuple(hotels))

# Tuples ()
# airlines = "JetBlue", "Delta"
airlines = ("JetBlue", "Delta")
# print(airlines)

# print(airlines[0])
# print(airlines[1])

airlines = airlines + ("Hawaiian Airlines", "Emirates")
# print(airlines)
# print(len(airlines))

# for element in airlines:
#     print(element)

# map_result = map(lambda airline: airline[0], airlines)
# new_tuple = tuple(map_result)
# print(new_tuple)

# filter_result = filter(lambda airline: airline[0] == 'J', airlines)
# new_tuple = tuple(filter_result)
# print(new_tuple)

# Converting a tuple to a list
# print(list(airlines))

# Strings ""
greeting = "hello flatiron"
# print(greeting)
# print(greeting[0])
# print(len(greeting))

# for char in greeting:
#     print(char)

# Generator expressions
countries = ["United States", "United Kingdom", "Greece", "Ecuador", "Antigua", "Bahamas", "Spain", "Mexico", "Japan"]
# print(countries)
# print(f"The list size is: {sys.getsizeof(countries)}")

generator_expression_of_countries = (country for country in countries)
# print(generator_expression_of_countries)
# print(f"The generator expression size is: {sys.getsizeof(generator_expression_of_countries)}")

list_result = list(generator_expression_of_countries)
# print(list_result)
# print(sys.getsizeof(list_result))

new_list = [element for element in generator_expression_of_countries]
# print(new_list)
# print(sys.getsizeof(new_list))

# Sets
playing_cards = {'7 of hearts', 'ace of spades'}
# print(playing_cards)
# print(type(playing_cards))

fruits = ["apple", "apple", "banana", "banana"]
# print(fruits)

# Converting list to a set to remove the duplicate fruit data
fruits_set = set(fruits)
# print(fruits_set)

# Converting the set back to a list to get a list that does not contain duplicate data
fruits_list_without_duplicates = list(fruits_set)
# print(fruits_list_without_duplicates)

person = {
    'name': "Alice"
}
# print(person)

person['age'] = 23
# print(person)

person['name'] = "Eve"
# print(person)

person['is_student'] = True
# print(person)

person.update({
    'name': "Bob",
    'age': 34
})
# print(person)

person.update({
    'phone_number': '1234567890',
    'email': "bob@gmail.com"
})
# print(person['name'])
# print(person['age'])
# print(person)

# Iterating over the keys in a dictionary using the for in loop
# for key in person:
    # print(key)
    # print(person[key])

def combine_sequences(seq1, seq2):
    pass

def sequence_n_times(seq, n):
    pass

def average(seq):
    pass

def append_n_times(input_list, element, n):
    pass

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