# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:23:51 2014

@author: Estevan Adrian Pequeno
"""

'''
This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e. the whole
e-mail address). At the end of the program print out the contents of your
dictionary.


python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

file_name = raw_input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    who_from_dict[domain] = who_from_dict.get(domain, 0) + 1

print who_from_dict
