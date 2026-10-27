import cv2

img = cv2.imread(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")

if img is not None:
    img = cv2.resize(img, (600, 400))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")