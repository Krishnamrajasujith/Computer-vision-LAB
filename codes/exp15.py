
import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is None:
    print("Image not found. Check the image path.")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner points for better visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Resize image for display
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(image, (int(w * scale), int(h * scale)))

    # Display output
    cv2.imshow("Harris Corner Detection", resize_image(img))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
