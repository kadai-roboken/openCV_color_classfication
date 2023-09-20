import cv2
import numpy as np

capture = cv2.VideoCapture(2)

while(True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp = 1.2, minDist = 100, param1 = 120, param2 = 60, minRadius = 0, maxRadius = 0)
    print(type(circles))
    print(np.around(circles))
    print(np.uint16(np.around(circles)))
    circles = np.uint16(np.around(circles))
    if len(circles):
        for circle in circles[0,:]:
            cv2.circle(frame,(circle[0],circle[1]),circle[2],(0,165,255),5)
            cv2.circle(frame,(circle[0],circle[1]),2,(0,255,255),3)
        cv2.imshow("video",frame)
        k = cv2.waitKey(46) & 0xFF
        if k == ord('q'):
            break
    else:
        print('見つかりませんでした')
        cv2.imshow('video',frame)
        k == cv2.waitKey(46) & 0xFF
        if k == ord('q'):
            break
capture.release()
cv2.destroyAllWindows