import cv2

img = cv2.imread('modi.jpg')
h, w = img.shape[:2]

new_w = 400
new_h = int(h * (new_w / w))

resized = cv2.resize(img, (new_w, new_h))
cv2.imwrite('out.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imshow('Resized', resized)
cv2.waitKey(0)


