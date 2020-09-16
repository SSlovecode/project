# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 22:20:19 2020

@author: hp
"""
import cv2

"""
here we have taken colour space BGR as default, 
because opencv reads images as BGR
"""
"""" enter location of image for conversion"""
image=cv2.imread("img/cell.jpg") 
print("enter choice for colour space")
print("1. BGR to RGB")
print("2. BGR to HSV")
print("3. BGR to YUV")
print("4. BGR to GRAY")
print("5. BGR to BINARY")
print("6. BGR to HLS")
print("7. BGR to LAB or CIEL*a*b*")
print("8. BGR to YCrCb")
print("9. BGR to RGBA")
c=int(input())
if c==1:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==2:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==3:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==4:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==5:
    img1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (thresh , img) = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==6:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==7:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==8:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif c==9:
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGBA)
    cv2.imshow('converted image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("invalid entry")    
cv2.imshow('real_image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()