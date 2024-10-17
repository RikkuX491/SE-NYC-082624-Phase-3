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
    
    # add new ORM methods after existing methods
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Customer instances """
        
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Customer instances """

        sql = """
            DROP TABLE IF EXISTS customers
        """

        CURSOR.execute(sql)

    def save(self):
        """ Insert a new row with the first_name and last_name values of the current Customer instance.
            Update object id attribute using the primary key value of new row.
        """

        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Customer.all.append(self)

    @classmethod
    def create(cls, first_name, last_name):
        """ Initialize a new Customer instance and save the object to the database """

        customer = cls(first_name, last_name)
        customer.save()
        return customer
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Customer object having the attribute values from the table row. """
    
        customer = cls(row[1], row[2])
        customer.id = row[0]
        return customer
    
    @classmethod
    def get_all(cls):
        """ Return a list containing a Customer object per row in the table """

        sql = """
            SELECT * FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Customer object corresponding to the table row matching the specified primary key """

        sql = """
            SELECT * FROM customers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        """ Update the table row corresponding to the current Customer instance. """

        sql = """
            UPDATE customers
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Customer instance and remove it from the all class variable """

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the instance from the all class variable
        Customer.all = [customer for customer in Customer.all if customer.id != self.id]
    
    def reviews(self):
        """ Return list of reviews associated with current customer """

        from models.review import Review

        sql = """
            SELECT * FROM reviews
            WHERE customer_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Review.instance_from_db(row) for row in rows]
    
    def hotels(self):
        """ Return list of hotels associated with current customer """

        from models.hotel import Hotel

        sql = """
            SELECT hotels.id, hotels.name FROM hotels
            INNER JOIN reviews
            ON hotels.id = reviews.hotel_id
            INNER JOIN customers
            ON customers.id = reviews.customer_id
            WHERE customers.id = ?
            GROUP BY hotels.id
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Hotel.instance_from_db(row) for row in rows]
    
    def __repr__(self):
        return f"<Customer # {self.id}: First Name = {self.first_name}, Last Name = {self.last_name}>"