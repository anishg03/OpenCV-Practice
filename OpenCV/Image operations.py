import numpy as np
import cv2

img= cv2.imread('Puppy.jpg', cv2.IMREAD_COLOR)

px= img[55, 55]# Particular pixel
#print(px)
img[55, 55] = [255,255,255]
roi= img[100:150, 150:190]# Region of image
img[100:150, 150:190]= [255,255,255]
dog_face= img[50:350, 100:350]
img[0:300, 0:250]= dog_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
