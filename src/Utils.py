import cv2
import pickle
import face_recognition
from sqlalchemy import create_engine, text

def encoding(name):
        temp_img = cv2.imread(f'Images\{name}.jpg')
        temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(temp_img)
        with open(r'data/Encodings.pkl', 'wb') as file:
            pickle.dump(encode, file)
            print("Face Encoding stored!")

def connection():
    password = 'Vinit#108' 
    engine = create_engine('mysql+pymysql://root:{}@localhost:3307/attendance'.format(password))
    return engine
    # For testing connection
    # with engine.connect() as conn:
    #     query="SELECT * from attendance.attendanceTable;"
    #     result = conn.execute(text(query))

    # print(list(result))

def showDB() -> list:
    engine = connection()
    with engine.connect() as conn:
        query="SELECT * FROM attendance.attendanceTable;"
        result = conn.execute(text(query))
        result = result.fetchall()
        for i in result:
            return i