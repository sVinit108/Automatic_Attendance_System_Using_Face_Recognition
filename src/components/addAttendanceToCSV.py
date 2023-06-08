import pandas as pd

csv = pd.read_csv(r"data/attendance.csv")

def addAttendanceToCSV(attendance_list,subject):
    for name in attendance_list:
        csv.loc[(csv.Student_name==name),[subject]]= csv.loc[(csv.Student_name==name),[subject]]+1
        csv.to_csv('Attendance.csv')
        print('Attendance updated\n')
        print(csv)