#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from app import *

class TestAppPy:
    '''app.py'''
    def test_combine_sequences(self):
        '''combine_sequences() returns a single sequence of the elements of seq1 followed by the elements of seq2.'''
        seq1 = [1, 2, 3]
        seq2 = ['a', 'b', 'c']
        assert(combine_sequences(seq1, seq2) == [1, 2, 3, 'a', 'b', 'c'])

        seq3 = [4, 5, 6]
        assert(combine_sequences(seq2, seq3) == ['a', 'b', 'c', 4, 5, 6])

    def test_sequence_n_times(self):
        '''sequence_n_times() returns a single sequence of seq repeated n times.'''
        seq1 = [7, 14, 21]
        assert(sequence_n_times(seq1, 3) == [7, 14, 21, 7, 14, 21, 7, 14, 21])
        
        seq2 = [28, 35, 42]
        assert(sequence_n_times(seq2, 2) == [28, 35, 42, 28, 35, 42])

    def test_average(self):
        '''average() returns the average of the numbers in the input sequence.'''
        seq1 = [1, 2, 4, 8, 16, 32]
        assert(average(seq1) == 10.5)

        seq2 = [7, 14, 21, 28, 35]
        assert(average(seq2) == 21.0)

    def test_append_n_times(self):
        '''append_n_times() returns a list with an element appended n times.'''
        seq1 = ['f', 'l', 'a', 't', 'i', 'r', 'o', 'n']
        assert(append_n_times(seq1, 'a', 4) == ['f', 'l', 'a', 't', 'i', 'r', 'o', 'n', 'a', 'a', 'a', 'a'])

        seq2 = ['s', 'c', 'h', 'o', 'o', 'l']
        assert(append_n_times(seq2, 'b', 3) == ['s', 'c', 'h', 'o', 'o', 'l', 'b', 'b', 'b'])

    def test_food_names_list(self):
        '''food_names has a list of the food names'''
        assert(food_names == ["Flatburger", "French Fries", "Burrito"])

    def test_average_price(self):
        '''average_price has the average price of the foods'''
        assert(average_price == (9.50 + 1.25 + 7.25) / 3.0)

    def test_animal_descriptions(self):
        '''animal_descriptions has a list of strings describing each animal. For example: Fido is a Dog'''
        assert(animal_descriptions == ["Fido is a Dog", "Kitty is a Cat", "Fluffy is a Guinea Pig"])