import cv2

img = cv2.imread('modi.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab  = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)




cv2.waitKey(0)
cv2.destroyAllWindows()
