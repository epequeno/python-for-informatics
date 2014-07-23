# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:00:35 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program to prompt for a score between 0.0 and 1.0. If the score is
out of range print an error. If the score is between 0.0 and 1.0, print a
grade using the following table:


Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F

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

Run the program repeatedly as shown above to test the various different values
for input. 
'''

while True:
    score = raw_input("Enter score: ")
    try:
        score = float(score)
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
    except:
        print "Bad score, exiting."
        break