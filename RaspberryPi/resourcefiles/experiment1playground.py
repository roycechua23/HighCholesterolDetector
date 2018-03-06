import cv2
import numpy as np

orig_img = cv2.imread("images/eye.jpg") # read image and assign to variable
cv2.imshow("orig_img", orig_img) # display original image
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120,
                            param1=100,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(orig_img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(orig_img,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("images/eyecircle.jpg", orig_img)
cv2.imshow("EyeCircles", orig_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
