# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 16:11:41 2014

@author: Estevan Adrian Pequeno
"""

'''
Use urllib to replicate the previous exercise of (1) retrieving the document
from a URL, (2) displaying up to 3000 characters, and (3) counting the
overall number of characters in the document. Don't worry about the headers
for this exercise, simply show the first 3000 characters of the document
contents.
'''

'''
I'm going to use requests instead http://docs.python-requests.org/en/latest/
'''

import requests

content = requests.get('http://www.py4inf.com').content

print content[:3000]

print len(content)
