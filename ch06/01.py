# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 19:11:47 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a while loop that starts at the last character in the string and works
its way backwards to the first character in the string, printing each letter
on a separate line, except backwards.
'''

word = "python"


def backwards(word):
    index = len(word) - 1  # adjust for 0th index
    while index >= 0:
        print word[index]
        index -= 1

backwards(word)
