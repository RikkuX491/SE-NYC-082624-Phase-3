#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from car import *

class TestCarPy:
    '''car.py'''

    def test_car_class_parameters(self):
        '''Car class takes in values for make, model, and year parameters and creates the appropriate instance variables with the correct values'''
        car = Car("Toyota", "Camry", 2000)
        assert(car.make == "Toyota")
        assert(car.model == "Camry")
        assert(car.year == 2000)

    def test_car_class_optional_parameter(self):
        '''Car class takes in an optional value for the horn_volume parameter that has a default value of 1 and creates a horn_volume instance variable that has the value of the horn_volume parameter'''
        car1 = Car("Toyota", "Camry", 2000, 7)
        assert(car1.horn_volume == 7)
        
        car2 = Car("Honda", "Civic", 1999)
        assert(car2.horn_volume == 1)

    def test_year_property_raises_type_error(self):
        '''Car class year property raises TypeError if year is not an integer'''
        with pytest.raises(TypeError):
            Car("Toyota", "Camry", "hello")
        
        with pytest.raises(TypeError):
            Car("Toyota", "Camry", True)

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", [1, 2, 3])

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", (1, 2, 3))

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", {1, 2, 3})

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", {"name": "Alice"})

    def test_year_property_raises_value_error(self):
        '''Car class year property raises ValueError if year is not between 1900 and 2024'''

        with pytest.raises(ValueError):
            Car("Toyota", "Camry", 1899)

        with pytest.raises(ValueError):
            Car("Toyota", "Camry", 2025)

    def test_horn_volume_property_raises_type_error(self):
        '''Car class horn_volume property raises TypeError if horn_volume is not an integer'''
        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, "hello")
        
        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, True)

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, [1, 2, 3])

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, (1, 2, 3))

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, {1, 2, 3})

        with pytest.raises(TypeError):
            Car("Toyota", "Camry", 2000, {"name": "Alice"})

    def test_horn_volume_property_raises_value_error(self):
        '''Car class horn_volume property raises ValueError if horn_volume is not between 1900 and 2024'''
        with pytest.raises(ValueError):
            Car("Toyota", "Camry", 2000, 0)

        with pytest.raises(ValueError):
            Car("Toyota", "Camry", 2000, 11)

    def test_make_property_raises_type_error(self):
        '''Car class make property raises TypeError if make is a string'''
        with pytest.raises(TypeError):
            Car(7, "Camry", 2000, 3)

        with pytest.raises(TypeError):
            Car(True, "Camry", 2000, 3)

        with pytest.raises(TypeError):
            Car([1, 2, 3], "Camry", 2000, 3)

        with pytest.raises(TypeError):
            Car((1, 2, 3), "Camry", 2000, 3)

        with pytest.raises(TypeError):
            Car({1, 2, 3}, "Camry", 2000, 3)

        with pytest.raises(TypeError):
            Car({"name": "Alice"}, "Camry", 2000, 3)

    def test_make_property_raises_value_error(self):
        '''Car class make property raises ValueError if make is less than 3 characters long'''
        with pytest.raises(ValueError):
            Car("", "Camry", 2000, 7)

        with pytest.raises(ValueError):
            Car("T", "Camry", 2000, 7)

        with pytest.raises(ValueError):
            Car("To", "Camry", 2000, 7)

    def test_honk_horn_instance_method_prints_message(self):
        '''Car class honk_horn() instance method prints correct message'''
        car1 = Car("Toyota", "Camry", 2000)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        car1.honk_horn()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "BEEP BEEP!\n")

        car2 = Car("Toyota", "Camry", 2000, 7)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        car2.honk_horn()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "BEEP BEEP!!!!!!!\n")