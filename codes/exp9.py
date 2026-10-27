
import cv2

# Read the image
img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is None:
    print("Image not found. Check the image path.")
else:
    # Scale image bigger and smaller
    bigger = cv2.resize(img, None, fx=2, fy=2,
                        interpolation=cv2.INTER_CUBIC)

    smaller = cv2.resize(img, None, fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_AREA)

    # Function to fit images within display size
    def fit_image(image, max_width=600, max_height=400):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        return cv2.resize(image, (int(w * scale), int(h * scale)))

    # Display resized previews
    cv2.imshow("Original Image", fit_image(img))
    cv2.imshow("Bigger Image", fit_image(bigger))
    cv2.imshow("Smaller Image", fit_image(smaller))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
