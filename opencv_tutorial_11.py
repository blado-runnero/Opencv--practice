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

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel , iterations=3)

	dialation = cv2.dilate(mask, kernel,  iterations=3)

	



	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dialation',dialation)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;

cv2.destroyAllWindows()
cap.release()