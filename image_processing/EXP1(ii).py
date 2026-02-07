import cv2

img = cv2.imread('modi.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('modi_gray.jpg', gray)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
