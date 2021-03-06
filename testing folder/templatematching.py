import cv2
import numpy as np

# read image
img_rgb = cv2.imread('/home/bence/binarycc2.jpg')
# convert to gray
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# read template
template = cv2.imread('/home/bence/template.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
cv2.imwrite('res.png', img_rgb)
