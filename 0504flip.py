import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread('img/children.jpg')

height, width = img.shape[0:2]

d10 = 10 * np.pi / 180
f1 = np.float32([[-1, 0, width - 1], [0, 1, 0]])
f2 = np.float32([[-1, 0, width - 1], [0, -1, height - 1]])
r10 = cv2.warpAffine(img, f1, (width, height))
r20 = cv2.warpAffine(img, f2, (width, height))
cv2.imshow('', img)
cv2.imshow('f1', r10)
cv2.imshow('f2', r20)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgg = cv2.imread('img/children.jpg', cv2.IMREAD_GRAYSCALE)
dflipx = np.zeros_like(imgg)
cv2.imshow('1', imgg)
cv2.imshow('df', dflipx)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgg = cv2.imread('img/children.jpg', cv2.IMREAD_GRAYSCALE)
height, width = imgg.shape
dflipx = np.zeros_like(imgg)
for i in range(width):
    dflipx[:, i] = imgg[:, width - 1 - i]
    dflipxy = np.zeros_like(imgg)
    for i in range(height):
        dflipxy[i, :] = dflipx[height - 1 - i, :]

font = ImageFont.truetype("fonts/gulim.ttc", 20)
image_pil = Image.fromarray(dflipxy)
draw = ImageDraw.Draw(image_pil)
draw.text((200,200), "아름다운 강산-이태희", font=font, fill=(0, 0, 0))
asd = np.array(image_pil)
cv2.imshow('', img)
cv2.imshow('2', dflipx)
cv2.imshow('3', asd)
cv2.waitKey(0)
cv2.destroyAllWindows()

imgg = cv2.imread('img/children.jpg', cv2.IMREAD_GRAYSCALE)

# Horizontal and Vertical flip
dflipyx = imgg[::-1, ::-1]

# Display the original and flipped images
cv2.imshow('Original', imgg)
cv2.imshow('Horizontal and Vertical Flip', dflipyx)
cv2.waitKey(0)
cv2.destroyAllWindows()