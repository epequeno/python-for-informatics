# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:31:07 2014

@author: Estevan Adrian Pequeno
"""

'''
Rewrite your pay computation with time-and-a-half for overtime and create a
function called computepay which takes two parameters (hours and rate).


Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
import sys

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
OVERTIME_RATE = 1.5

try:
    hours = float(hours)
    rate = float(rate)
except:
    print "Please enter valid input"
    sys.exit(1)


def computepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40  # hours over 40
        hours -= overtime_hours  # regular rate hours
        overtime_pay = overtime_hours * rate * OVERTIME_RATE
        return (hours * rate) + overtime_pay
    else:
        return (hours * rate)


print "Pay: %.2f" % computepay(hours, rate)
