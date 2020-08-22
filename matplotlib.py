# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:57:39 2020

@author: hp
"""

import matplotlib.image as mi
import matplotlib.pyplot as plt
img=mi.imread("img/cell.jpg")
print(type(img))
print(img.shape)
plt.imshow(img)
plt.colorbar()