#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:32:45 2020
直方图均衡化
@author: hou
"""

from PIL import Image
from pylab import *
from numpy import *
import cv2
import numpy as np
import matplotlib.pyplot as plt

def histeq(im,nbr_bins = 256):
    """对一幅灰度图像进行直方图均衡化"""
    #计算图像的直方图
    #在numpy中，也提供了一个计算直方图的函数histogram(),第一个返回的是直方图的统计量，第二个为每个bins的中间值
    imhist,bins = histogram(im.flatten(),nbr_bins,normed= True)
    cdf = imhist.cumsum()   #
    cdf = 255.0 * cdf / cdf[-1]
    #使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf


im = cv2.imread('a.jpg')
im2,cdf = histeq(im)

im2 = Image.fromarray(uint8(im2))
im2.show()
# print(cdf)
# plot(cdf)
im2.save("junheng.jpg")