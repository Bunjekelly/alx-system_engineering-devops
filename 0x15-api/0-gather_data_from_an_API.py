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

    tasks_completed = 0
    total_tasks = 0

    for task in tasks:
        total_tasks += 1
        if task.get("completed"):
            tasks_completed += 1

    employee_name = employee.get('name')
    title = task.get('title')

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, tasks, total_tasks))

    for task in tasks:
        if task.get("completed"):
            print("\t {}".format(title))
