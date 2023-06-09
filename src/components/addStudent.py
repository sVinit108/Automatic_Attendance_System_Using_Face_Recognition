import cv2
import pickle
import pandas as pd
from PIL import Image
from src.Utils import encoding
from src.components.DBStudentInsert import insertstudent

df = pd.read_csv(r'data/attendance.csv',index_col='Index')

def addStudent():
    '''Adds a new student's attendance record in Database & his/her image in Image folder'''

    name = input('Enter your name: ')
    if name not in df['Student_name'].values:
        eng = int(input('English Attendance: '))
        math = int(input('Math Attendance: '))
        sci = int(input('Science Attendance: '))

        df.loc[len(df.index)] = [name,eng,math,sci]
        df.to_csv(r'data/attendance.csv')
        print(df)

        insertstudent(name,eng,math,sci)

        cap=cv2.VideoCapture(0)
        while True:
            _,frame=cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            img = Image.fromarray(frame)
            img.convert('RGB')
            img.save(f'Images\{name}.jpg')

            encoding(name)

            cv2.imshow('Face Cropper',frame)

            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cap.release()
        cv2.destroyAllWindows()

        with open(r'data/Names.pkl','wb') as file:
            pickle.dump(name,file)

        print('Name added sucessfully')
    else: 
        return print("Name already present inside DB")