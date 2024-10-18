#!/usr/bin/env python3

from helpers import (
    exit_program,
    retrieve_all_hotels,
    find_hotel_by_id,
    create_hotel,
    update_hotel,
    delete_hotel,
    retrieve_reviews_for_hotel,
    retrieve_hotel_that_review_belongs_to
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            retrieve_all_hotels()
        elif choice == "2":
            find_hotel_by_id()
        elif choice == "3":
            create_hotel()
        elif choice == "4":
            update_hotel()
        elif choice == "5":
            delete_hotel()
        elif choice == "6":
            retrieve_reviews_for_hotel()
        elif choice == "7":
            retrieve_hotel_that_review_belongs_to()
        else:
            print("Invalid choice! Please try again!")
        input("\nPress 'return' to continue... ")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Retrieve all hotels")
    print("2. Find hotel by id")
    print("3. Create new hotel")
    print("4. Update a hotel")
    print("5. Delete a hotel")
    print("6. Retrieve associated reviews for a hotel")
    print("7. Retrieve associated hotel that a review belongs to")

if __name__ == "__main__":
    main()