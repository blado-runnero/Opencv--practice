import numpy as np
import cv2

cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubstractorMOG2()

while True:
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)

	cv2.imshow('original',frame)
	cv2.imshoe('foreground', fgmask)

	k == cv2.waitKey(30) & 0xFF
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()