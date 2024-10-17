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
        if(isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 50):
            self._text = text_parameter
        else:
            raise ValueError("Text must be a string between 3 and 50 characters long!")

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

    # add new ORM methods after existing methods
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """

        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                rating INTEGER,
                text TEXT,
                hotel_id INTEGER,
                customer_id INTEGER
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review instances """

        sql = """
            DROP TABLE IF EXISTS reviews
        """

        CURSOR.execute(sql)

    def save(self):
        """ Insert a new row with the rating, text, hotel_id and customer_id values of the current Review instance.
            Update object id attribute using the primary key value of new row.
        """

        sql = """
            INSERT INTO reviews (rating, text, hotel_id, customer_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.rating, self.text, self.hotel_id, self.customer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Review.all.append(self)

    @classmethod
    def create(cls, rating, text, hotel_id, customer_id):
        """ Initialize a new Review instance and save the object to the database """

        review = cls(rating, text, hotel_id, customer_id)
        review.save()
        return review
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Review object having the attribute values from the table row. """

        review = cls(row[1], row[2], row[3], row[4])
        review.id = row[0]
        return review
    
    @classmethod
    def get_all(cls):
        """ Return a list containing a Review object per row in the table """

        sql = """
            SELECT * FROM reviews
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Review object corresponding to the table row matching the specified primary key """

        sql = """
            SELECT * FROM reviews
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        """ Update the table row corresponding to the current Review instance. """

        sql = """
            UPDATE reviews
            SET rating = ?, text = ?, hotel_id = ?, customer_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.rating, self.text, self.hotel_id, self.customer_id, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Review instance and remove it from the all class variable """

        sql = """
            DELETE FROM reviews
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the instance from the all class variable
        Review.all = [review for review in Review.all if review.id != self.id]
    
    def hotel(self):
        """ Return hotel instance associated with current review """

        from models.hotel import Hotel

        sql = """
            SELECT hotels.id, hotels.name FROM hotels
            INNER JOIN reviews
            ON hotels.id = reviews.hotel_id
            WHERE reviews.hotel_id = ?
            GROUP BY hotels.id
        """

        row = CURSOR.execute(sql, (self.hotel_id,)).fetchone()

        if row:
            return Hotel.instance_from_db(row)
        else:
            return None

    def customer(self):
        """ Return customer instance associated with current review """

        from models.customer import Customer

        sql = """
            SELECT customers.id, customers.first_name, customers.last_name FROM customers
            INNER JOIN reviews
            ON customers.id = reviews.customer_id
            WHERE reviews.customer_id = ?
            GROUP BY customers.id
        """

        row = CURSOR.execute(sql, (self.customer_id,)).fetchone()

        if row:
            return Customer.instance_from_db(row)
        else:
            return None
        
    def __repr__(self):
        return f"<Review # {self.id}: Rating = {self.rating}, Text = {self.text}, Hotel ID = {self.hotel_id}, Customer ID = {self.customer_id}>"