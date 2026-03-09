# import cv2

# img = cv2.imread("modi.jpg",0)

# _, simple = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# adaptive = cv2.adaptiveThreshold(img,255,
# cv2.ADAPTIVE_THRESH_MEAN_C,
# cv2.THRESH_BINARY,11,2)

# _, otsu = cv2.threshold(img,0,255,
# cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# cv2.imshow("Simple", simple)
# cv2.imshow("Adaptive", adaptive)
# cv2.imshow("Otsu", otsu)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




import cv2
import sys

# 1. Load the reliable input image in grayscale
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not load image at {img_path}.")
    sys.exit()

# Resize for clean display windows
img = cv2.resize(img, (400, 400))

# ==========================================
# i. Simple Thresholding
# ==========================================
# We manually set a global threshold value (e.g., 127). 
# Pixels > 127 become white (255), else black (0).
_, thresh_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# ==========================================
# ii. Adaptive Thresholding
# ==========================================
# Calculates the threshold for small regions (11x11 block size here).
# Using a Gaussian weighted sum of neighborhood values.
thresh_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)

# ==========================================
# iii. Otsu Thresholding
# ==========================================
# Automatically calculates the optimal global threshold value.
# We pass 0 as the manual value because Otsu overrides it.
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ==========================================
# Displaying the Results
# ==========================================
cv2.imshow("1. Original Grayscale", img)
cv2.imshow("2. Simple Threshold (Global=127)", thresh_simple)
cv2.imshow("3. Adaptive Threshold (Gaussian)", thresh_adaptive)
cv2.imshow("4. Otsu Threshold (Automatic)", thresh_otsu)

# Wait for key press to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()