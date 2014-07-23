# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:34:08 2014

@author: Estevan Adrian Pequeno
"""

'''
Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line. Count the number of messages from
each person using a dictionary.

After all the data has been read print the person with the most commits by
creating a list of (count, email) tuples from the dictionary and then sorting
the list in reverse order and print out the person who has the most commits.


Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

file_name = raw_input("Enter a file name: ")
line_list = [line.strip("\n") for line in open(file_name, 'r')
             if line.startswith("From ")]
email_dict = {}

for line in line_list:
    email = line.split()[1]
    email_dict[email] = email_dict.get(email, 0) + 1

tulple_list = []
for email in email_dict:
    tulple_list.append((email_dict[email], email))

winner = sorted(tulple_list, reverse=True)[0]
print winner[1], winner[0]
