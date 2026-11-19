import cv2
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/images.jpg")
if image is None:
    print("Error: Image not found!")
else:
    overlay = image.copy()
    cv2.putText(
        overlay,
        "Dharshan",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 255, 255),
        4,
        cv2.LINE_AA
    )
    alpha = 0.4
    watermarked = cv2.addWeighted(
        overlay,
        alpha,
        image,
        1 - alpha,
        0
    )
    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked)
    cv2.imwrite("watermarked_image.jpg", watermarked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
