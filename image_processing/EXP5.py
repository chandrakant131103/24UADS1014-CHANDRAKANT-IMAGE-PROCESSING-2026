import cv2
import numpy as np

# Read image (BGR format by default in OpenCV)
img = cv2.imread("modi.jpg")

# Resize for better display (optional)
img = cv2.resize(img, (400, 400))

# ---------------------------------------------------
# 1. COLOR SPACE CONVERSIONS
# ---------------------------------------------------

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gray to Binary (Thresholding)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# ---------------------------------------------------
# CMY Conversion
# Formula: CMY = 255 - RGB
# ---------------------------------------------------
cmy = 255 - rgb


# ---------------------------------------------------
# CMYK Conversion
# ---------------------------------------------------
rgb_norm = rgb / 255.0

K = 1 - np.max(rgb_norm, axis=2)

C = (1 - rgb_norm[:,:,0] - K) / (1 - K + 1e-5)
M = (1 - rgb_norm[:,:,1] - K) / (1 - K + 1e-5)
Y = (1 - rgb_norm[:,:,2] - K) / (1 - K + 1e-5)

C = (C * 255).astype(np.uint8)
M = (M * 255).astype(np.uint8)
Y = (Y * 255).astype(np.uint8)
K = (K * 255).astype(np.uint8)


# ---------------------------------------------------
# 2. COLOR COMPONENT EXTRACTION (Split)
# ---------------------------------------------------

# RGB channels
R, G, B = cv2.split(rgb)

# CMY channels
C1, M1, Y1 = cv2.split(cmy)

# HSV channels
H, S, V = cv2.split(hsv)


# ---------------------------------------------------
# 3. COMBINING COLOR COMPONENTS (Merge)
# ---------------------------------------------------

rgb_merge = cv2.merge((R, G, B))
cmy_merge = cv2.merge((C1, M1, Y1))
hsv_merge = cv2.merge((H, S, V))


# ---------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------

cv2.imshow("Original", img)

cv2.imshow("RGB", rgb)
cv2.imshow("HSV", hsv)
cv2.imshow("Gray", gray)
cv2.imshow("Binary", binary)

cv2.imshow("CMY", cmy)

cv2.imshow("C channel", C)
cv2.imshow("M channel", M)
cv2.imshow("Y channel", Y)
cv2.imshow("K channel", K)

# Split channels
cv2.imshow("Red channel", R)
cv2.imshow("Green channel", G)
cv2.imshow("Blue channel", B)

cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)

# Merged images
cv2.imshow("Merged RGB", rgb_merge)
cv2.imshow("Merged CMY", cmy_merge)
cv2.imshow("Merged HSV", hsv_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()