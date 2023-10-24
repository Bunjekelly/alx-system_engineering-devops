#!/usr/bin/python3
"""a python script that gets data from a REST API and writes it to json"""

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    api_url = 'http://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(api_url, user_id)
    tasks_url = '{}/todos?userId={}'.format(api_url, user_id)
    employee = requests.get(employee_url).json()
    tasks = requests.get(tasks_url).json()

    data = {user_id: []}
    for task in tasks:
        data[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee.get('username')
        })

    with open(f'{user_id}.json', 'w') as file:
        json.dump(data, file)
