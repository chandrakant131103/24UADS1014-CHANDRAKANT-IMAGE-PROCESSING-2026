import cv2
import numpy as np
import sys

# 1. Load the reliable input image
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Could not load image at {img_path}.")
    sys.exit()

# Resize base image to a standard 400x400 so the pop-up windows fit on screen
img = cv2.resize(img, (400, 400))
h, w = img.shape[:2]

# Annotate the original image for your lab record
cv2.putText(img, 'C. Barik (24UADS1014)', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

# ==========================================
# i. Scaling, Rotation and Flipping
# ==========================================

# --- SCALING ---
# Shrink to half size (0.5x)
img_scaled_down = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Enlarge to 1.5x size
img_scaled_up = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# --- ROTATION ---
# Rotate 45 degrees counter-clockwise around the center of the image
center = (w // 2, h // 2)
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
img_rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

# --- FLIPPING ---
img_flipped_h = cv2.flip(img, 1)  # 1 = Horizontal flip (mirror)
img_flipped_v = cv2.flip(img, 0)  # 0 = Vertical flip (upside down)

# ==========================================
# ii. Translation using affine matrix
# ==========================================

# Shift the image by tx=100 pixels right, and ty=50 pixels down
tx, ty = 100, 50
# Create the 2x3 affine translation matrix M of float32 type
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the affine transformation
img_translated = cv2.warpAffine(img, translation_matrix, (w, h))

# ==========================================
# Displaying the Results
# ==========================================
cv2.imshow("1. Original", img)
cv2.imshow("2. Scaled Down (0.5x)", img_scaled_down)
cv2.imshow("3. Scaled Up (1.5x)", img_scaled_up)
cv2.imshow("4. Rotated (45 deg)", img_rotated)
cv2.imshow("5. Flipped Horizontally", img_flipped_h)
cv2.imshow("6. Flipped Vertically", img_flipped_v)
cv2.imshow("7. Translated", img_translated)

# Wait for key press to clean up
cv2.waitKey(0)
cv2.destroyAllWindows()