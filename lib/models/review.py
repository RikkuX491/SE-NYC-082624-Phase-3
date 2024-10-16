from models.__init__ import CONN, CURSOR

class Review:

    all = []
    
    def __init__(self, rating, text, hotel_id, customer_id):
        self.rating = rating
        self.text = text
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.id = None

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(isinstance(rating_parameter, int)) and (1 <= rating_parameter <= 5):
            self._rating = rating_parameter
        else:
            raise ValueError("Rating must be an integer between 1 and 5!")

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 40):
            self._text = text_parameter
        else:
            raise ValueError("Text must be a string between 3 and 40 characters long!")

    @property
    def hotel_id(self):
        return self._hotel_id
    
    @hotel_id.setter
    def hotel_id(self, hotel_id_parameter):
        if(isinstance(hotel_id_parameter, int)):
            self._hotel_id = hotel_id_parameter
        else:
            raise ValueError("Hotel ID must be an integer!")

    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id_parameter):
        if(isinstance(customer_id_parameter, int)):
            self._customer_id = customer_id_parameter
        else:
            raise ValueError("Customer ID must be an integer!")
        
    def hotel(self):
        pass

    def customer(self):
        pass

    # add new ORM methods after existing methods