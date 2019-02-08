import numpy as np
import cv2

img = cv2.imread('pic.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(75,75),(150,150),(0,0,0),20)

cv2.rectangle(img,(75,75),(150,150),(0,0,0),5)

cv2.circle(img,(112,112),55,(0,0,0),5)

points = np.array([[10,20],[100,20],[34,12],[65,124],[134,80],[230,235]],np.int32)

cv2.polylines(img,[points],True, (0,255,255),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello There', (0,250),font,1,(200,250,250),2,cv2.LINE_AA)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()