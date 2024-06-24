# Подключитесь к существующей базе данных SQLite3.
# Используя оператор UPDATE, обновите данные в таблице.
# Например, можно изменить курс определенной записи или изменить группу.
# Сохраните изменения в базе данных и закройте соединение.


import sqlite3

conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute('UPDATE student SET gender = "Ж" WHERE id = 6')

conn.commit()
conn.close()
