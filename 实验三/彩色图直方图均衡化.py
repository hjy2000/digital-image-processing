import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用于读取图片
import copy
def hisEqulColor(img1):
    #img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    channels = cv2.split(img1)
    #print(len(channels))
    cv2.equalizeHist(channels[0],channels[0])
    cv2.equalizeHist(channels[1],channels[1])
    cv2.equalizeHist(channels[2],channels[2])
    cv2.merge(channels, img1)
    #cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    return img1

im = mpimg.imread('000.jpg')
#cv2.imshow('im1', im)
#cv2.waitKey(0)
im1=copy.deepcopy(im)
eq = hisEqulColor(im1)
#cv2.imwrite('12345.jpg',eq)
#cv2.imshow('image2',eq)
cv2.imwrite("./result.jpg", eq, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
#cv2.waitKey(0)
plt.figure(figsize=(20,20))
plt.subplot(121);plt.imshow(im);plt.title('origin')
plt.subplot(122);plt.imshow(eq);plt.title('result')
