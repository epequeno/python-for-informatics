# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 17:30:44 2014

@author: Estevan Adrian Pequeno
"""

'''
Rewrite the grade program from the previous chapter using a function called
computegrade that takes a score as its parameter and returns a grade as a
string.


Score   Grade
> 0.9     A
> 0.8     B
> 0.7     C
> 0.6     D
<= 0.6    F

Program Execution:

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly to test the various different values for input. 
'''

import sys

score = 0

def computegrade(score):
    while True:
        try:
            score = raw_input("Enter score: ")
            score = float(score)
        except:
            print "Bad score, exiting"
            sys.exit(1)
        if score < 0.6 and score > 0:
            print "F"
        elif score >= 0.6 and score < 0.7:
            print "D"
        elif score >= 0.7 and score < 0.8:
            print "C"
        elif score >= 0.8 and score < 0.9:
            print "B"
        elif score >= 0.9 and score < 1:
            print "A"
        else:
            print "Bad score, continuing."
            
computegrade(score)
    