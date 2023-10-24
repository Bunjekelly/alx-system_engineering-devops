#!/usr/bin/python3
"""this is a python script that gets data from a REST API"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    employee_url = 'http://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    tasks_url = 'http://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    employee = requests.get('{}'.format(employee_url)).json()
    tasks = requests.get('{}'.format(tasks_url)).json()

    tasks_completed = []
    for task in tasks:
        if task.get("completed"):
            tasks_completed.append(task.get("title"))

    completed_count = len(tasks_completed)
    total_count = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), completed_count, total_count))
    for task in tasks_completed:
        print("\t" + " " + task)
