
import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is None:
    print("Image not found. Check the image path.")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define four points in the original image
    pts1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Define four destination points
    pts2 = np.float32([
        [50, 50],
        [cols - 100, 30],
        [30, rows - 50],
        [cols - 50, rows - 30]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(img, matrix, (cols, rows))

    # Resize images for display without stretching
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(image, (int(w * scale), int(h * scale)))

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Perspective Transformed Image", resize_image(transformed))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
