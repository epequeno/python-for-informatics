# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:11:13 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program to look for lines of the form

New Revision: 39772

And extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.


Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
'''

import re

file_name = raw_input("Enter file: ")
data_lines = [line.strip('\n') for line in open(file_name, 'r')]

pattern = re.compile('New Revision: \d+')

total = 0
count = 0

for line in data_lines:
    result = re.search(pattern, line)
    if result:
        count += 1
        total += float(result.group(0)[14:])

print total / count
