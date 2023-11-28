import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/mountain.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist)
plt.show()
print("hist.shape", hist.shape)
print("hist.sum", hist.sum())
print("img shape", img.shape)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('img/mountain.jpg')
bgr = cv2.split(img)
colors = ('b', 'g', 'r')
for (ch, color) in zip (bgr, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.show()