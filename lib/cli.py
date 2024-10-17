#!/usr/bin/env python3

from helpers import (
    exit_program,
    option_1_function,
    option_2_function
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            option_1_function()
        elif choice == "2":
            option_2_function()
        else:
            print("Invalid choice! Please try again!")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Option 1")
    print("2. Option 2")

if __name__ == "__main__":
    main()