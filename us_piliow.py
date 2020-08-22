# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:34:57 2020

@author: hp
"""
import numpy as np
from PIL import Image
img=Image.open("img/cell.jpg")
print(type(img))
print(img.format)
#img.show(img)
img1=np.asarray(img)
print(type(img1))