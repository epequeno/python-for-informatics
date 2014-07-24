# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:39:07 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a simple program to simulate the operation of the the grep command on
Unix. Ask the user to enter a regular expression and count the number of
lines that matched the regular expression:


$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
'''

import re

user_input = raw_input("Enter a regular expression: ")
file_name = 'mbox.txt'
data_list = [line.strip('\n') for line in open(file_name, 'r')]

pattern = re.compile(user_input)

count = 0
for line in data_list:
    result = re.search(pattern, line)
    if result:
        count += 1

print "%s had %d lines that matched %s" % (file_name, count, user_input)
