import numpy as np
import cv2

img = cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

px = img[55,55]

img[55,55] = [255,255,255]

px = img[55,55]

print(px)

img[100:150,100:130] = [255,240,140]

copy_region = img[250:350,50:150]

img[0:100, 0:100] = copy_region

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()