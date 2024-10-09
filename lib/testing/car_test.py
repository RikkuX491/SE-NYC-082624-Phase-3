#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from car import *

class TestCarPy:
    '''car.py'''

    def test_model_property_raises_exception(self):
        '''Car class model property raises Exception if model already exists and there is an attempt to change its value or if model is not a string'''
        with pytest.raises(Exception):
            car = Car("Toyota", "Camry", 2000)
            car.model = "Corolla"

        with pytest.raises(Exception):
            Car("Honda", 7, 1970)

        with pytest.raises(Exception):
            Car("Honda", True, 1970)

        with pytest.raises(Exception):
            Car("Honda", [1, 2, 3], 1970)

        with pytest.raises(Exception):
            Car("Honda", (1, 2, 3), 1970)

        with pytest.raises(Exception):
            Car("Honda", {1, 2, 3}, 1970)

        with pytest.raises(Exception):
            Car("Honda", {"name": "Alice"}, 1970)

    def test_class_variable_all_is_list(self):
        '''Car class has a class variable named all whose value is a list'''
        assert(type(Car.all) == list)

    def test_init_adds_instance_to_class_variable_all(self):
        '''Car class __init__() method adds instance to all class variable'''
        Car.all = []

        car1 = Car("Toyota", "Camry", 2000, 7)
        assert(len(Car.all) == 1)
        assert(car1 in Car.all)
        
        car2 = Car("Honda", "Civic", 1970)
        assert(len(Car.all) == 2)
        assert(car2 in Car.all)

    def test_average_year_class_method_returns_average_year(self):
        '''Car class average_year() class method returns the average year for all Car instances'''
        Car.all = []

        Car("Toyota", "Camry", 2000, 7)
        assert(Car.average_year() == 2000)
        
        Car("Honda", "Civic", 1970)
        assert(Car.average_year() == 1985)