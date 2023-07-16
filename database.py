import sqlite3

"""
Operates on the codewise database
"""

connection = sqlite3.connect('codewise.db')
cursor = connection.cursor()
#cursor.execute('''CREATE TABLE lecturers(id INTEGER PRIMARY KEY,name TEXT,class TEXT)''')
#COMMITING CHANGES
#connection.commit()

cursor.execute("INSERT INTO lecturers (name,class) VALUES ('Jackson','cohort10')")
connection.commit()

cursor.execute("SELECT * FROM lecturers")
rows = cursor.fetchall()
for row in rows:
    print(row)

