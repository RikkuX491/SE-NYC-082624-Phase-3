from models.__init__ import CONN, CURSOR

class Hotel:

    all = []
    
    def __init__(self, name):
        self.name = name
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (5 <= len(name_parameter) <= 20):
            self._name = name_parameter
        else:
            raise ValueError("Name must be a string between 5 and 20 characters long!")

    def reviews(self):
        pass
    
    def customers(self):
        pass
    
    # add new ORM methods after existing methods