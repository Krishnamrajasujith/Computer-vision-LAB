
import cv2

# Read the source image
img = cv2.imread(
    r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg"
)

if img is None:
    print("Image not found. Check the image path.")
else:
    # Get image dimensions
    h, w = img.shape[:2]

    # Select ROI (center region)
    x1 = w // 4
    y1 = h // 4
    x2 = 3 * w // 4
    y2 = 3 * h // 4

    # Crop the selected region
    roi = img[y1:y2, x1:x2]

    # Copy the original image
    copied_img = img.copy()

    # Paste ROI at the top-left corner
    rh, rw = roi.shape[:2]
    copied_img[0:rh, 0:rw] = roi.copy()

    # Resize images for display
    def resize_image(image, max_width=600, max_height=400):
        height, width = image.shape[:2]
        scale = min(max_width / width, max_height / height)
        return cv2.resize(
            image,
            (int(width * scale), int(height * scale))
        )

    # Display results
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Cropped ROI", resize_image(roi))
    cv2.imshow("Copied and Pasted ROI", resize_image(copied_img))

    # Save the results
    cv2.imwrite("cropped_roi.jpg", roi)
    cv2.imwrite("pasted_roi.jpg", copied_img)

    print("ROI cropped, copied and pasted successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
