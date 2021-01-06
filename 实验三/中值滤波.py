#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:10:49 2020

@author: hou
"""

import scipy.signal as signal
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import skimage
import cv2
img0=cv2.imread('danghui_yuantu.bmp',cv2.IMREAD_GRAYSCALE)
img=cv2.imread('danghui_jiaoyan.bmp',cv2.IMREAD_GRAYSCALE)

img1 = signal.medfilt(img,(3,3)) #二维中值滤波
img2 = signal.medfilt(img,(5,5)) #二维中值滤波
img3 = signal.medfilt(img,(7,7)) #二维中值滤波
plt.figure(figsize=(10,10))
plt.subplot(235);plt.imshow(img3,'gray');plt.title('7*7')
plt.subplot(233);plt.imshow(img1,'gray');plt.title('3*3')
plt.subplot(234);plt.imshow(img2,'gray');plt.title('5*5')
plt.subplot(231);plt.imshow(img0,'gray');plt.title('yuantu')
plt.subplot(232);plt.imshow(img,'gray');plt.title('noise')