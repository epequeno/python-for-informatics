# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:57:50 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program that reads the words in words.txt and stores them as keys in
a dictionary. It doesn't matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.
'''

'''
The book didn't specify where to get 'words.txt' but I'm going to assume
the file @ http://www.py4inf.com/code/words.txt is what is reffered to.
'''

lines = [word.strip('\n') for word in open('words.txt', 'r')]
word_dict = {}
for line in lines:
    words = line.split()
    for word in words:
        word_dict[word] = None


print "would" in word_dict
print "fast" in word_dict
print "python" in word_dict
