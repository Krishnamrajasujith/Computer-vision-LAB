
import cv2

# Read the captured video
video = cv2.VideoCapture(
    r"C:\Users\HELLO\Videos\Screen Recordings\Screen Recording 2026-08-31 134310.mp4"
)

# Check whether the video is opened
if not video.isOpened():
    print("Video not found. Check the video path.")
else:
    fps = video.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Normal motion
    while True:
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow("Normal Motion", frame)

        if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord('q'):
            break

    # Slow motion
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        if cv2.waitKey(int(1000 / fps * 3)) & 0xFF == ord('q'):
            break

    # Fast motion
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow("Fast Motion", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
video.release()
cv2.destroyAllWindows()
