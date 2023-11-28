import cv2
img_file = "img/images.png"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow("IMGWindow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

video_file = "img/big_buck.avi"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(1)
        else:
            break
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                cv2.imwrite("img/myphoto1017.jpg", img)
                break
cap.release()
cv2.destroyAllWindows()