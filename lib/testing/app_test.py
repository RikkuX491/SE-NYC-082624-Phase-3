#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from app import *

class TestAppPy:
    '''app.py'''

    def test_prints_hello_world(self):
        '''prints "Hello Flatiron! Class is in session!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello Flatiron! Class is in session!\n")

    def test_add(self):
        '''add() takes two input args, adds them, and returns the sum.'''
        assert(add(7, 14) == 21)
        assert(add(3.4, 5.2) == 8.6)

    def test_add_raises_type_error(self):
        '''add() raises TypeError when the two input args for add() are not both numbers (integers or floats).'''
        with pytest.raises(TypeError):
            add("hello", 41)

        with pytest.raises(TypeError):
            add(4.3, "flatiron")

        with pytest.raises(TypeError):
            add("hello", "flatiron")

    def test_subtract(self):
        '''subtract() takes two input args, subtracts the 2nd input arg from the 1st input arg, and returns the difference.'''
        assert(subtract(28, 21) == 7)
        assert(subtract(7.2, 2.3) == 4.9)

    def test_subtract_handles_type_error(self):
        '''subtract() handles TypeError when the two input args for subtract() are not both numbers (integers or floats).'''
        subtract("hello", 82)
        subtract(2.7, "flatiron")
        subtract("hello", "flatiron")

    def test_subtract_prints_error_message(self):
        '''subtract() prints error message when handling TypeError.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        subtract("hello", "flatiron")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Error: num1 and num2 must both be integers or floats!\n")

    def test_multiply(self):
        '''multiply() takes two input args, multiplies them, and returns the product.'''
        assert(multiply(7, 7) == 49)
        assert(multiply(4.5, 2) == 9.0)

    def test_multiply_raises_type_error(self):
        '''multiply() raises TypeError when the two input args for multiply() are not both numbers (integers or floats).'''
        with pytest.raises(TypeError):
            multiply("hello", 77)

        with pytest.raises(TypeError):
            multiply(5.4, "flatiron")

        with pytest.raises(TypeError):
            multiply("hello", "flatiron")

    def test_divide(self):
        '''divide() takes two input args, the 2nd input arg from the 1st input arg, and returns the quotient.'''
        assert(divide(70, 7) == 10.0)
        assert(divide(3.2, 2) == 1.6)

    def test_divide_handles_type_error(self):
        '''divide() handles TypeError when the two input args for divide() are not both numbers (integers or floats).'''
        divide("hello", 707)
        divide(2.3, "flatiron")
        divide("hello", "flatiron")

    def test_divide_handles_zero_division_error(self):
        '''divide() handles ZeroDivisionError when the 2nd input arg for divide() is 0.'''
        divide(32, 0)

    def test_divide_prints_type_error_message(self):
        '''divide() prints error message when handling TypeError.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        divide("hello", "flatiron")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Error: num1 and num2 must both be integers or floats!\n")

    def test_divide_prints_zero_division_error_message(self):
        '''divide() prints error message when handling ZeroDivisionError.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        divide(7, 0)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Error: num2 cannot be equal to 0!\n")

    def test_calculator(self):
        '''calculator() performs the operation (+, -, *, or /) specified by the first input arg on the second and third input args and returns the result.'''
        assert(calculator('+', 10, 5) == 15)
        assert(calculator('-', 20, 15) == 5)
        assert(calculator('*', 30, 3) == 90)
        assert(calculator('/', 100, 4) == 25.0)
    
    def test_validates_calculator(self):
        '''operation is +, -, *, or /. raises Exception if any other value is passed into calculator as the input arg for operation.'''
        with pytest.raises(Exception):
            calculator('$', 1, 2)

        with pytest.raises(Exception):
            calculator(True, 1, 2)

    def test_create_user(self):
        '''create_user() takes an input arg with the value for a username and prints a message confirming that the user has been successfully created'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        create_user("Alice")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "User successfully created! Welcome Alice!\n")

        captured_out = io.StringIO()
        sys.stdout = captured_out
        create_user("Bob")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "User successfully created! Welcome Bob!\n")

    def test_create_user_raises_type_error(self):
        '''create_user() raises TypeError when the input arg for create_user() is not a string'''
        with pytest.raises(TypeError):
            create_user(7)

        with pytest.raises(TypeError):
            create_user(True)

    def test_create_user_raises_value_error(self):
        '''create_user() raises ValueError when the input arg for create_user() is a string that is less than 2 characters in length'''
        with pytest.raises(ValueError):
            create_user('')
        
        with pytest.raises(ValueError):
            create_user('a')

    def test_print_greeting_loop(self):
        '''print_greeting_loop() prints each character of a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_greeting_loop("hello flatiron")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "h\ne\nl\nl\no\n \nf\nl\na\nt\ni\nr\no\nn\n")
