import cv2

# Read input image
image = cv2.imread("sample.jpg")

# Check if image loaded
if image is None:
    print("ERROR: input.jpg not found!")
    exit()

# Create a copy for watermark
watermark = image.copy()

# Add text watermark
cv2.putText(watermark,
            "CV LAB",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2)

# Blend original and watermark
output = cv2.addWeighted(image, 0.8, watermark, 0.2, 0)

# Display result
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
