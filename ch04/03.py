# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:27:58 2014

@author: Estevan Adrian Pequeno
"""

'''
Move the function call back to the bottom and move the definition of
print_lyrics after the definition of repeat_lyrics. What happens when you run
this program?
'''

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'

repeat_lyrics()

'''
The program runs as expcted. If one function is called within another the 
order which they are defined within the script is not important.
'''