import cv2
import numpy as np
import sys

# 1. Load the main image and the template
# Main image
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modi.jpg"
img = cv2.imread(img_path)

# Template image (You must create this crop beforehand!)
template_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\modicopy.jpg"
template = cv2.imread(template_path)

# Safety Check
if img is None or template is None:
    print("Error: Could not load the image or the template.")
    print("Ensure 'modi.jpg' and 'modi_template.jpg' are in the directory.")
    sys.exit()

# Convert both to grayscale for the matching algorithm
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get the width (w) and height (h) of the template
h, w = template_gray.shape

# ==========================================
# i. Use cv2.matchTemplate()
# ==========================================
# TM_CCOEFF_NORMED is a highly robust method that handles lighting differences well
result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# ==========================================
# ii. Locate best match
# ==========================================
# minMaxLoc finds the global minimum and maximum in the result matrix
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# For TM_CCOEFF_NORMED, the maximum value indicates the best match
top_left = max_loc
# Calculate the bottom right corner of the bounding box using the template's dimensions
bottom_right = (top_left[0] + w, top_left[1] + h)

# ==========================================
# iii. Draw bounding box
# ==========================================
# Draw a bright green rectangle around the matched region on the ORIGINAL color image
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

# Add your credentials for the final lab record
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Match Found - C. Barik (24UADS1014) MBM Univ', 
            (10, 30), font, 0.7, (0, 255, 255), 2)

# ==========================================
# Displaying the Results
# ==========================================
cv2.imshow("1. The Template", template)
cv2.imshow("2. Matching Result (Bounding Box)", img)

# Save the final output to your folder
cv2.imwrite("experiment_16_final_output.jpg", img)

# Wait for key press to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()