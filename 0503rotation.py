import cv2
import numpy as np

img = cv2.imread('img/children.jpg')

height, width = img.shape[0:2]

d10 = 10 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), 0], [np.sin(d10), np.cos(d10), 0]])
r10 = cv2.warpAffine(img, m10, (width, height))
cv2.imshow('', img)
cv2.imshow('r10', r10)
cv2.waitKey(0)
cv2.destroyAllWindows()



d10 = 180 * np.pi / 180
m10 = np.float32([[np.cos(d10), -1 * np.sin(d10), width], [np.sin(d10), np.cos(d10), height]])
r10 = cv2.warpAffine(img, m10, (width, height))
cv2.imshow('', img)
cv2.imshow('r10', r10)
cv2.waitKey(0)
cv2.destroyAllWindows()