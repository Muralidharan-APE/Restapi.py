import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Oracle@123",
    database="dummy"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()