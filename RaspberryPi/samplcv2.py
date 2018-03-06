import cv2

img = cv2.imread("out.jpg")
cv2.imshow("Captured Image", img)
## cv2.imwrite("out.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()