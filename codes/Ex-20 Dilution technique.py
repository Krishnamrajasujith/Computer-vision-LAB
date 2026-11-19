import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/images.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated_image)

    # Save the output image
    cv2.imwrite("dilated_image.jpg", dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
