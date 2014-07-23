# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 11:17:06 2014

@author: Estevan Adrian Pequeno
"""

'''
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies.
'''


file_name = raw_input("Which book? ")
book = open(file_name, 'r')


def prepare_text(raw_book):
    ''' Take file handler as input. Chop off the project Gutenberg header
    and footer. Remove non-alpha characters. Convert all letters to
    lowercase and finally return the entire book as a singe string '''
    start_marker = "*** START OF THIS"
    end_marker = "*** END OF THIS"
    process_text = False
    book_lines = []
    all_letters = ''

    for line in raw_book:
        # see the start marker, switch flag to begin processing
        if line.startswith(start_marker) and process_text is False:
            process_text = True

        # see the end marker, switch flag to end processing
        if line.startswith(end_marker) and process_text is True:
            process_text = False

        if process_text is True:
            line = ''.join([char for char in line if char.isalpha()])
            line = line.lower()
            book_lines.append(line)

    all_letters = all_letters.join(book_lines)
    return all_letters

condensed_book = prepare_text(book)

letter_histogram = {}

for letter in condensed_book:
    letter_histogram[letter] = letter_histogram.get(letter, 0) + 1

results_list = []

for key in letter_histogram:
    results_list.append((letter_histogram[key], key))

print "Letter frequency results for:", file_name
for pair in sorted(results_list, reverse=True):
    print pair[1], pair[0]
