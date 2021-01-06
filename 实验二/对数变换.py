#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:11:50 2020
指数变换
@author: hou
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

#伽玛变换
def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut) #像素灰度值的映射
    output_img = np.uint8(output_img)
    return output_img
 
#读取原始图像
img = cv2.imread('t3.jpg')
 
#图像灰度伽玛变换
output1 = gamma(img, 20,0.6)
output2 = gamma(img, 20,0.4)

#显示图像
cv2.imshow('Imput', img)
cv2.imshow('Output1', output1)
cv2.imshow('Output2', output2)
cv2.imwrite("./tz1.jpg", output1, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
cv2.imwrite("./tz2.jpg", output2, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 

cv2.waitKey(0)
cv2.destroyAllWindows()