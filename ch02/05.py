# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:59:31 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program which prompts the user for a Celsius temperature, convert the
temperature to Fahrenheit and print out the converted temperature. 
'''

'''
From: http://en.wikipedia.org/wiki/Celsius#Conversion_table_between_the_different_temperature_units
'''

celsius = float(raw_input("Temp in Celsius: "))
fahr = celsius * (9.0/5.0) + 32

print "Temp in Fahrenheit: %.2f" % fahr
