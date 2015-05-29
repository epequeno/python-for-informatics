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

def calc():
    numbers = []
    count = 0
    while True:
        get_num = raw_input("Enter a number: ")
        if get_num == 'done':
            print min(numbers), max(numbers)
            break
        else:
            try:
                numbers.append(float(get_num))
            except:
                print "Invalid input"
                continue
        
calc()