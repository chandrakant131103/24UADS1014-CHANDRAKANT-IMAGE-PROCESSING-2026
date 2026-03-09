import cv2
import numpy as np
import sys

# 1. Load the reliable image in grayscale
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not load image at {img_path}.")
    sys.exit()

# Resize for clean display windows
img = cv2.resize(img, (400, 400))

# ==========================================
# i & ii. Apply DFT and Shift zero frequency to center
# ==========================================
# Compute the 2D Discrete Fourier Transform
# cv2.DFT_COMPLEX_OUTPUT ensures the result has 2 channels (real and imaginary parts)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift the zero-frequency component to the center of the spectrum
dft_shift = np.fft.fftshift(dft)

# Calculate the magnitude spectrum for visualization only (requires log scale to be visible)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)
# Normalize to 0-255 for OpenCV display
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# ==========================================
# Prepare for Filtering
# ==========================================
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
radius = 40  # Size of the filter mask

# ==========================================
# iii. Apply Low Pass Filter (LPF)
# ==========================================
# Mask: Center circle is 1 (allows low frequencies), everything else is 0
mask_lpf = np.zeros((rows, cols, 2), np.uint8)
cv2.circle(mask_lpf, (ccol, crow), radius, (1, 1), -1)

# Apply mask and inverse DFT
fshift_lpf = dft_shift * mask_lpf
f_ishift_lpf = np.fft.ifftshift(fshift_lpf)
img_back_lpf = cv2.idft(f_ishift_lpf)
img_back_lpf = cv2.magnitude(img_back_lpf[:, :, 0], img_back_lpf[:, :, 1])
img_back_lpf = cv2.normalize(img_back_lpf, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# ==========================================
# iv. Apply High Pass Filter (HPF)
# ==========================================
# Mask: Center circle is 0 (blocks low frequencies), everything else is 1
mask_hpf = np.ones((rows, cols, 2), np.uint8)
cv2.circle(mask_hpf, (ccol, crow), radius, (0, 0), -1)

# Apply mask and inverse DFT
fshift_hpf = dft_shift * mask_hpf
f_ishift_hpf = np.fft.ifftshift(fshift_hpf)
img_back_hpf = cv2.idft(f_ishift_hpf)
img_back_hpf = cv2.magnitude(img_back_hpf[:, :, 0], img_back_hpf[:, :, 1])
img_back_hpf = cv2.normalize(img_back_hpf, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# ==========================================
# Displaying the Results
# ==========================================
cv2.imshow("1. Original Grayscale", img)
cv2.imshow("2. Magnitude Spectrum (Shifted)", magnitude_spectrum)
cv2.imshow("3. LPF Output (Blurred)", img_back_lpf)
cv2.imshow("4. HPF Output (Edges)", img_back_hpf)

# Wait for key press to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()