import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from toolexecutor import execute_tool

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
tools = [
    {
        "type": "function",
        "function": {
            "name": "read_employee",
            "description": "Read all employee",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "insert_employee",
            "description": "Insert a new employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"}
                },
                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_employee",
            "description": "Delete a employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"}
                },
                "required": ["employee_id"]
            }
        }
    }
]

def chat(user_message):
    messages = [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        result = execute_tool(name, args)

        print("Tool:", name)
        print("Result:", result)
    else:
        print(msg.content)

chat("load  Lakisha as employee") #insert
chat("Show all employee") #select