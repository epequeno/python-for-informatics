# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 20:14:22 2014

@author: Estevan Adrian Pequeno
"""

'''
Sometimes when programmers get bored or want to have a bit of fun, they add
a harmless Easter Egg to their program
(en.wikipedia.org/wiki/Easter_egg_(media)). Modify the program that prompts
the user for the file name so that it prints a funny message when the user
types in the exact file name 'na na boo boo'. The program should behave
normally for all other files which exist and don't exist. Here is a sample
execution of the program:


python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

We are not encouraging you to put Easter Eggs in your programs - this is just
an exercise.
'''
import sys

user_data = raw_input("Enter the file name: ")

if user_data == "na na boo boo":
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    sys.exit(0)

try:
    user_file = open(user_data, 'r')
except:
    print "File cannot be opened: " + user_data
    sys.exit(1)


lines_list = [line.strip("\n") for line in user_file]


def count_subject_lines(data):
    subject_count = 0
    for line in lines_list:
        if line.startswith("Subject"):
            subject_count += 1
    print subject_count

count_subject_lines(lines_list)
