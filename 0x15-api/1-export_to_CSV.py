#!/usr/bin/python3
"""
Python script that, using this REST API, 
for a given employee ID, returns information 
about his/her TODO list progress and exports the data in CSV format.
"""
import requests
import csv
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

        name = name_result.get("username")
        user_id = name_result.get("id")

        # Display employee TODO list progress
        print(f"Employee {name} is done with tasks:")
        
        # Export data to CSV
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Write header
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write data rows
            for todo in todo_result:
                task_completed_status = "Completed" if todo.get("completed") else "Not Completed"
                task_title = todo.get("title")
                csv_writer.writerow([user_id, name, task_completed_status, task_title])
                # Print task details on console
                print(f"    Task Completed: {task_completed_status}\tTask Title: {task_title}")

        print(f"CSV file '{csv_filename}' has been created with the TODO list data.")
    else:
        # Print an error message if the request was not successful
        print("Error: Unable to retrieve data from the API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
