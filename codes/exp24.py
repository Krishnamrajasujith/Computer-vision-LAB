
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

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Black-Hat operation
    blackhat = cv2.morphologyEx(
        gray, cv2.MORPH_BLACKHAT, kernel
    )

    # Resize images for display
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(
            image, (int(w * scale), int(h * scale))
        )

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Grayscale Image", resize_image(gray))
    cv2.imshow("Black-Hat Image", resize_image(blackhat))

    # Save the result
    cv2.imwrite("blackhat_image.jpg", blackhat)

    print("Black-Hat operation applied successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
