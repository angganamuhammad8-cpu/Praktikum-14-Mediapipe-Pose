import cv2
import mediapipe as mp

mpose = mp.solutions.pose
mpdraw = mp.solutions.drawing_utils

pose = mpose.Pose()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)

    if hasil.pose_landmarks:
        mpdraw.draw_landmarks(
            img,
            hasil.pose_landmarks,
            mpose.POSE_CONNECTIONS
        )

        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)

            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.putText(img, str(id), (cx, cy),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 225, 0), 1)

    cv2.imshow("Pose landmarks", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()