import cv2
import numpy as np

# 1. Load the image in grayscale
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not load image at {img_path}.")
    exit()

# 2. Select a target pixel (x, y) -> (column, row)
# Picking a coordinate near the center of the image
x, y = 100, 100

print(f"--- Center Target Pixel ({x}, {y}) ---")
print(f"Value: {img[y, x]}\n")

# 3. Define the coordinates for the neighbors
# Note: Image matrices are accessed via img[row, column] -> img[y, x]
n4_coords = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]           # Top, Bottom, Left, Right
nd_coords = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]   # The 4 corners
n8_coords = n4_coords + nd_coords                              # All 8 surrounding pixels

# 4. Print the values of the neighbors
print("--- 4-Point Neighbors ---")
for nx, ny in n4_coords:
    print(f"Pixel ({nx}, {ny}): {img[ny, nx]}")

print("\n--- Diagonal Neighbors ---")
for nx, ny in nd_coords:
    print(f"Pixel ({nx}, {ny}): {img[ny, nx]}")

print("\n--- 8-Point Neighbors (All) ---")
for nx, ny in n8_coords:
    print(f"Pixel ({nx}, {ny}): {img[ny, nx]}")

# 5. Change the values of those pixels to black (0)
for nx, ny in n8_coords:
    img[ny, nx] = 0

# 6. Display the result
# Because 8 pixels are too small to see, we crop a 50x50 area around it 
# and resize it massively so the black pixel ring becomes visible.
crop_size = 25
zoomed_crop = img[y-crop_size : y+crop_size, x-crop_size : x+crop_size]

# Resize using NEAREST interpolation to keep the pixels sharp and blocky
display_img = cv2.resize(zoomed_crop, (500, 500), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Zoomed View: Neighbors Changed to Black", display_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




# --- Center Target Pixel (100, 100) ---
# Value: 148

# --- 4-Point Neighbors ---
# Pixel (100, 99): 148
# Pixel (100, 101): 149
# Pixel (99, 100): 148
# Pixel (101, 100): 148

# --- Diagonal Neighbors ---
# Pixel (99, 99): 147
# Pixel (101, 99): 149
# Pixel (99, 101): 149
# Pixel (101, 101): 150

# --- 8-Point Neighbors (All) ---
# Pixel (100, 99): 148
# Pixel (100, 101): 149
# Pixel (99, 100): 148
# Pixel (101, 100): 148
# Pixel (99, 99): 147
# Pixel (101, 99): 149
# Pixel (99, 101): 149
# Pixel (101, 101): 150