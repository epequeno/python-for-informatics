# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:58:58 2014

@author: Estevan Adrian Pequeno
"""

'''
This program counts the distribution of the hour of the day for each of the
messages. You can pull the hour from the "From" line by finding the time
string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts,
one per line, sorted by hour as shown below.


Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

file_name = raw_input("Enter a file name: ")
line_list = [line.strip("\n") for line in open(file_name, 'r')
             if line.startswith("From ")]
hour_histogram = {}
tuple_list = []

for line in line_list:
    time = line.split()[5]
    hour = time.split(":")[0]
    hour_histogram[hour] = hour_histogram.get(hour, 0) + 1

for key in hour_histogram:
    tuple_list.append((key, hour_histogram[key]))

sorted_tuple_list = sorted(tuple_list)

for item in sorted_tuple_list:
    print item[0], item[1]
