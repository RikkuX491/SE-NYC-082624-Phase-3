import ipdb

class Car:

    # greeting = "hello flatiron"

    # Deliverable # 2 solution code
    all = []
    
    def __init__(self, make, model, year, horn_volume=1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

        if len(Car.all) == 0:
            self.id = 1
        else:
            # self.id = Car.all[len(Car.all) - 1].id + 1
            # self.id = Car.all[-1].id + 1
            last_car = Car.all[-1]
            last_car_id = last_car.id
            next_id = last_car_id + 1
            self.id = next_id

            # the id should be the next value after the previous car's id (ex: if the last element in the list has an id of 14, the next one should have an id of 15)
            # take a different approach to figure out what the value for the id should be

        # print(Car.greeting)
        # print(Car.all)
        print(self)

        # Deliverable # 2 solution code
        Car.all.append(self)

    @classmethod
    def example_class_method(cls):
        print(cls)

    @classmethod
    def average_year(cls):
        if len(cls.all) == 0:
            print("Error: No cars have been created yet!")
            return None
        else:
            # year_list = [element.year for element in Car.all]
            year_list = [element.year for element in cls.all]
            
            # total = 0
            # for year in year_list:
            #     total += year
            
            # return total / len(year_list)

            return sum(year_list) / len(year_list)
        
    @classmethod
    def get_newest_car(cls):
        return max(cls.all, key=lambda c: c.year)
    
    @classmethod
    def get_oldest_car(cls):
        return min(cls.all, key=lambda c: c.year)

    @classmethod
    def get_list_of_detailed_descriptions(cls):
        return [f"This is a {element.make} car that has the {element.model} model which was created in {element.year}. It's horn volume is {element.horn_volume}" for element in cls.all]

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

    # Deliverable # 1 solution code
    @property
    def model(self):
        return self._model
    
    # Deliverable # 1 solution code
    @model.setter
    def model(self, value):
        if hasattr(self, 'model') or not (type(value) == str):
            raise Exception("Model cannot be changed and must be a string!")
        else:
            self._model = value

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

    def __repr__(self):
        return f"<Car # {self.id}: Make={self.make}, Model={self.model}, Year={self.year}, Horn Volume={self.horn_volume}>"

# ipdb.set_trace()