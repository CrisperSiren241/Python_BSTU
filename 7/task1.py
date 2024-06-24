# Создайте базу данных SQLite3 с помощью модуля sqlite3.
# Создайте таблицу student в базе данных с несколькими столбцами|: "id", "name", "date of birth", "faculty", "course", "group ".
# Вставьте несколько записей в таблицу, используя оператор INSERT INTO.
# Сохраните изменения в базе данных и закройте соединение.

import sqlite3

conn = sqlite3.connect('students.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE student (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         date_of_birth TEXT,
#         faculty TEXT,
#         course INTEGER,
#         group_ INTEGER
#     )
# ''')

students = [
    (4, 'Геско Мария Дмитриевна', '2003-07-09', 'ФИТ', 3, 9),
    (5, 'Пальчастая Анна Николаевна', '2003-03-03', 'ПИМ', 4, 10),
    (6, 'Подоксенова Лина Сергеевна', '2004-10-27', 'ХТИТ', 2, 2),
]
cursor.executemany('''
    INSERT INTO student (id, name, date_of_birth, faculty, course, group_) 
                   VALUES (?, ?, ?, ?, ?, ?)
''', students)

conn.commit()
conn.close()
