# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:25:23 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a function called chop that takes a list and modifies it, removing the
first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
'''

list_one = [x for x in range(1,10)]
list_two = [x for x in range(2, 20, 2)]

def chop(my_list):
    last_item_index = len(my_list) - 1  # adjust for 0th index
    del my_list[last_item_index]
    del my_list[0]
    return None
    
print list_one, id(list_one)
print "chop() returns:", chop(list_one)
print "chop chop..."
print list_one, id(list_one), "\n"

def middle(my_list):
    return my_list[1:(len(my_list) - 1)]
    
print list_two, id(list_two)
new_list = middle(list_two)
print "middle() returns: ", new_list
print new_list, id(new_list)