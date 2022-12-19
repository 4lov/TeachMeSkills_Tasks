import sqlite3

con = sqlite3.connect('task14.sqlite')
cur = con.cursor()

#Связь о2о

cur.execute("""CREATE TABLE IF NOT EXISTS employees(
   employee_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL);
""")

cur.execute("""DELETE FROM employees""")

cur.execute("""INSERT INTO employees(name) 
   VALUES('Aleksey');""")

cur.execute("""CREATE TABLE IF NOT EXISTS workplaces(
   workplace_id INTEGER PRIMARY KEY,
   number TEXT NOT NULL,
   employee_id INTEGER,
   FOREIGN KEY (employee_id) REFERENCES employees(id));
""")

cur.execute("""DELETE FROM workplaces""")

cur.execute("""INSERT INTO workplaces(number, employee_id) 
   VALUES('A22', '1');""")

con.commit()


#Связь o2m

cur.execute("""CREATE TABLE IF NOT EXISTS authors(
   author_id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS books(
   book_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   author_id INTEGER NOT NULL,
   FOREIGN KEY (author_id) REFERENCES authors(id));
""")

cur.execute("""DELETE FROM authors""")
cur.execute("""DELETE FROM books""")

cur.execute("""INSERT INTO authors(first_name, last_name) 
   VALUES('Лев', 'Толстой');
""")

cur.execute("""INSERT INTO books(name, author_id)
   VALUES('Анна Каренина', '1'), ('Война и мир', '1')
""")

con.commit()

#Связь m2m

cur.execute("""CREATE TABLE IF NOT EXISTS actors(
   actor_id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS films(
   film_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL)
   """)

cur.execute("""CREATE TABLE IF NOT EXISTS films_actors(
   films_actors_id INTEGER PRIMARY KEY,
   actor_id INTEGER NOT NULL,
   film_id INTEGER NOT NULL,
   FOREIGN KEY (actor_id) REFERENCES actors(id)
   FOREIGN KEY (film_id) REFERENCES films(id))  
""")

cur.execute("""DELETE FROM actors""")
cur.execute("""DELETE FROM films""")
cur.execute("""DELETE FROM films_actors""")

cur.execute("""INSERT INTO actors(first_name, last_name) 
   VALUES('Райан', 'Рейнольдс'), ('Дуэйн', 'Джонсон'), ('Вин', 'Дизель')
""")

cur.execute("""INSERT INTO films(name) 
   VALUES('Красное уведомление'), ('Форсаж'), ('Дедпул')
""")

cur.execute("""INSERT INTO films_actors(actor_id, film_id)
   VALUES('1', '1'), ('1', '3'), ('2', '1'), ('2', '2'), ('3', '2')
""")

con.commit()

#Join
cur.execute("""SELECT films.name, actors.first_name, actors.last_name FROM films LEFT JOIN actors ON films.film_id == actors.actor_id;""")
print(cur.fetchall())

cur.execute("""SELECT films.name, actors.first_name, actors.last_name FROM films INNER JOIN actors ON films.film_id == actors.actor_id;""")
print(cur.fetchall())

cur.execute("""SELECT * FROM films CROSS JOIN actors""")
print(cur.fetchall())

#Подзапрос с функцией

cur.execute("""SELECT name, author_id from books WHERE author_id in (SELECT id FROM authors WHERE first_name = 'Лев');""")
print(cur.fetchall())
