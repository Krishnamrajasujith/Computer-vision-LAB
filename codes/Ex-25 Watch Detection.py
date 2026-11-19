import cv2

# Load the Haar Cascade classifier
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")

# Read the image
image = cv2.imread("C:/Users/dhars/OneDrive/Pictures/Photo/Watch.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Check if cascade file is loaded
if watch_cascade.empty():
    print("Error: Could not load watch_cascade.xml")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image
cv2.imshow("Detected Watch", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
