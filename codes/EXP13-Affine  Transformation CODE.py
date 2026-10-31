
import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is None:
    print("Image not found. Check the image path.")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define three points in the original image
    pts1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Define corresponding points in the output image
    pts2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(img, matrix, (cols, rows))

    # Resize images for display
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(image, (int(w * scale), int(h * scale)))

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Affine Transformed Image", resize_image(transformed))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
