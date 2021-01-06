# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:25:07 2020
数字图像处理实验四
@author: ASUS
"""

import cv2
#import pandas as pd
from skimage import util
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import scipy.ndimage as nd
img=np.array(Image.open('dayanta_mohu.bmp').convert('L'),dtype='uint8')

#b, g, r = img.split()
#img = np.array(Image.merge("RGB", (r, g, b)))

noise_gs_img = np.array(util.random_noise(img,mode='gaussian')*255,dtype='uint8')
noise_salt_img = np.array(util.random_noise(img,mode='salt')*255,dtype='uint8')

#img=noise_salt_img

def roberts(im):
    kernelx = np.array([[-1, 0], [0, 1]],dtype=int)
    kernely = np.array([[0, -1], [1, 0]],dtype=int)
    x = cv2.filter2D(im, cv2.CV_16S, kernelx)
    y = cv2.filter2D(im, cv2.CV_16S, kernely)
    # 转转成uint8
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    Roberts=Roberts*5
    #images = [img, Roberts]
    imglist=[]
    imglist.append(Roberts)
    imglist.append(absX)
    imglist.append(absY)
    return imglist

def Prewitt(im):
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    x = cv2.filter2D(im, cv2.CV_16S, kernelx)
    y = cv2.filter2D(im, cv2.CV_16S, kernely)
    # 转转成uint8
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    im1 = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    imglist=[]
    imglist.append(im1)
    imglist.append(absX)
    imglist.append(absY)
    
    return imglist

def sobel(im):
    
    x = cv2.Sobel(im, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(im, cv2.CV_16S, 0, 1)
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    im1 = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    
    imglist=[]
    imglist.append(im1)
    imglist.append(absX)
    imglist.append(absY)
    
    return imglist
    
def lpls(im):
    im1=cv2.Laplacian(im,cv2.CV_64F, ksize=5)
    im2=cv2.Laplacian(im,cv2.CV_64F, ksize=9)
    im3=nd.filters.gaussian_laplace(im,sigma=2)
    im3=im3+im
    imglist=[im1,im2,im3]
    return imglist

def cv2fspz(im):
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(20, 20))
    eroded = cv2.erode(im,kernel)        #腐蚀图像
    dilated = cv2.dilate(im,kernel)#膨胀图像
    imglist=[eroded,dilated]
    return imglist
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10,10))

'''
plt.subplot(341)
plt.imshow(img,'gray')
plt.title('gs_pic')

plt.subplot(342)
plt.imshow(roberts(img)[0],'gray')
plt.title('roberts')
plt.subplot(346)
plt.imshow(roberts(img)[1],'gray')
plt.title('roberts_x')
plt.subplot(3,4,10)
plt.imshow(roberts(img)[2],'gray')
plt.title('roberts_y')

plt.subplot(343)
plt.imshow(Prewitt(img)[0],'gray')
plt.title('Prewitt')
plt.subplot(347)
plt.imshow(Prewitt(img)[1],'gray')
plt.title('Prewitt_x')
plt.subplot(3,4,11)
plt.imshow(Prewitt(img)[2],'gray')
plt.title('Prewitt_y')

plt.subplot(344)
plt.imshow(sobel(img)[0],'gray')
plt.title('sobel')
plt.subplot(348)
plt.imshow(sobel(img)[1],'gray')
plt.title('sobel_x')
plt.subplot(3,4,12)
plt.imshow(sobel(img)[2],'gray')
plt.title('sobel_y')
'''
'''
plt.subplot(221)
plt.imshow(img,'gray')
plt.title('origin_pic')
plt.subplot(222)
plt.imshow(lpls(img)[0],'gray')
plt.title('H1_pic')
plt.subplot(223)
plt.imshow(lpls(img)[1],'gray')
plt.title('H2_pic')
plt.subplot(224)
plt.imshow(lpls(img)[2],'gray')
plt.title('LOG_pic')
'''
plt.subplot(131)
plt.imshow(img,'gray')
plt.title('origin_pic')

plt.subplot(132)
plt.imshow(cv2fspz(img)[0],'gray')
plt.title('eroded_pic')

plt.subplot(133)
plt.imshow(cv2fspz(img)[1],'gray')
plt.title('dilated_pic')

plt.show()
