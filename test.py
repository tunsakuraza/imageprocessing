import cv2
import numpy as np

img = cv2.imread('haar.png')


cv2.rectangle(img,(9,9),(15,16),(255,255,255),-1)
cv2.rectangle(img,(11,9),(13,16),(0,0,0),-1)



# cv2.imshow('image', img)
cv2.imwrite("colorS0T9.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
