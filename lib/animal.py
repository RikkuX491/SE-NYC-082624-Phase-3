import ipdb

# Bonus Deliverable # 1 solution code
class Animal:

    # Bonus Deliverable # 1 solution code
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Bonus Deliverable # 2 solution code
    def make_animal_sound(self):
        print("Animal Sound!")

# Bonus Deliverable # 3 solution code
class Dog(Animal):

    # Bonus Deliverable # 4 solution code
    def __init__(self, name, age, bark_volume=1, obedience_level=3):
        super().__init__(name, age)
        self.bark_volume = bark_volume
        self.obedience_level = obedience_level

    # Bonus Deliverable # 5 solution code
    def make_animal_sound(self):
        print(f"Bark{'!' * self.bark_volume}")

# Bonus Deliverable # 6 solution code
class Cat(Animal):
    
    # Bonus Deliverable # 7 solution code
    def make_animal_sound(self):
        print("Meow!")