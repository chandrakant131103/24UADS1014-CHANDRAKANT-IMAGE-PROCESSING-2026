import cv2
import sys

# 1. Load an image containing multiple objects
# Make sure to place an image named 'objects.jpg' in your folder, 
# or change this filename to one you already have.
img_path = r"C:\IP\24UADS1014-CHANDRAKANT-IMAGE-PROCESSING-2026-main\image_processing\EXP8.jpg"
img = cv2.imread(img_path)

# Safety Check to prevent the !ssize.empty() error
if img is None:
    print(f"Error: Could not load image Aat {img_path}. Please check the path.")
    sys.exit()

# 2. Draw Geometrical Shapes to highlight objects

# Draw a Green Rectangle (e.g., to highlight a boxy object)
# Syntax: cv2.rectangle(image, top_left_corner, bottom_right_corner, color_BGR, thickness)
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 3)

# Draw a Red Circle (e.g., to highlight a round object)
# Syntax: cv2.circle(image, center_coordinates, radius, color_BGR, thickness)
cv2.circle(img, (400, 150), 75, (0, 0, 255), 3)

# Draw a Blue Line (e.g., pointing to an object or underlining something)
# Syntax: cv2.line(image, start_point, end_point, color_BGR, thickness)
cv2.line(img, (50, 320), (450, 320), (255, 0, 0), 3)

# 3. Annotate the image with Text
# Syntax: cv2.putText(image, text, bottom_left_corner, font, font_scale, color_BGR, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Annotated by: Chandrakant Barik', (20, 400), font, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

# 4. Display and Save the result
cv2.imshow("Annotated Image", img)
cv2.imwrite("experiment_8_annotated.jpg", img)

# Wait for a key press and clean up windows
cv2.waitKey(0)
cv2.destroyAllWindows()