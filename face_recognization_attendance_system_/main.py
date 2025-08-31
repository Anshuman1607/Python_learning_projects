import face_recognition
import face_recognition as fr
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)
anshuman_image = face_recognition.load_image_file("faces/Anshuman.png")
salman_image = face_recognition.load_image_file("faces/Salman.png")
akshay_image = face_recognition.load_image_file("faces/Akshay.png")
# face encodings
anshuman_encoding = face_recognition.face_encodings(anshuman_image)[0]
salman_encoding = face_recognition.face_encodings(salman_image)[0]
akshay_encoding = face_recognition.face_encodings(akshay_image)[0]

known_encodings = [anshuman_encoding, salman_encoding, akshay_encoding]
known_names = ["Anshuman", "Salman", "Akshay"]
students = known_names.copy()
face_locations = []
face_encodings = []
# get the current date and time
now = datetime.now()
current_day = now.strftime("%d-%m-%Y")
f = open(f"{current_day}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    #recognize faces
    face_location = fr.face_locations(rgb_small_frame)
    face_encoding = fr.face_encodings(rgb_small_frame, face_location)
    for face_encoded in face_encoding:
        matches = fr.compare_faces(known_encodings, face_encoded)
        face_distances = fr.face_distance(known_encodings, face_encoded)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
    # add the text if a person is present
        if name in known_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame,name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
        if name in students:
            students.remove(name)
            current_time = now.strftime("%H:%M:%S")
            lnwriter.writerow([current_time, name])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()