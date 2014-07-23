# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 19:25:36 2014

@author: Estevan Adrian Pequeno
"""

'''
Take the following Python code that stores a string:`
'''

string = 'X-DSPAM-Confidence:  0.8475'

'''
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
'''

space_index = string.find(" ")

number = float(string[space_index + 1:])

print number, type(number)
