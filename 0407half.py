import cv2
import numpy as np

img_face = cv2.imread('./img/man_face.jpg')
img_skull = cv2.imread('./img/skull.jpg')

alpha_width_rate = 20

height, width, _ = img_face.shape
middle = width // 2

alpha_width = width * alpha_width_rate // 100
start = middle - alpha_width // 2
step = 100 / alpha_width

img = np.zeros_like(img_face)
img[:middle, :, :] = img_face[:middle, :, :].copy()
img[middle:, :, :] = img_skull[middle:, :, :].copy()

for i in range(alpha_width + 1):
    alpha = (100 - step * i) / 100
    beta = 1 - alpha
    img[start + i, :] = img_face[start + i, :] * alpha + img_skull[start + i, :] * beta

    print(i, alpha, beta)

cv2.imshow('img', img)



cv2.waitKey()
cv2.destroyAllWindows()