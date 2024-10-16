from models.__init__ import CONN, CURSOR

class Customer:

    all = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = None

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if(isinstance(first_name_parameter, str)) and (len(first_name_parameter) > 0):
            self._first_name = first_name_parameter
        else:
            raise ValueError("First Name must be a string at least 1 character long!")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if(isinstance(last_name_parameter, str)) and (len(last_name_parameter) > 0):
            self._last_name = last_name_parameter
        else:
            raise ValueError("Last Name must be a string at least 1 character long!")

    def reviews(self):
        pass
    
    def hotels(self):
        pass
    
    # add new ORM methods after existing methods
