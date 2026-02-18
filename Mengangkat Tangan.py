import cv2
import mediapipe as mp


mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        landmarks = results.pose_landmarks.landmark

        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]

        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]

        h, w, c = img.shape

        ls_y = int(left_shoulder. y * h)
        lw_y = int(left_wrist. y * h)

        rs_y = int(right_shoulder. y * h)
        rw_y = int(right_wrist. y * h)

        if lw_y < ls_y:
            cv2.putText(img, "Tangan Kiri Terangkat",(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,225,0),2)

        if rw_y < rs_y:
            cv2.putText(img, "Tangan Kanan terdeteksi", (10,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,225,0),2)

    cv2.imshow("Deteksi Angkat Tangan", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



