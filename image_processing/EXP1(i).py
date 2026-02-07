import cv2

img = cv2.imread('modi.jpg')
if img is None:
    print("Still not found")
else:
    print("Loaded OK")
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv2.imwrite('modi_gray.jpg', img)

print("Image saved")

