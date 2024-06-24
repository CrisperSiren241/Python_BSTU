import sqlite3 
from tabulate import tabulate 
 
conn = sqlite3.connect('students.db') 
cursor = conn.cursor() 
 
cursor.execute('''SELECT * FROM student where gender ="Ж"''')

results = cursor.fetchall() 
 
table_headers = [i[0] for i in cursor.description] 
print(tabulate(results, headers=table_headers, tablefmt='grid')) 
 
conn.close()