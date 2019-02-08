import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
txtfiles = [] 
for file in glob.glob("*.jpg"):
    txtfiles.append(file)
    
for ix in txtfiles:
    img = cv2.imread(ix,cv2.IMREAD_COLOR)
    imgtest1 = img.copy()
    imgtest = cv2.cvtColor(imgtest1, cv2.COLOR_BGR2GRAY)
    facecascade = cv2.CascadeClassifier('C:\\Users\\bladeRUNNER\\Desktop\\scripts\\haarcascade_frontalface_default.xml')
    faces = facecascade.detectMultiScale(imgtest, scaleFactor=1.2, minNeighbors=5)
 
    print('Total number of Faces found',len(faces))
    
    for (x, y, w, h) in faces:
        face_detect = cv2.rectangle(imgtest, (x, y), (x+w, y+h), (255, 0, 255), 2)
        roi_gray = imgtest[y:y+h, x:x+w]
        roi_color = imgtest[y:y+h, x:x+w]        
        plt.imshow(face_detect)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()