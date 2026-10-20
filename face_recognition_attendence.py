import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

names = {
    0: "Leena"
}

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

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
        else:
            person_name = "Unknown"

        cv2.rectangle(
            frame, (x, y), (x+w, y+h), (0, 255, 0), 2
        )

        cv2.putText(
            frame, person_name, (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()