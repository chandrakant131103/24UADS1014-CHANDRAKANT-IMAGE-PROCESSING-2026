import cv2
import numpy as np
import sys

# 1. Load the image and convert to binary
# Using the absolute path to prevent the !ssize.empty() error
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path, 0)

if img is None:
    print(f"Error: Could not load {img_path}")
    sys.exit()

# Convert to Binary (Black & White)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 2. Artificially add "Noise" and "Gaps" to demonstrate the filters properly
noisy_img = binary.copy()
gappy_img = binary.copy()

# Add Noise (White dots in the dark background)
cv2.circle(noisy_img, (50, 50), 3, 255, -1)
cv2.circle(noisy_img, (100, 50), 4, 255, -1)
cv2.circle(noisy_img, (150, 80), 2, 255, -1)

# Add Gaps (Black holes inside the white foreground)
cv2.circle(gappy_img, (200, 200), 3, 0, -1)
cv2.circle(gappy_img, (250, 250), 4, 0, -1)
cv2.circle(gappy_img, (300, 220), 2, 0, -1)

# 3. Define the structuring element (Kernel)
kernel = np.ones((5, 5), np.uint8)

# 4. Perform Morphological Operations
# i. Dilation & Erosion
erosion = cv2.erode(binary, kernel)
dilation = cv2.dilate(binary, kernel)

# ii. Remove noise using opening
opening = cv2.morphologyEx(noisy_img, cv2.MORPH_OPEN, kernel)

# iii. Fill gaps using closing
closing = cv2.morphologyEx(gappy_img, cv2.MORPH_CLOSE, kernel)

# 5. Display the Results
# Dilation & Erosion
cv2.imshow("1. Original Binary", binary)
cv2.imshow("2. Erosion (Shrunk)", erosion)
cv2.imshow("3. Dilation (Expanded)", dilation)

# Noise Removal (Opening)
cv2.imshow("4. Image WITH Noise", noisy_img)
cv2.imshow("5. Noise Removed (OPENING)", opening)

# Gap Filling (Closing)
cv2.imshow("6. Image WITH Gaps", gappy_img)
cv2.imshow("7. Gaps Filled (CLOSING)", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()