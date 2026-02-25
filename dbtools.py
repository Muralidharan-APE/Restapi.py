import mysql.connector

def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oracle@123",
        database="dummy"
    )

def read_employee():
    c = conn()
    cur = c.cursor(dictionary=True)
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    cur.close()
    c.close()
    return rows

def insert_employee(title):
    c = conn()
    cur = c.cursor()
    cur.execute("INSERT INTO employee(title) VALUES(%s)", (title,))
    c.commit()
    cur.close()
    c.close()
    return {"status": "inserted"}

def delete_employee(employee_id):
    c = conn()
    cur = c.cursor()
    cur.execute("DELETE FROM employee WHERE id=%s", (employee_id,))
    c.commit()
    cur.close()
    c.close()
    return {"status": "deleted"}

def update_employee(employee_id, title):
    c = conn()
    cur = c.cursor()
    cur.execute(
        "UPDATE tasks SET title=%s WHERE id=%s",
        (title, employee_id)
    )
    c.commit()
    cur.close()
    c.close()
    return {"status": "updated"}