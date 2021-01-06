#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:39:45 2020
灰度二值化
@author: hou
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('a.jpg')
 
#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x=grayImage
#获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]
 
#创建一幅图像
result = np.zeros((height, width), np.uint8)
 
#图像灰度反色变换 s=255-r
for i in range(height):
    for j in range(width):
        if grayImage[i,j]>128:
            result[i,j] = np.uint8(255)
        else:
            result[i,j] = np.uint8(0)
 
#显示图像
 
cv2.imshow("Gray Image", grayImage)
cv2.imshow("Result", result)
 

#cv2.imwrite("./a2.jpg", result, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
