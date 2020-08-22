# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:08:02 2020

@author: hp
"""

from skimage import io
img= io.imread("img/cell.jpg")
print(type(img))
print(img.shape)
io.imshow(img)