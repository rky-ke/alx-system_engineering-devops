#!/usr/bin/python3
"""
Python script that, using this REST API, 
for a given employee ID, returns information 
about his/her TODO list progress
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    # Make API requests
    todo_response = requests.get(todo_url)
    name_response = requests.get(name_url)

    # Check if requests were successful
    if todo_response.ok and name_response.ok:
        todo_result = todo_response.json()
        name_result = name_response.json()

        todo_num = len(todo_result)
        todo_complete = len([todo for todo in todo_result if todo.get("completed")])
        name = name_result.get("name")

        # Display employee TODO list progress
        print(f"Employee {name} is done with tasks({todo_complete}/{todo_num}):")
        for todo in todo_result:
            if todo.get("completed"):
                print(f"\t {todo.get('title')}")
    else:
        # Print an error message if the request was not successful
        print("Error: Unable to retrieve data from the API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)


