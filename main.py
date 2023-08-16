import cv2
import poseModule as pm
import numpy as np

detector = pm.poseDetector()
count = 0
dir = 0

video = cv2.VideoCapture('C:/Users/RAHUL/Downloads/squat.mp4')

while True:
    success,img = video.read()
    img = cv2.resize(img,(1100,620))
    img = detector.findPose(img,draw=True)
    lmlist = detector.findPosition(img,draw=True)
    #print(lmlist)
    if len(lmlist)!=0:
       #right leg
       angle = detector.findAngle(img,24,26,28)
       print(angle)

       low = 35
       high = 170
       per = np.interp(angle,(low,high),(0,100))
       
       #print(angle,'=======>',per)
        
       if per == 0:
          if dir == 1:
             count+=0.5
             dir = 0
       if per == 100:
          if dir ==0:
             count+=0.5
             dir = 1

    print(count) 
    cv2.putText(img, str(int(count)), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)      


    cv2.imshow('video',img)

    if cv2.waitKey(1) & 0xFF == 27:
      break
video.release()
cv2.destroyAllWindows()


