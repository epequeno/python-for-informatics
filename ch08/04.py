# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 21:29:58 2014

@author: Estevan Adrian Pequeno
"""

'''
Download a copy of the file from www.py4inf.com/code/romeo.txt

Write a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is
not in the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical
order.


Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 
'and', 'breaks', 'east', 'envious', 'fair', 'grief', 
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 
'sun', 'the', 'through', 'what', 'window', 
'with', 'yonder']
'''

file_name = raw_input("Enter file: ")

lines = [line.strip('\n') for line in open(file_name, 'r')]

word_list = []

for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_list:
            pass
        else:
            word_list.append(word)

print sorted(word_list)