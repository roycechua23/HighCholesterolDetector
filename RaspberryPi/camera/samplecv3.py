import cv2

img = cv2.imread("normaleye.jpg")
cv2.imshow("normal eye",img)
cv2.waitKey(0)
cv2.destroyAllWindows()