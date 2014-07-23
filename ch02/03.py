# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:47:22 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program to prompt the user for hours and rate per hour to compute
gross pay.


Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

We won't worry about making sure our pay has exactly two digits after the
decimal place for now. If you want, you can play with the built-in Python
round function to properly round the resulting pay to two decimal places.
'''

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
gross_pay = int(hours) * float(rate)
print gross_pay