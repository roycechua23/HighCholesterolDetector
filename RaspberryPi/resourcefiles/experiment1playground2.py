import cv2
import numpy as np

orig_img = cv2.imread("eye.jpg") # read image and assign to variable
cv2.imshow("orig_img", orig_img) # display original image
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# cv2.imwrite("images/eyecircle.jpg", orig_img)
cv2.imshow("Eye", cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
