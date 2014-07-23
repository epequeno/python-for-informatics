# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:26:19 2014

@author: Estevan Adrian Pequeno
"""

'''
Move the last line of this program to the top, so the function call appears
before the definitions. Run the program and see what error message you get. 
'''

repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# NameError: name 'repeat_lyrics' is not defined