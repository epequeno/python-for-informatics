# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 17:43:05 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try
and except and print an error message and skip to the next number.


Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333
'''

def calculator():
    total = 0
    count = 0
    while True:
        num = raw_input("Enter a number: ")
        if num == 'done':
            print total, count, (total / count)
            break
        else:
            try:
                total += float(num)
            except:
                print "Invalid input"
                continue
        count += 1
        
calculator()
