import cv2
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/images.jpg")
if image is None:
    print("Error: Image not found!")
else:
    roi = image[100:300, 150:350]
    roi_copy = roi.copy()
    image[50:250, 400:600] = roi_copy
    cv2.imshow("Original with ROI Pasted", image)
    cv2.imshow("Cropped ROI", roi)
    cv2.imwrite("Original with ROI Pasted", image)
    cv2.imwrite("roi_output.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
