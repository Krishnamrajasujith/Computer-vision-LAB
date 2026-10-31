
import cv2
import numpy as np

# Read the image
img = cv2.imread(
    r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg"
)

if img is None:
    print("Image not found. Check the image path.")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Resize images for display without stretching
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(
            image, (int(w * scale), int(h * scale))
        )

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Erosion Image", resize_image(eroded))

    # Save the eroded image
    cv2.imwrite("eroded_image.jpg", eroded)

    print("Erosion applied successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()