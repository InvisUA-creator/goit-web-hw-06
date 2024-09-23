import sqlite3
import random
from faker import Faker


conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
fake = Faker()

cur.execute(
    """CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY,
             first_name TEXT,
             last_name TEXT,
             group_id INTEGER REFERENCES groups(id))"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS groups
             (id INTEGER PRIMARY KEY,
             name TEXT)"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS teachers
             (id INTEGER PRIMARY KEY,
             first_name name TEXT,
             last_name TEXT)"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS subjects
             (id INTEGER PRIMARY KEY,
             name TEXT,
             teacher_id INTEGER REFERENCES teachers(id))"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS grades (
               id INTEGER PRIMARY KEY,
               student_id INTEGER REFERENCES students(id),
               subject_id INTEGER REFERENCES subjects(id),
               grade INTEGER,
               date DATE
            )"""
)

groups = ["Group 1", "Group 2", "Group 3"]
for group in groups:
    cur.execute("INSERT INTO groups (name) VALUES (?)", (group,))

teachers = []
for _ in range(5):
    firs_name = Faker().first_name()
    last_name = Faker().last_name()
    teachers.append((firs_name, last_name))

for teacher in teachers:
    cur.execute("INSERT INTO teachers (first_name, last_name) VALUES (?, ?)", teacher)

subjects = [
    ("Mathematics", 1),
    ("Physics", 2),
    ("Chemistry", 3),
    ("Biology", 4),
    ("Computer Science", 5),
]

for subject in subjects:
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subject)

students = []
for i in range(50):
    first_name = Faker().first_name()
    last_name = Faker().last_name()
    group_id = random.randint(1, 3)
    students.append((first_name, last_name, group_id))

for student in students:
    cur.execute("SELECT id FROM students WHERE id = ?", (student[0],))
result = cur.fetchone()
if result:
    cur.execute(
        "UPDATE students SET first_name = ?, last_name = ?, group_id = ? WHERE id = ?",
        (student[0], student[1], student[2], student[3]))
else:
    cur.execute(
        "INSERT INTO students (id, first_name, last_name, group_id) VALUES (?, ?, ?, ?)",
        student,
    )
    cur.execute(
        "INSERT INTO students (id, first_name, last_name, group_id) VALUES (?, ?, ?)",
        student,
    )

grades = []
for student_id in range(1, 51):
    for subject_id in range(1, 6):
        grade = random.randint(1, 100)
        date = Faker().date_between(start_date="-3y", end_date="today")
        grades.append((student_id, subject_id, grade, date))

for grade in grades:
    cur.execute(
        "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
        grade,
    )


conn.commit()

cur.close()
conn.close()
