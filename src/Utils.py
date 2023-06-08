import cv2
import pickle
import face_recognition

def encoding(name):
        temp_img = cv2.imread(f'Images\{name}.jpg')
        temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(temp_img)
        with open(r'data/Encodings.pkl', 'wb') as file:
            pickle.dump(encode, file)
        print("Face Encoding stored!")