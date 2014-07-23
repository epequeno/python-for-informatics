# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:51:54 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program to read through a mail log, and build a histogram using a
dictionary to count how many messages have come from each email address and
print the dictionary.


Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''

file_name = 'mbox-short.txt'
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    words = line.split()
    who_from_dict[words[1]] = who_from_dict.get(words[1], 0) + 1

print who_from_dict
