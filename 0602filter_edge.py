import cv2
import numpy as np

img = cv2.imread('./img/sudoku.jpg')

gx_kernel = np.array([[-1, 1]])
gy_kernel = np.array([[-1], [1]])

edgex = cv2.filter2D(img, -1, gx_kernel)
edgey = cv2.filter2D(img, -1, gy_kernel)

cv2.imshow('origin', img)
cv2.imshow('edgex', edgex)
cv2.imshow('edgey', edgey)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 소벨 필터
gx_k = np.array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])
gy_k = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])

sobelx = cv2.filter2D(img, -1, gx_k)
sobely = cv2.filter2D(img, -1, gy_k)

cv2.imshow('origin', img)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 샤르 필터
gx_k = np.array([[-3, 0, 3],
                 [-10, 0, 10],
                 [-3, 0, 3]])
gy_k = np.array([[3, 10, 3],
                 [0, 0, 0],
                 [-3, -10, -3]])

scharx = cv2.filter2D(img, -1, gx_k)
schary = cv2.filter2D(img, -1, gy_k)

cv2.imshow('origin', img)
cv2.imshow('scharx', scharx)
cv2.imshow('schary', schary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Laplacian 필터
laple_k = np.array([[0, 1, 0],
                     [1, -4, 1],
                     [0, 1, 0]])

laple = cv2.filter2D(img, -1, laple_k)

cv2.imshow('origin', img)
cv2.imshow('laple', laple)
cv2.waitKey(0)
cv2.destroyAllWindows()
