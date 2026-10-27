import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found")
        return

    img = cv2.resize(img, (600, 400))

    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.title("Image Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

analyze_histogram(r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg")