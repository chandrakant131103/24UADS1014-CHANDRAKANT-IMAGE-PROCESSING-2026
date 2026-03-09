import cv2
import numpy as np

img = cv2.imread("modi.jpg",0)

sobel = cv2.Sobel(img,cv2.CV_64F,1,0)

kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
prewitt = cv2.filter2D(img,-1,kernel)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

canny = cv2.Canny(img,100,200)

cv2.imshow("Sobel",sobel)
cv2.imshow("Prewitt",prewitt)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("Canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
















# import cv2
# import numpy as np
# import sys

# # 1. Load the image in grayscale
# img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
# img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# if img is None:
#     print(f"Error: Could not load image at {img_path}.")
#     sys.exit()

# # Resize for clean display windows
# img = cv2.resize(img, (400, 400))

# # Apply a slight Gaussian blur to reduce noise before edge detection
# img_blurred = cv2.GaussianBlur(img, (3, 3), 0)

# # ==========================================
# # i. Sobel Edge Detection
# # ==========================================
# # Compute gradients along the X and Y axes
# sobel_x = cv2.Sobel(img_blurred, cv2.CV_64F, 1, 0, ksize=3)
# sobel_y = cv2.Sobel(img_blurred, cv2.CV_64F, 0, 1, ksize=3)

# # Convert back to uint8 (0-255) and combine them
# sobel_x = cv2.convertScaleAbs(sobel_x)
# sobel_y = cv2.convertScaleAbs(sobel_y)
# sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)


# # ==========================================
# # ii. Prewitt Edge Detection (Manual Kernel)
# # ==========================================
# # Define the manual Prewitt kernels
# kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
# kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

# # Apply the manual kernels using filter2D
# prewitt_x = cv2.filter2D(img_blurred, -1, kernel_prewitt_x)
# prewitt_y = cv2.filter2D(img_blurred, -1, kernel_prewitt_y)

# # Convert back to uint8 and combine them
# prewitt_x = cv2.convertScaleAbs(prewitt_x)
# prewitt_y = cv2.convertScaleAbs(prewitt_y)
# prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)


# # ==========================================
# # iii. Laplacian Edge Detection
# # ==========================================
# # Laplacian calculates the 2nd derivative to find edges
# laplacian = cv2.Laplacian(img_blurred, cv2.CV_64F)
# laplacian = cv2.convertScaleAbs(laplacian)


# # ==========================================
# # iv. Canny Edge Detection
# # ==========================================
# # Canny is a multi-stage algorithm (uses hysteresis thresholding)
# # 100 and 200 are the lower and upper thresholds
# canny = cv2.Canny(img_blurred, 100, 200)


# # ==========================================
# # Displaying the Results
# # ==========================================
# cv2.imshow("1. Original Grayscale", img)
# cv2.imshow("2. Sobel Edges", sobel_combined)
# cv2.imshow("3. Prewitt Edges", prewitt_combined)
# cv2.imshow("4. Laplacian Edges", laplacian)
# cv2.imshow("5. Canny Edges", canny)

# # Wait for key press to close windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()