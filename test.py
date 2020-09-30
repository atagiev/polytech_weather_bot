import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()  

cursor.execute("SELECT * FROM users")
for i in cursor.fetchall():
    print(i)