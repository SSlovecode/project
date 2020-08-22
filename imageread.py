# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:29:46 2020

@author: hp
"""
import numpy as np
from skimage import io
from skimage import img_as_float #u can use it for convert values of image from 0 to 1
from matplotlib import pyplot as plt
img = io.imread('img\cell.jpg')
random_image=np.random.random([500,500])
plt.imshow(random_image)
print(random_image.min(),random_image.max())
print(img.min(),img.max())