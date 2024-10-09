import ipdb

class Car:
    
    def __init__(self, make, model, year, horn_volume=1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        if not (type(value) == str):
            raise TypeError("Make must be a string!")
        elif len(value) < 3:
            raise ValueError("Make must be at least 3 characters long!")
        else:
            self._make = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not (type(value) == int):
            raise TypeError("Year must be an integer!")
        elif not (1900 <= value <= 2024):
            raise ValueError("Year must be between 1900 and 2024!")
        else:
            self._year = value

    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, value):
        if not (type(value) == int):
            raise TypeError("Horn Volume must be an integer!")
        elif not (1 <= value <= 10):
            raise ValueError("Horn Volume must be between 1 and 10!")
        else:
            self._horn_volume = value

    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")