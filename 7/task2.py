# Подключитесь к существующей базе данных SQLite3.
# Используя оператор SELECT, выполните запрос к таблице и получите все записи.
# Выведите полученные данные на экран.


import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM student where date_of_birth like "%-06-%"')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
