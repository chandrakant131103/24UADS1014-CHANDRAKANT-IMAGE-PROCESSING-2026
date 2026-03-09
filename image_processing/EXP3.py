import cv2

img = cv2.imread('modi.jpg')

resized = cv2.resize(img, (300, 300))

cv2.imwrite('modi_small.jpg', resized)
cv2.imshow('Resized', resized)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# With aspect ratio

h, w = img.shape[:2]

new_w = 300
new_h = int(h * (new_w / w))

resized = cv2.resize(img, (new_w, new_h))
cv2.imwrite('out.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imshow('Resized', resized)
cv2.waitKey(0)



# : Crop center (1/8 size)

h, w = img.shape[:2]

ch = h//8
cw = w//8

start_x = w//2 - cw//2
start_y = h//2 - ch//2

crop = img[start_y:start_y+ch, start_x:start_x+cw]

cv2.imshow("Crop", crop)
cv2.waitKey(0)
