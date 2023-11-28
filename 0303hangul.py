import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
img = np.full((500, 1000, 3), 255, dtype=np.uint8)

# sans-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

cv2.putText(img, "아름다운강산-이태희", (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0))

# 한글 텍스트 추가
font = ImageFont.truetype("fonts/gulim.ttc", 20)
image_pil = Image.fromarray(img)
draw = ImageDraw.Draw(image_pil)
draw.text((50, 200), "아름다운 강산-이태희", font=font, fill=(0, 0, 0))
img = np.array(image_pil)

cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()