# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:56:48 2014

@author: Estevan Adrian Pequeno
"""

'''
Add code to the above program to figure out who has the most messages in the
file.

After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section ??) to find who has
the most messages and print how many messages the person has.


Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

file_name = raw_input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    words = line.split()
    who_from_dict[words[1]] = who_from_dict.get(words[1], 0) + 1

most = 0
winner = None
for person in who_from_dict:
    if who_from_dict[person] > most:
        most = who_from_dict[person]
        winner = person

print winner, who_from_dict[winner]
