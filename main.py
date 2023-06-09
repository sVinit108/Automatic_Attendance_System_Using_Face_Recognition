import warnings
import pandas as pd
from src.components.addStudent import addStudent
from src.pipelines.UpdateAttendance import UpdateAttendance

# Ignore all warnings
warnings.filterwarnings("ignore")

csv = pd.read_csv(r"data\attendance.csv")

while True:
    user_input = input('''Hi!
    Which Option do you want to select:-
    \t 1. Get Attendace
    \t 2. Update Attendance
    \t 3. Get Students List
    \t 4. Add Student \n''')

    if user_input=='q':
        break

    elif user_input=='1':
        print(csv)

    elif user_input=='2':
        UpdateAttendance()

    elif user_input=='3':
        print(csv.Student_name)

    elif user_input=='4':
        addStudent()

    else:
        print("Invalid input")