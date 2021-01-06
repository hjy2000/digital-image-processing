#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:03:33 2020

@author: hou
"""

import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import skimage
import cv2
img0=cv2.imread('xust_yuantu.bmp')
img=cv2.imread('xust_gaosi.bmp')


img1 = cv2.blur(img,(3,3))
img2 = cv2.blur(img,(5,5))
img3 = cv2.blur(img,(7,7))
plt.figure(figsize=(10,10))
plt.subplot(235);plt.imshow(img3,'gray');plt.title('7*7')
plt.subplot(233);plt.imshow(img1,'gray');plt.title('3*3')
plt.subplot(234);plt.imshow(img2,'gray');plt.title('5*5')
plt.subplot(231);plt.imshow(img0,'gray');plt.title('yuantu')
plt.subplot(232);plt.imshow(img,'gray');plt.title('moise')