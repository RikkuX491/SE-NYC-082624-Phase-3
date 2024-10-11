import ipdb

class Hotel:

    all = []
    
    def __init__(self, name):
        self.name = name
        if len(Hotel.all) == 0:
            self.id = 1
        else:
            last_hotel = Hotel.all[-1]
            last_hotel_id = last_hotel.id
            next_id = last_hotel_id + 1
            self.id = next_id
        Hotel.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and 5 <= len(value) <= 20:
            self._name = value

    # 1-to-many relationship (1 Hotel has many Reviews)
    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
    # Part of the Many-to-many relationship (1 Hotel has many Customers (it's a many-to-many because a Customer also has many Hotels))
    def customers(self):
        return list(set([review.customer for review in Review.all if review.hotel is self]))
    
    def review_texts(self):
        if len(self.reviews()) == 0:
            return None
        else:
            return [review.text for review in self.reviews()]
        
    def average_rating(self):
        rating_list = [review.rating for review in self.reviews()]
        return sum(rating_list) / len(rating_list)
    
    def customers_more_than_three_reviews(self):
        return [customer for customer in self.customers() if self.customer_left_more_than_3_reviews(customer)]
    
    def customer_left_more_than_3_reviews(self, customer):
        if len([review for review in customer.reviews() if review.hotel is self]) > 3:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"<Hotel # {self.id}>"

class Customer:
    
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        if len(Customer.all) == 0:
            self.id = 1
        else:
            last_customer = Customer.all[-1]
            last_customer_id = last_customer.id
            next_id = last_customer_id + 1
            self.id = next_id
        Customer.all.append(self)

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if (not hasattr(self, 'first_name')) and type(value) == str and len(value) > 0:
            self._first_name = value
        # else:
        #     raise Exception("First Name cannot be changed and must be a string that is longer than 0 characters")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if (not hasattr(self, 'last_name')) and type(value) == str and len(value) > 0:
            self._last_name = value

    # 1-to-many relationship (1 Customer has many Reviews)
    def reviews(self):
        return [review for review in Review.all if review.customer is self]
        
    # Part of the Many-to-many relationship (1 Customer has many Hotels (it's a many-to-many because a Hotel also has many Customers))
    def hotels(self):
        return list(set([review.hotel for review in Review.all if review.customer is self]))
    
    def submit_review(self, hotel, rating, text):
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        if len(self.reviews()) == 0:
            return None
        else:
            return [hotel.name for hotel in self.hotels()]
        
    def __repr__(self):
        return f"<Customer # {self.id}>"

class Review:

    all = []
    
    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text
        if len(Review.all) == 0:
            self.id = 1
        else:
            last_review = Review.all[-1]
            last_review_id = last_review.id
            next_id = last_review_id + 1
            self.id = next_id
        Review.all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if (not hasattr(self, 'rating')) and type(value) == int and 1 <= value <= 5:
            self._rating = value

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        if (not hasattr(self, 'text')) and type(value) == str and 3 <= len(value) <= 40:
            self._text = value

    @property
    def hotel(self):
        return self._hotel
    
    @hotel.setter
    def hotel(self, value):
        # if isinstance(value, Hotel):
        if type(value) == Hotel:
            self._hotel = value

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if type(value) == Customer:
            self._customer = value

    def __repr__(self):
        return f"<Review # {self.id}>"

hotel1 = Hotel("Marriott")
hotel2 = Hotel("Hilton Resort")
customer1 = Customer("Alice", "Baker")
customer2 = Customer("Bruce", "Jackson")
review1 = Review(hotel1, customer1, 5, "Best Hotel ever!")
review2 = Review(hotel2, customer1, 4, "Amazing!")
review3 = Review(hotel2, customer2, 5, "Great!")
review4 = Review(hotel1, customer1, 4, "Still pretty good!")
ipdb.set_trace()