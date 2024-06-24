# Подключитесь к существующей базе данных SQLite3.
# Используя оператор DELETE, удалите определенные записи из таблицы: 
# всех студентом младше 2000 года рождения
# всех студентов 2 курса 5 группы 
# Сохраните изменения в базе данных и закройте соединение.


import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM student WHERE date_of_birth > '2000-12-31'")
cursor.execute("DELETE FROM student WHERE course = 2 AND group_ = 5")
conn.commit()
conn.close()
