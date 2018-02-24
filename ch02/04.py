# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:51:17 2014

@author: Estevan Adrian Pequeno
"""

'''
Assume that we execute the following assignment statements:


width = 17
height = 12.0

For each of the following expressions, write the value of the expression and
the type (of the value of the expression).

1. width/2

2. width/2.0

3. height/3

4. 1 + 2 * 5 #Does the text of the PDF have a typo?  Reads 1 + 2 \* 5.  Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Location 574). Kindle Edition. 

Use the Python interpreter to check your answers. 
'''

'''
1. Since width is an int dividing it by 2 will give floor division which would
   be between 16/2 = 8 and 18/2 = 9 so ~8
   
   In [11]: width/2
   Out[11]: 8
   
2. Since we are now dividing by 2.0 a float, we will get a float as a result.
   ~8.5
   
   In [12]: width/2.0
   Out[12]: 8.5
   
3. height is already a float so dividing by 3 (int) will still produce a float
   as an answer 4.0
   
   In [13]: height/3
   Out[13]: 4.0

4. Following PEMDAS multiplication takes precedent so 2*5 is computed first
   giving 10 then added to 1 producing 11
   
   In [14]: 1 + 2 * 5
   Out[14]: 11
'''
