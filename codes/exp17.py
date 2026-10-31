
import cv2

# Read the original image
img = cv2.imread(
    r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg"
)

if img is None:
    print("Image not found. Check the image path.")
else:
    # Copy the original image
    watermarked = img.copy()

    # Watermark text
    watermark = "COPYRIGHT"

    # Set font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color
    thickness = 2

    # Get image dimensions
    h, w = img.shape[:2]

    # Set watermark position at bottom-right
    text_size = cv2.getTextSize(
        watermark, font, font_scale, thickness
    )[0]

    x = max(0, w - text_size[0] - 20)
    y = max(text_size[1], h - 20)

    # Add watermark to the image
    cv2.putText(
        watermarked,
        watermark,
        (x, y),
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    # Resize images for display
    def resize_image(image, max_width=600, max_height=400):
        height, width = image.shape[:2]
        scale = min(max_width / width, max_height / height)
        return cv2.resize(
            image,
            (int(width * scale), int(height * scale))
        )

    # Display images
    cv2.imshow("Original Image", resize_image(img))
    cv2.imshow("Watermarked Image", resize_image(watermarked))

    # Save the watermarked image
    cv2.imwrite("watermarked_image.jpg", watermarked)
    print("Watermark added successfully!")
    print("Saved as watermarked_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
