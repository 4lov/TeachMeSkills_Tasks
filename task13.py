import sqlite3

con = sqlite3.connect('task13.sqlite')
cur = con.cursor()

#teachers
cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
   teacher_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   position TEXT NOT NULL,
   age INTEGER);
""")


cur.execute("""DELETE FROM teachers""")


cur.execute("""INSERT INTO teachers(name, last_name, age, position)
   VALUES('Dima', 'Mishuta', '23', 'mentor');""")


cur.execute("""INSERT INTO teachers(name, last_name, age, position)
   VALUES('Test', 'Test', '111' ,'mentor');""")


#students
cur.execute("""CREATE TABLE IF NOT EXISTS students(
   student_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   age INTEGER,
   teacher_id INTEGER FOREING KEY);
""")


cur.execute("""DELETE FROM students""")


cur.execute("""INSERT INTO students(name, last_name, age, teacher_id) 
   VALUES('Aleksey', 'Malachow', '21', '1');""")


cur.execute("""INSERT INTO students(name, last_name, age, teacher_id) 
   VALUES('Wladimir', 'Malahit', '14', '1');""")


cur.execute("""INSERT INTO students(name, last_name, age, teacher_id) 
   VALUES('Natallia', 'Kudriava', '34', '2');""")
con.commit()


cur.execute("""SELECT teachers.name, students.name, students.last_name, students.age FROM teachers LEFT JOIN students ON teachers.teacher_id=students.teacher_id;""")
print(cur.fetchall())

