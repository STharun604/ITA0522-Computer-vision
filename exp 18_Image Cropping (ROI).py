import cv2

# Read input image
image = cv2.imread("sample.jpg")

# Check if image loaded
if image is None:
    print("ERROR: input.jpg not found!")
    exit()

# Select ROI (Region of Interest)
roi = image[50:200, 50:200]   # [y1:y2, x1:x2]

# Paste ROI to another location
image[250:400, 250:400] = roi

# Display result
cv2.imshow("Cropped and Pasted Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
