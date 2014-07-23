# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:54:06 2014

@author: Estevan Adrian Pequeno
"""

'''
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print words[2]

Figure out which line of the above program is still not properly guarded.
See if you can construct a text file which causes the program to fail and then
modify the program so that the line is properly guarded and test it to make
sure it handles your new text file. 

user_data = raw_input("Which file? ")
fhand = open(user_data, 'r')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print words[2]
    
We can cause an IndexError by passing this program a line which 
starts with "From" but containing nothing else. This passes the first test, the
length of the line is > 0. The second test checks if the line starts with
"From" and the program proceeds to try to print words[2] which does not exist.
We can guard against this case by adding an "or" test to check that the line
contains a 3rd item.
'''
user_data = raw_input("Which file? ")
fhand = open(user_data, 'r')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or len(words) < 3: continue
    if words[0] != 'From' : continue
    print words[2]
    
