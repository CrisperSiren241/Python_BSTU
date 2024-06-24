import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("ALTER TABLE student ADD COLUMN gender CHAR(1) CHECK(gender IN ('М', 'Ж'))")
conn.commit()
conn.close()
