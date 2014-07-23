# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 19:04:17 2014

@author: Estevan Adrian Pequeno
"""

'''
Write another program that prompts for a list of numbers as above and at the
end prints out both the maximum and minimum of the numbers instead of the
average.
'''

MAX = 0
MIN = 0


def calculator():
    global MAX
    global MIN
    while True:
        number = raw_input("Enter a number: ")
        if number == "done":
            print MAX, MIN
            break
        try:
            number = float(number)
        except:
            print "Invalid input"
            continue
        if number > MAX:
            MAX = number
        if number < MIN:
            MIN = number

calculator()
