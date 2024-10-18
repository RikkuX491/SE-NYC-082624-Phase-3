from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

def exit_program():
    print("Goodbye!")
    exit()

def retrieve_all_hotels():
    print("Here is the information for all of the hotels:")
    for hotel in Hotel.get_all():
        print(hotel)

def find_hotel_by_id():
    id = input("Enter a value for the id for the hotel that you want to find > ")
    hotel = Hotel.find_by_id(id)
    if hotel:
        print(f"Here is the information for Hotel # {id}:")
        print(hotel)
    else:
        print("Error: Hotel Not Found!")

def create_hotel():
    name = input("Enter the name of the new hotel that you want to create > ")
    try:
        new_hotel = Hotel.create(name)
        print("New hotel successfully created! Here is the information for your new hotel:")
        print(new_hotel)
    except ValueError:
        print("Error: Unable to create new hotel since the name must be between 5 and 20 characters long!")

def update_hotel():
    id = input("Enter a value for the id for the hotel that you want to update > ")
    hotel = Hotel.find_by_id(id)
    if hotel:
        name = input("Enter the new name for this hotel > ")
        try:
            hotel.name = name
            hotel.update()
            print(f"Hotel # {id} successfully updated! Here is the information for the updated hotel:")
            print(hotel)
        except:
            print("Error: Unable to update hotel since the name must be between 5 and 20 characters long!")
    else:
        print(f"Error: Unable to update Hotel # {id} since this hotel does not exist!")

def delete_hotel():
    id = input("Enter a value for the id for the hotel that you want to delete > ")
    hotel = Hotel.find_by_id(id)
    if hotel:
        hotel.delete()
        print(f"Hotel # {id} successfully deleted!")
    else:
        print(f"Error: Unable to delete Hotel # {id} since this hotel does not exist!")

# Retrieving data for the 1-to-Many relationship between Hotel and Review (1 Hotel has many Reviews)
def retrieve_reviews_for_hotel():
    id = input("Enter a value for the id for the hotel whose reviews you want to retrieve > ")
    hotel = Hotel.find_by_id(id)
    if hotel:
        hotel_reviews = hotel.reviews()
        if len(hotel_reviews) > 0:
            print(f"Here are the reviews for Hotel # {id}:")
            for review in hotel_reviews:
                print(review)
        else:
            print(f"There are no reviews for Hotel # {id}")
    else:
        print("Error: Hotel Not Found!")

# Retrieving data for the belongs to part of the 1-to-Many relationship between Hotel and Review (Review belongs to a Hotel)
def retrieve_hotel_that_review_belongs_to():
    id = input("Enter a value for the id for the review whose hotel you want to retrieve > ")
    review = Review.find_by_id(id)
    if review:
        associated_hotel = review.hotel()
        if associated_hotel:
            print(f"Here is the information for the hotel that Review # {id} belongs to:")
            print(associated_hotel)
        else:
            print("This review does not belong to a hotel!")
    else:
        print("Error: Review Not Found!")