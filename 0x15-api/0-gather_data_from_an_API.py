#!/usr/bin/python3
"""this is a python script that gets data from a REST API"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    
    api_url = 'http://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(api_url, user_id)
    tasks_url = '{}/todos?userId={}'.format(api_url, user_id)
    employee = requests.get('{}'.format(employee_url)).json()
    tasks = requests.get('{}'.format(tasks_url)).json()

    tasks_completed = 0
    for task in tasks:
        if task.get("completed"):
            tasks_completed += 1
    total_count = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), tasks_completed, total_count))
    for task in tasks:
        if task.get("completed"):
            print("\t " + task.get("title"))
