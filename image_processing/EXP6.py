import cv2
import sys

# 1. Load the images
img1 = cv2.imread("modi.jpg")
img2 = cv2.imread("modi2.jpg")

# 2. Safety Check: Verify both images loaded successfully
if img1 is None:
    print("Error: Could not load 'modi.jpg'. Check the file path and name.")
    sys.exit()
if img2 is None:
    print("Error: Could not load 'rahulreal.jpg'. Check the file path and name.")
    sys.exit()

# 3. Resize img2 to match img1's dimensions
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# --- Arithmetic Operations ---
add = cv2.add(img1, img2)
sub = cv2.subtract(img1, img2)
mul = cv2.multiply(img1, img2)
div = cv2.divide(img1, img2)

# --- Logical Operations ---
AND = cv2.bitwise_and(img1, img2)
OR = cv2.bitwise_or(img1, img2)
XOR = cv2.bitwise_xor(img1, img2)
NOT = cv2.bitwise_not(img1)

# Derived Logical Operations (NAND, NOR, EXNOR)
NAND = cv2.bitwise_not(AND)
NOR = cv2.bitwise_not(OR)
EXNOR = cv2.bitwise_not(XOR)

# --- Display Arithmetic ---
cv2.imshow("Add", add)
cv2.imshow("Subtract", sub)
cv2.imshow("Multiply", mul)
cv2.imshow("Divide", div)

# --- Display Logical ---
cv2.imshow("AND", AND)
cv2.imshow("OR", OR)
cv2.imshow("XOR", XOR)
cv2.imshow("NOT (Img1)", NOT)
cv2.imshow("NAND", NAND)
cv2.imshow("NOR", NOR)
cv2.imshow("EXNOR", EXNOR)

# Wait for a key press and clean up windows
cv2.waitKey(0)
cv2.destroyAllWindows()