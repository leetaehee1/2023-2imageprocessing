import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

img = cv2.imread('./img/children.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)
print(f'{faces=}')

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi = gray[y : y + h, x : x + w]

    # 얼굴부분 블러 처리
    # roib = img[y : y + h, x : x + w]
    # roib = cv2.blur(roib, (30, 30))
    # img[y: y + h, x: x + w] = roib

    eyes = eye_cascade.detectMultiScale(roi)
    print(f'{eyes=}')
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img[y : y + h, x : x + w], (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()