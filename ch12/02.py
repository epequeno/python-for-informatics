# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:58:54 2014

@author: Estevan Adrian Pequeno
"""

'''
Change your socket program so that it counts the number of characters it has
received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number
of characters and display the count of the number of characters at the end
of the document.
'''

import socket
import os

# user_url = raw_input("Enter url: ")
user_url = 'http://www.py4inf.com/code/romeo.txt'
try:
    host_name = user_url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    mysock.send('GET ' + user_url + ' HTTP/1.0\n\n')
except:
    print "Please enter a valid URL"
    os.sys.exit(1)

count = 0
while True:
    data = mysock.recv(512)
    count += len(data)
    if (len(data) < 1) or count >= 3000:
        break
    print data

mysock.close()
print count
