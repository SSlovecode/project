# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:18:51 2020

@author: hp
"""

import numpy as np
from skimage import io
from skimage import img_as_float #u can use it for convert values of image from 0 to 1
from matplotlib import pyplot as plt
img = io.imread('img\cell.jpg')
plt.imshow(img)
