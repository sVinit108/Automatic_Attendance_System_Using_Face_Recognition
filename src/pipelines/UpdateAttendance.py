import cv2
import pickle
import numpy as np
import face_recognition
from src.components.addAttendanceToCSV import addAttendanceToCSV
from src.components.updateAttendaceToDB import addAttendanceToDB

def UpdateAttendance():
    with open(r'data/Encodings.pkl', 'rb') as file:
        encodeListKnown = pickle.load(file)
    with open(r'data/Names.pkl', 'rb') as file:
        Names=[]
        while True:
            try:            
                string = pickle.load(file)
                Names.append(string)
            except EOFError:
                break
    
    cap = cv2.VideoCapture(0)

    attendance_list=[]
    while True:
        _, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceLocation = face_recognition.face_locations(imgS)
        faceEncoding = face_recognition.face_encodings(imgS, faceLocation)

        for encodeFace, faceLoc in zip(faceEncoding, faceLocation):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = Names[matchIndex]
                if name not in attendance_list:
                    attendance_list.append(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1+10, y1+10), (x2+10, y2+10), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Webcam', img)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

    print(attendance_list)

    subject = input('Attendance for which subject?: ')
    addAttendanceToCSV(attendance_list,subject.upper())
    addAttendanceToDB(attendance_list,subject.lower())