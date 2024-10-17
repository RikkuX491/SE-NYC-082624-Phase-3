#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

def seed_database():
    Review.drop_table()
    Hotel.drop_table()
    Customer.drop_table()

    Hotel.create_table()
    Customer.create_table()
    Review.create_table()

    # Create seed data
    Hotel.create("Marriott")
    Hotel.create("Waikiki Resort")
    Hotel.create("Bahamas Resort")

    Customer.create("Alice", "Baker")
    Customer.create("Bob", "Carris")
    Customer.create("Cynthia", "Dawson")
    Customer.create("David", "Evans")

    Review.create(5, "Best hotel ever!", 1, 1)
    Review.create(4, "Amazing!", 1, 2)
    Review.create(4, "Great!", 2, 1)
    Review.create(3, "Not as good as the first time I was there.", 1, 1)

seed_database()
print("🌱 Hotels, Customers, and Reviews successfully seeded! 🌱")