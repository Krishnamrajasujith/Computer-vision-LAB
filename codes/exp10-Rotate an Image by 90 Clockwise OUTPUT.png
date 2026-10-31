
import cv2

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

# Check whether the image is loaded
if img is None:
    print("Image not found. Check the image path.")
else:
    # Rotate image 90 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Resize images for display without stretching
    def resize_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(image, (int(w * scale), int(h * scale)))

    # Display original and rotated images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Rotated Image - 90 Degrees Clockwise",
               resize_image(rotated))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
