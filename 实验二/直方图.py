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

img=np.array(mpimg.imread('~/000.jpg'))

plt.figure("lena")
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256,facecolor='green', alpha=0.75)  
plt.show()
