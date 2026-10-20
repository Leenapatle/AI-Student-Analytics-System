import cv2
import os

name = input("Enter your name: ")

if not os.path.exists("dataset"):
    os.makedirs("dataset")

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

print("Look at the camera. Press Q to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not working!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5
    )

    for (x, y, w, h) in faces:
        count += 1

        face = gray[y:y+h, x:x+w]

        person_folder = os.path.join("dataset", name)
        os.makedirs(person_folder, exist_ok=True)

        cv2.imwrite(
            os.path.join(person_folder, f"{count}.jpg"),
            face
        )

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            frame, f"Images: {count}", (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2
        )

    cv2.imshow("Face Registration", frame)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Registration completed! Total images: {count}")