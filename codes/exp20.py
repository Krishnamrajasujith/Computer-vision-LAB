
import cv2
import numpy as np

# Read the image
img = cv2.imread(
    r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg"
)

if img is None:
    print("Image not found. Check the image path.")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert image to binary
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Resize images for display without stretching
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(
            image, (int(w * scale), int(h * scale))
        )

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Binary Image", resize_image(binary))
    cv2.imshow("Dilated Image", resize_image(dilated))

    # Save the dilated image
    cv2.imwrite("dilated_image.jpg", dilated)

    print("Dilation applied successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
