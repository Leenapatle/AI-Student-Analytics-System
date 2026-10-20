import cv2
import csv
import os
from datetime import datetime

# Load trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

names = {0: "Leena"}

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

attendance_file = "attendance.csv"

# Create CSV file if it does not exist
if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])

# Check whether today's attendance is already marked
today = datetime.now().strftime("%Y-%m-%d")
attendance_marked = False

with open(attendance_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Date"] == today and row["Name"] == "Leena":
            attendance_marked = True
            break

cap = cv2.VideoCapture(0)

print("Press Q to close the camera.")

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
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if label in names and confidence < 80:
            person_name = names[label]

            if attendance_marked:
                message = "Attendance Already Marked"

            else:
                now = datetime.now()

                with open(attendance_file, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        person_name,
                        now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                        "Present"
                    ])

                attendance_marked = True
                message = "Attendance Marked"
                print("Attendance marked successfully!")

            color = (0, 255, 0)

        else:
            person_name = "Unknown"
            message = "Not Registered"
            color = (0, 0, 255)

        cv2.rectangle(
            frame, (x, y), (x+w, y+h), color, 2
        )

        cv2.putText(
            frame,
            f"{person_name}: {message}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Attendance system closed.")