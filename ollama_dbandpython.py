import requests
from Ollama_dbconnect import get_connection

def chat(prompt):
    system_prompt = """
You are a database assistant.

Rules:
If user wants to see all employees, reply exactly:
SHOW_EMPLOYEE

If user wants to add an employee, reply exactly:
ACTION:INSERT_EMPLOYEE:<name>

Otherwise reply normally.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": system_prompt + "\nUser: " + prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def read_employee():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def insert_employee(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employee (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return "Employee inserted"


if __name__ == "__main__":
    user_input = input("You: ")
    ai_reply = chat(user_input)

    if "SHOW_EMPLOYEE" in ai_reply:
        data = read_employee()
        print("DB Result:", data)

    elif "ACTION:INSERT_EMPLOYEE:" in ai_reply:
        name = ai_reply.split(":")[2].strip()
        print(insert_employee(name))

    else:
        print("AI:", ai_reply)