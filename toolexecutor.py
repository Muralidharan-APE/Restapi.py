from dbtools import read_employee, insert_employee, delete_employee,update_employee

def execute_tool(name, args):
    if name == "read_employee":
        return read_employee()

    if name == "insert_employee":
        return insert_employee(args["title"])

    if name == "delete_employee":
        return delete_employee(args["employee_id"])

    if name == "update_employee":
        return update_employee(args["employee_id"], args["title"])