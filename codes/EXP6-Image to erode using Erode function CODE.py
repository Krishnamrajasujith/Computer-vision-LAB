
import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

# Check whether the image is loaded
if img is None:
    print("Image not found. Check the image path.")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Resize images while preserving proportions
    def resize_image(image, max_width=600, max_height=400):
        height, width = image.shape[:2]
        scale = min(max_width / width, max_height / height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        return cv2.resize(image, (new_width, new_height))

    original_small = resize_image(img)
    eroded_small = resize_image(eroded)

    # Display images
    cv2.imshow("Original Image", original_small)
    cv2.imshow("Eroded Image", eroded_small)

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
