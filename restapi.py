from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# DB connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oracle@123",
        database="dummy"
    )

# GET API - Fetch all users
@app.get("/employee")
def get_employee():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employee")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

# POST API - Add new user
@app.post("/employee")
def add_employee(name: str, age: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employee (name, age) VALUES (%s, %s)",
        (name, age)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User added successfully"}