import cv2

img = cv2.imread('modi.jpg')

resized = cv2.resize(img, (1000, 300))

cv2.imwrite('modi_small.jpg', resized)
cv2.imshow('Resized', resized)
cv2.waitKey(0)  
cv2.destroyAllWindows()



