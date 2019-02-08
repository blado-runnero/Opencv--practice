import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap_ret = cv2.VideoCapture(2)

saved = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', saved, 20.0, (640,480))

while True:
	ret1, frame1 = cap_ret.read()
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame1)
	cv2.imshow('normal_one',frame)
	cv2.imshow('gray_one',gray)
	cv2.imshow('3d_one',frame1)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
    
cap.release()
out.release()
cv2.destroyAllWindows()
