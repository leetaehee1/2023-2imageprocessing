import numpy as np

import cv2

img = cv2.imread('img/fish.jpg')

dx = 100; dy = 50
mtrx = np.float32([[1, 0, dx], [0, 1, dy]])
height, width, _ = img.shape
dst = cv2.warpAffine(img, mtrx, (width + dx, height + dy))

cv2.imshow('', img)
cv2.imshow('p', dst)
cv2.waitKey()
cv2.destroyAllWindows()

mtrx = np.float32([[2, 0, 0], [0, 3, 0]])
height, width, _ = img.shape
dst = cv2.warpAffine(img, mtrx, (width * 2, height * 3))

cv2.imshow('', img)
cv2.imshow('p', dst)
cv2.waitKey()
cv2.destroyAllWindows()

mtrx = np.float32([[2, 0, 0], [0, 3, 0]])
height, width, _ = img.shape
dst = cv2.resize(img, (int(width * 3) + 1, int(height * 3) + 1))

cv2.imshow('', img)
cv2.imshow('p', dst)
cv2.waitKey()
cv2.destroyAllWindows()

mtrx = np.float32([[2, 0, 0], [0, 3, 0]])
height, width, _ = img.shape
dst = cv2.resize(img, (500, 500))

cv2.imshow('', img)
cv2.imshow('p', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# ===========================
img = cv2.imread('img/fish.jpg')
dst = cv2.resize(img, (int(width * 0.7), int(height * 0.8)))
cv2.imshow('', img)
cv2.imshow('s', dst)
cv2.waitKey()
cv2.destroyAllWindows()