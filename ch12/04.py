# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 16:12:27 2014

@author: Estevan Adrian Pequeno
"""

'''
Change the urllinks.py program to extract and count paragraph (p) tags from
the retrieved HTML document and display the count of the paragraphs as the
output of your program. Do not display the paragraph text - only count them.
Test your program on several small web pages as well as some larger web pages.
'''

import re
import requests

url = 'http://www.py4inf.com'
req = requests.get(url)
pattern = re.compile('<p>')
content_lines = [line for line in req.iter_lines()]

count = 0
for line in content_lines:
    if re.search(pattern, line):
        count += 1

print "There are %d <p> tags @ %s" % (count, url)
