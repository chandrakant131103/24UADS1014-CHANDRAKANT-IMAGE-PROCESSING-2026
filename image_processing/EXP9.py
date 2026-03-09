import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# 1. Load Images in Grayscale
# Make sure to add 'overexposed.jpg' and 'underexposed.jpg' to this directory
path_over = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\overexposed.jpg"
path_under = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\underexposed.jpg"

img_over = cv2.imread(path_over, cv2.IMREAD_GRAYSCALE)
img_under = cv2.imread(path_under, cv2.IMREAD_GRAYSCALE)

# Safety Check
if img_over is None or img_under is None:
    print("Error: Missing input images.")
    print("Please ensure 'overexposed.jpg' and 'underexposed.jpg' exist in your folder.")
    sys.exit()

# i. Histogram Equalization
eq_over = cv2.equalizeHist(img_over)
eq_under = cv2.equalizeHist(img_under)

# ii. Power Law (Gamma) Transformation
# Choosing gamma values to correct the specific exposure issues
gamma_over = 2.0  # > 1 darkens the overexposed image
gamma_under = 0.5 # < 1 brightens the underexposed image

# Formula: Output = 255 * (Input/255) ^ gamma
pl_over = np.array(255 * ((img_over / 255.0) ** gamma_over), dtype='uint8')
pl_under = np.array(255 * ((img_under / 255.0) ** gamma_under), dtype='uint8')

# iv. Perform Image Negation
neg_over = cv2.bitwise_not(img_over)
neg_under = cv2.bitwise_not(img_under)

# Displaying Images using OpenCV
cv2.imshow("Overexposed - Original", img_over)
cv2.imshow("Overexposed - Equalized", eq_over)
cv2.imshow("Overexposed - Gamma (2.0)", pl_over)
cv2.imshow("Overexposed - Negative", neg_over)

cv2.imshow("Underexposed - Original", img_under)
cv2.imshow("Underexposed - Equalized", eq_under)
cv2.imshow("Underexposed - Gamma (0.5)", pl_under)
cv2.imshow("Underexposed - Negative", neg_under)

# iii. Plot Histograms (Before and After Equalization)
plt.figure(figsize=(12, 8))
plt.suptitle("C. Barik (24UADS1014) - Histogram Comparisons", fontsize=14)

plt.subplot(2, 2, 1)
plt.hist(img_over.ravel(), 256, range=[0, 256], color='red')
plt.title('Overexposed - Original Histogram')

plt.subplot(2, 2, 2)
plt.hist(eq_over.ravel(), 256, range=[0, 256], color='green')
plt.title('Overexposed - Equalized Histogram')

plt.subplot(2, 2, 3)
plt.hist(img_under.ravel(), 256, range=[0, 256], color='blue')
plt.title('Underexposed - Original Histogram')

plt.subplot(2, 2, 4)
plt.hist(eq_under.ravel(), 256, range=[0, 256], color='purple')
plt.title('Underexposed - Equalized Histogram')

plt.tight_layout()

# This will open the Matplotlib window with your charts
plt.show()

# Wait for key press to close the OpenCV image windows
cv2.waitKey(0)
cv2.destroyAllWindows()