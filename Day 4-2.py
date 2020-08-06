# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:58:23 2020

@author: USER
"""
file = open('000.png','rb')
img = file.read()
file.close()

file = open('001.jpg','wb')
file.write(img)
file.close()