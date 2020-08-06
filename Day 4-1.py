# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:17:28 2020

不存在@author: USER
"""

import os.path
if os.path.isfile('4-1.txt'):
    print('4-1.txt存在')
else:
    print('4-1.txt不存在')
    


x=open('4-1.txt','w')
x.write('you ')

x=open('4-1.txt','r')
print(x.read())

x=open('4-1.txt','a')
x.write('and me')

x.close()

