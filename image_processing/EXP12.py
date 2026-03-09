import cv2
import numpy as np
import sys

# Load the reliable input image
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Could not load image at {img_path}.")
    sys.exit()

# Resize to standard size for clean display windows
img = cv2.resize(img, (400, 400))

# Annotate original for lab record
cv2.putText(img, 'C. Barik (24UADS1014) - Exp 12', (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

# ==========================================
# i. Add Gaussian noise and Salt & Pepper noise
# ==========================================

# 1. Add Gaussian Noise
mean = 0
sigma = 25
# Generate Gaussian noise matrix matching the image shape
gauss = np.random.normal(mean, sigma, img.shape)
# Add noise to original image and clip values to stay within 0-255 bounds
img_gaussian_noise = np.clip(img.astype(np.float32) + gauss, 0, 255).astype(np.uint8)

# 2. Add Salt & Pepper Noise
img_sp_noise = img.copy()
prob = 0.05 # 5% of the pixels will be noise
# Generate a random matrix of probabilities
rnd = np.random.rand(img.shape[0], img.shape[1])
# Apply Pepper (Black)
img_sp_noise[rnd < prob/2] = [0, 0, 0]
# Apply Salt (White)
img_sp_noise[rnd > 1 - prob/2] = [255, 255, 255]


# ==========================================
# ii. Remove using median & Gaussian filters
# ==========================================

# Median filter is mathematically best for Salt & Pepper noise
filtered_median = cv2.medianBlur(img_sp_noise, 5)

# Gaussian filter is best for Gaussian noise
filtered_gaussian = cv2.GaussianBlur(img_gaussian_noise, (5, 5), 0)


# ==========================================
# iii. Smooth using Averaging & Bilateral filter
# ==========================================
# Applying these to the original image to demonstrate pure smoothing behavior

# Averaging Filter (Blurs everything equally)
smoothed_avg = cv2.blur(img, (5, 5))

# Bilateral Filter (Smooths textures but preserves sharp edges)
smoothed_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)


# ==========================================
# Displaying the Results
# ==========================================
cv2.imshow("1. Original Image", img)

# Noise Addition Windows
cv2.imshow("2. Added Gaussian Noise", img_gaussian_noise)
cv2.imshow("3. Added Salt & Pepper Noise", img_sp_noise)

# Noise Removal Windows
cv2.imshow("4. Gaussian Noise REMOVED (Gaussian Filter)", filtered_gaussian)
cv2.imshow("5. S&P Noise REMOVED (Median Filter)", filtered_median)

# Smoothing Windows
cv2.imshow("6. Smoothed (Averaging Filter)", smoothed_avg)
cv2.imshow("7. Smoothed (Bilateral Filter)", smoothed_bilateral)

# Wait for key press to close
cv2.waitKey(0)
cv2.destroyAllWindows()








# import cv2
# import numpy as np

# img = cv2.imread("image.jpg")

# # Gaussian noise
# gauss = img + np.random.normal(0,25,img.shape).astype('uint8')

# # Median filter
# median = cv2.medianBlur(gauss,5)

# # Gaussian filter
# gaussian = cv2.GaussianBlur(gauss,(5,5),0)

# # Bilateral
# bilateral = cv2.bilateralFilter(gauss,9,75,75)

# cv2.imshow("Noise", gauss)
# cv2.imshow("Median", median)
# cv2.imshow("Gaussian", gaussian)
# cv2.imshow("Bilateral", bilateral)

# cv2.waitKey(0)
# cv2.destroyAllWindows()