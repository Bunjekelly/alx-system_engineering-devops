#!/usr/bin/python3
"""a python script that gets data from a REST API"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    employee_url = f'http://jsonplaceholder.typicode.com/users/{user_id}'
    tasks_url = f'http://jsonplaceholder.typicode.com/todos?userId={user_id}'
    employee = requests.get(f'{employee_url}').json()
    tasks = requests.get(f'{tasks_url}').json()

    tasks_completed = []
    for task in tasks:
        if task.get("completed"):
            tasks_completed.append(task.get("title"))

    completed_count = len(tasks_completed)
    total_count = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), completed_count, total_count))
    for task in tasks_completed:
        print("\t" + task)
