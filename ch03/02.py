# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 14:24:32 2014

@author: Estevan Adrian Pequeno
"""

'''
Rewrite your pay program using try and except so that your program handles
non-numeric input gracefully by printing a message and exiting the program.
The following shows two executions of the program:


Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''

import sys

OVERTIME_RATE = 1.5

try:
    hours = float(raw_input("Enter Hours: "))
    rate = float(raw_input("Enter Rate: "))
except:
    print "Error, please enter numeric input"
    sys.exit(1)


def pay(hours, rate):
    ''' Determine pay given hours and rate and 1.5 times the hourly
    rate for hours worked above 40.'''
    overtime_pay = 0
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * OVERTIME_RATE
        final_pay = ((hours - overtime_hours) * rate) + overtime_pay
    else:
        final_pay = (hours * rate)
    return "Pay: " + str(final_pay)

print pay(hours, rate)