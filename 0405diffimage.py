# 2023 / 11 / 07 이미지 처리 / 이미지 연산 - 뺴기
import numpy as np
import cv2

img1 = cv2.imread('img/robot_arm1.jpg')
img2 = cv2.imread('img/robot_arm2.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
diff = img1_gray - img2_gray

otsu_threshold, t_diff = cv2.threshold(diff, -1, 255, cv2.THRESH_OTSU)

diff_color = cv2.cvtColor(t_diff, cv2.COLOR_GRAY2BGR)
diff_color[:, :, 0] = 0
spot = cv2.bitwise_xor(img1, diff_color)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('t_diff', t_diff)
cv2.imshow('diff_color', diff_color)
cv2.imshow('spot', spot)
cv2.waitKey()
cv2.destroyAllWindows()