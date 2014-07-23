# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 19:21:07 2014

@author: Estevan Adrian Pequeno
"""

'''

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count

Encapsulate this code in a function named count, and generalize it so that it
accepts the string and the letter as arguments.
'''

word = 'banana'


def count(word, target):
    count = 0
    for letter in word:
        if letter == target:
            count += 1
    print count

count(word, 'a')
