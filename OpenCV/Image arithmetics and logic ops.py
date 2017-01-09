import cv2
import numpy as np

img1= cv2.imread('3D-Matplotlib.png')# Both images have to be of the same size
#img2= cv2.imread('mainsvmimage.png')
img3= cv2.imread('mainlogo.png')
#add= img1 + img2
#add= cv2.add(img1, img2) adds pixel values at each pixel
#weighted= cv2.addWeighted(img1, 0.6, img2, 0.4, 0) 0 is gamma value

rows, cols, channels= img3.shape
roi= img1[0:rows, 0:cols]

img2gray= cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', img2gray)
#                                 min  max thresh values
ret, mask= cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow('mask', mask)
mask_inv= cv2.bitwise_not(mask)
#cv2.imshow('mask_inv', mask_inv)
img1_bg= cv2.bitwise_and(roi, roi, mask=mask_inv)
#cv2.imshow('img1_bg', img1_bg)
img3_fg= cv2.bitwise_and(img3, img3, mask=mask)
#cv2.imshow('img3_fg', img3_fg)
dst= cv2.add(img1_bg, img3_fg)
#cv2.imshow('dst', dst)
img1[0:rows, 0:cols]= dst

cv2.imshow('res', img1)
#cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
