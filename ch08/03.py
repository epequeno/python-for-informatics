# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 21:12:05 2014

@author: Estevan Adrian Pequeno
"""

'''
Rewrite the guardian code in the above example without two if statements. 
Instead use a compound logical expression using the and logical operator with
a single if statement. 
'''

user_data = raw_input("Which file? ")
fhand = open(user_data, 'r')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if (len(words) == 0 or len(words) < 3) or words[0] != 'From' : continue
    print words[2]
    
    
'''
combining with the solution from the previous question I was able to obtain
the same behavior but using an "or" operator. I'll have to revisit this one
'''