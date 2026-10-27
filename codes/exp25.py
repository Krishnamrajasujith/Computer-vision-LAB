
import cv2

# Read the input image
img = cv2.imread(
    r"C:\Users\HELLO\OneDrive\Pictures\134327514668181732.jpg"
)

if img is None:
    print("Image not found. Check the image path.")
else:
    # Load a pre-trained MobileNet SSD model
    prototxt = "MobileNetSSD_deploy.prototxt"
    model = "MobileNetSSD_deploy.caffemodel"

    try:
        net = cv2.dnn.readNetFromCaffe(prototxt, model)

        # Class labels supported by MobileNet SSD
        classes = [
            "background", "aeroplane", "bicycle", "bird",
            "boat", "bottle", "bus", "car", "cat", "chair",
            "cow", "diningtable", "dog", "horse", "motorbike",
            "person", "pottedplant", "sheep", "sofa", "train",
            "tvmonitor"
        ]

        h, w = img.shape[:2]

        # Prepare image for the model
        blob = cv2.dnn.blobFromImage(
            cv2.resize(img, (300, 300)),
            0.007843, (300, 300), 127.5
        )

        net.setInput(blob)
        detections = net.forward()

        found = False

        # Detect supported objects
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                class_id = int(detections[0, 0, i, 1])
                label = classes[class_id]

                x1 = int(detections[0, 0, i, 3] * w)
                y1 = int(detections[0, 0, i, 4] * h)
                x2 = int(detections[0, 0, i, 5] * w)
                y2 = int(detections[0, 0, i, 6] * h)

                cv2.rectangle(
                    img, (x1, y1), (x2, y2), (0, 255, 0), 2
                )
                cv2.putText(
                    img, label, (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 0), 2
                )

                if label == "watch":
                    found = True

        if found:
            print("Watch detected!")
        else:
            print("Watch not detected by this model.")

        # Resize for display
        h, w = img.shape[:2]
        scale = min(600 / w, 400 / h)
        display = cv2.resize(
            img, (int(w * scale), int(h * scale))
        )

        cv2.imshow("Object Recognition", display)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except cv2.error:
        print("Model files not found or could not be loaded.")
        print("Download the MobileNet SSD model files first.")