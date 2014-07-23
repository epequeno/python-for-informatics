# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:25:11 2014

@author: Estevan Adrian Pequeno
"""

'''
Rewrite the program that prompts the user for a list of numbers and prints
out the maximum and minimum of the numbers at the end when the user enters
"done". Write the program to store the numbers the user enters in a list and
use the max() and min() functions to compute the maximum and minimum numbers
after the loop completes.


Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
'''


def find_min_max():
    user_responses = []
    while True:
        try:
            user_input = raw_input("Enter a number: ")
            user_input = int(user_input)
        except:
            break
        user_responses.append(user_input)
    print "Maximum: ", max(user_responses)
    print "Minimum: ", min(user_responses)

find_min_max()
