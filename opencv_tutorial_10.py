import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lower = np.array([0,0,0])
	upper = np.array([193,191,202])

	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones((15,15), np.float32)/32
	smoothed = cv2.filter2D(res,-1,kernel)

	blur = cv2.GaussianBlur(res, (15,15), 0)
	median = cv2.medianBlur(res,15)
	bilateral = cv2.bilateralFilter(res, 15,75,75)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('smoothed',bilateral)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;


cv2.destroyAllWindows()
cap.release()