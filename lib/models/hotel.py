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
    
    # add new ORM methods after existing methods
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Hotel instances """

        sql = """
            CREATE TABLE IF NOT EXISTS hotels (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Hotel instances """

        sql = """
            DROP TABLE IF EXISTS hotels
        """

        CURSOR.execute(sql)

    def save(self):
        """ Insert a new row with the name value of the current Hotel instance.
            Update object id attribute using the primary key value of new row.
        """

        sql = """
            INSERT INTO hotels (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Hotel.all.append(self)

    @classmethod
    def create(cls, name):
        """ Initialize a new Hotel instance and save the object to the database """

        hotel = cls(name)
        hotel.save()
        return hotel
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Hotel object having the attribute values from the table row. """
    
        hotel = cls(row[1])
        hotel.id = row[0]
        return hotel
    
    @classmethod
    def get_all(cls):
        """ Return a list containing a Hotel object per row in the table """

        sql = """
            SELECT * FROM hotels
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Hotel object corresponding to the table row matching the specified primary key """

        sql = """
            SELECT * FROM hotels
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        """ Update the table row corresponding to the current Hotel instance. """

        sql = """
            UPDATE hotels
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Hotel instance and remove it from the all class variable """

        sql = """
            DELETE FROM hotels
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Remove the instance from the all class variable
        Hotel.all = [hotel for hotel in Hotel.all if hotel.id != self.id]

    def reviews(self):
        """ Return list of reviews associated with current hotel """

        from models.review import Review

        sql = """
            SELECT * FROM reviews
            WHERE hotel_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Review.instance_from_db(row) for row in rows]
    
    def customers(self):
        """ Return list of customers associated with current hotel """

        from models.customer import Customer

        sql = """
            SELECT customers.id, customers.first_name, customers.last_name FROM customers
            INNER JOIN reviews
            ON customers.id = reviews.customer_id
            INNER JOIN hotels
            ON hotels.id = reviews.hotel_id
            WHERE hotels.id = ?
            GROUP BY customers.id
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Customer.instance_from_db(row) for row in rows]
    
    def __repr__(self):
        return f"<Hotel # {self.id}: Name = {self.name}>"