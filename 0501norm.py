import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('', img)
cv2.imshow('n', img_norm)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_n = cv2.calcHist([img_norm], [0], None, [256], [0, 255])

# 히스토그램 그래프 그리기
plt.figure(figsize=(12, 6))

# 원본 이미지 히스토그램
plt.subplot(1, 2, 1)
plt.plot(hist)
plt.title('Histogram of Original Image')

# 정규화된 이미지 히스토그램
plt.subplot(1, 2, 2)
plt.plot(hist_n)
plt.title('Histogram of Normalized Image')

plt.show()


cv2.waitKey()
cv2.destroyAllWindows()