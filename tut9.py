import numpy as np
import cv2
img = cv2.imread('cipher.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 25) 
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 500, 80, 90, 100,50)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:1]:
        cv2.circle(img, (i[0], i[1]), i[1], (255,255,255), 4)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()