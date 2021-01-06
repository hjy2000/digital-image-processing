#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:00:37 2020
画直方图
@author: hou
"""
import matplotlib.image as mpimg # mpimg 用于读取图片
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

img=Image.open('result.jpg')
r,g,b=img.split()

plt.figure("lena")

ar=np.array(r).flatten()
plt.hist(ar, bins=256,facecolor='r',edgecolor='r')
ag=np.array(g).flatten()
plt.hist(ag, bins=256, facecolor='g',edgecolor='g')
ab=np.array(b).flatten()
plt.hist(ab, bins=256, facecolor='b',edgecolor='b')
plt.show()