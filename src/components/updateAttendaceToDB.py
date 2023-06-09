from sqlalchemy import text
from src.Utils import connection, showDB

engine = connection()

def addAttendanceToDB(attendance_list,subject):
    with engine.connect() as conn:
        print(attendance_list)
        for i in attendance_list:
            query=f"UPDATE attendance.attendancetable  SET {subject}={subject}+1 WHERE student_name='{i}' "
            conn.execute(text(query))
    
    showDB()