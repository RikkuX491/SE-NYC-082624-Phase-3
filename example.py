import ipdb

VALID_SIZES = ["Small", "Medium", "Large"]

class Example:
    
    def __init__(self):
        print("New Example created!")
        # print(self)
        self.name = "Bob"
        self.another_property = True

class Toy:
    
    def __init__(self, color, size="Small", year=2024):
        print("In Toy class' __init__ method...")
        # print("New Toy created!")
        self.color = color
        self.size = size
        self.year = year

    def get_color(self):
        # print("Calling the Getter method for the color instance variable!")
        return self._color

    def set_color(self, value):
        # print("Calling the Setter method for the color instance variable!")
        # print(value)
        if type(value) == str:
            self._color = value
        else:
            raise TypeError("Color must be a String value!")

    # Using the property function to make the color instance variable into a property
    color = property(get_color, set_color)

    # Using the @property decorator to make the size instance variable into a property
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in VALID_SIZES:
            self._size = value
        else:
            raise ValueError("Size must be either Small, Medium, or Large!")
        
    @property
    def year(self):
        # print("Calling the Getter method for year!")
        return self._year
    
    @year.setter
    def year(self, value):
        # print("Calling the Setter method for year!")
        # if hasattr(self, 'year'):
        #     raise Exception("Year cannot be changed!")
        # else:
        #     self._year = value
        if not (hasattr(self, 'year')):
            self._year = value
        else:
            raise Exception("Year cannot be changed!")

    def make_sound(self):
        print("BEEP!")

    def __repr__(self):
        return f"<Toy: Color={self.color}, Size={self.size}, Year={self.year}>"
    
# ToyCar inherits from the Toy class
class ToyCar(Toy):

    def __init__(self, color, size="Small", year=2024, horn_volume=1):
        print("In ToyCar class' __init__ method...")
        super().__init__(color, size, year)
        self.horn_volume = horn_volume

    def make_sound(self):
        print("HONK HONK!")
    
    def __repr__(self):
        return f"<ToyCar: Color={self.color}, Size={self.size}, Year={self.year}, Horn Volume={self.horn_volume}>"

# example1 = Example()
# print(example1)
# print(example1.name)
# print(example1.another_property)
# print(example1 is example1)

# example2 = Example()
# print(example2)
# print(example1 is example2)

toy1 = Toy("Red")
# print(toy1)
print(toy1.color)
# print(toy1.size)
toy1.make_sound()

toy2 = Toy("Blue", "Large")
# print(toy2)
print(toy2.color)
# print(toy2.size)

# toy3 = Toy(7)
# toy3 = Toy("Green", "Hello")
# print(toy3.color)

toycar1 = ToyCar("Yellow", "Medium", 1995)

ipdb.set_trace()