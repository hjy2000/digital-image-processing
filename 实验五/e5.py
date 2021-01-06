# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:42:33 2021

@author: ASUS
"""

from imutils.perspective import four_point_transform
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

image = cv2.imread(r'D:/ASUS/image.png')


# 透视矫正
def perspective_transformation(img):
    # 读取图像，做灰度化、高斯模糊、膨胀、Canny边缘检测
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    dilate = cv2.dilate(blurred, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    # edged = cv2.Canny(dilate, 75, 200)
    edged = cv2.Canny(dilate, 30, 120,3)
 
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cnts = cnts[0]
    docCnt = None

    # 确保至少找到一个轮廓
    if len(cnts) > 0:
        # 按轮廓大小降序排列
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            # 近似轮廓
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # 如果我们的近似轮廓有四个点，则确定找到了纸
            if len(approx) == 4:
                docCnt = approx
                break

 
    # 对原始图像应用四点透视变换，以获得纸张的俯视图
    paper = four_point_transform(img, docCnt.reshape(4,2))
    return paper

im=perspective_transformation(image)
b,g,r = cv2.split(im)
img_rgb = cv2.merge([r,g,b])

plt.imshow(img_rgb)

plt.show()