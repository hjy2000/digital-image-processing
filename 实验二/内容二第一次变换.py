#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:32:54 2020
内容二第一次变换
@author: hou
"""

#灰度反转
# -*- coding: utf-8 -*
import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('a.jpg')
 
#图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]
 
#创建一幅图像
result = np.zeros((height, width), np.uint8)
 
#图像灰度变换
for i in range(height):
    for j in range(width):
        gray = grayImage[i,j]-46
        result[i,j] = np.uint8(gray)



#显示图像
 
cv2.imshow("Gray Image", grayImage)
cv2.imshow("Result", result)
 

cv2.imwrite("./info2.jpg", result, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
#等待显示
cv2.waitKey(0)



cv2.destroyAllWindows()