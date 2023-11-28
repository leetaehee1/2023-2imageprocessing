import cv2
import numpy as np

img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img)   # 원본과 동일한 크기의 0으로 채워진 이미지
thresh_np[ img > 127] = 255      # 127 보다 큰 값만 255로 변경

# ---② OpenCV API로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("gray", img)
cv2.imshow("thresh", thresh_np)
cv2.imshow("thresh cv", thresh_cv)

cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('./img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("paper", img)
_, t_80 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
otsu_threshold, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_OTSU)
cv2.imshow("t_80", t_80)
cv2.imshow("t_otsu", t_otsu)
cv2.waitKey()
cv2.destroyAllWindows()

blk_size = 9
C = 5

img = cv2.imread('./img/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("paper", img)
otsu_threshold, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, blk_size, C)
cv2.imshow("t_otsu", t_otsu)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.waitKey()
cv2.destroyAllWindows()