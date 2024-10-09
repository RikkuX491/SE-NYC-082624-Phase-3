import ipdb

# Deliverable # 1 solution code
class Car:
    
    # Deliverable # 1 solution code
    def __init__(self, make, model, year, horn_volume=1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

    # Deliverable # 2 solution code
    @property
    def year(self):
        return self._year
    
    # Deliverable # 2 solution code
    @year.setter
    def year(self, value):
        if not (type(value) == int):
            raise TypeError("Year must be an integer!")
        elif not (1900 <= value <= 2024):
            raise ValueError("Year must be between 1900 and 2024!")
        else:
            self._year = value

    # Deliverable # 3 solution code
    @property
    def horn_volume(self):
        return self._horn_volume
    
    # Deliverable # 3 solution code
    @horn_volume.setter
    def horn_volume(self, value):
        if not (type(value) == int):
            raise TypeError("Horn Volume must be an integer!")
        elif not (1 <= value <= 10):
            raise ValueError("Horn Volume must be between 1 and 10!")
        else:
            self._horn_volume = value

    # Deliverable # 4 solution code
    @property
    def make(self):
        return self._make
    
    # Deliverable # 4 solution code
    @make.setter
    def make(self, value):
        if not (type(value) == str):
            raise TypeError("Make must be a string!")
        elif len(value) < 3:
            raise ValueError("Make must be at least 3 characters long!")
        else:
            self._make = value

    # Deliverable # 5 solution code
    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")