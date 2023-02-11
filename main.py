import cv2
import numpy as np
k, cap = 'a', cv2.VideoCapture(r"C:\Users\Lenovo\Downloads\Red Dot.mp4")
while True and k != 'q' and cap.isOpened():
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_red1, u_red1 = np.array([0, 70, 50]), np.array([10, 255, 255])
    l_red2, u_red2 = np.array([170, 70, 50]), np.array([180, 255, 255])
    thr1, thr2 = cv2.inRange(hsv, l_red1, u_red1), cv2.inRange(hsv, l_red2, u_red2)
    thr = thr1 | thr2
    thresh = thr.copy()
    cont = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    maxi, fin_cnt = 0, 0
    for cnt in cont:
        area = cv2.contourArea(cnt)
        if area > maxi:
            maxi = area
            fin_cnt = cnt
    momen = cv2.moments(fin_cnt)
    x, y = int(momen['m10'] / momen['m00']), int(momen['m01'] / momen['m00'])
    #print(x, y)
    cv2.rectangle(frame, (x - 125, y - 125), (x + 125, y + 125), (0, 255, 0), 3)
    cv2.circle(frame, (x, y), 1, (0, 255, 0), 5)
    frame = cv2.resize(frame, (1280, 720))
    cv2.imshow('frame', frame)
    k = chr(cv2.waitKey(10) & 255)
cv2.destroyAllWindows()
