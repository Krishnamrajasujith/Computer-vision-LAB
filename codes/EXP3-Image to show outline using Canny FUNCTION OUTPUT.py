import cv2

img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is not None:
    img = cv2.resize(img, (600, 400))

    edges = cv2.Canny(img, 100, 200)

    cv2.imshow("Original Image", img)
    cv2.imshow("Image Outline", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")