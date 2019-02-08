import numpy as np
import cv2

img = cv2.imread('bookpage.jpg')

# Simple Threshold
retval,threshold = cv2.threshold(img, 100,255,cv2.THRESH_BINARY)

# Converted to Grayscale and then Thresholded
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled, 100,255,cv2.THRESH_BINARY)

# Gaussian Adaptive Threshold
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# OTSU
retval3,otsu = cv2.threshold(grayscaled, 50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('image',otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()