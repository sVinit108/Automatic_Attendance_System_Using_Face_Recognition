from sqlalchemy import text
from src.Utils import connection

def insertstudent(name,english,maths,science):
    engine = connection()
    with engine.connect() as conn:
        query=f"Insert into attendance.attendancetable (student_name,english,maths,science) Values ('{name}',{english},{maths},{science});"
        conn.execute(text(query))
        print("Student added in DB")