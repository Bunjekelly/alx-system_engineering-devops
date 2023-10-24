#!/usr/bin/python3
"""a python script that gets data from a REST API and
writes it to json for all employees"""

import json
import requests
import sys

if __name__ == '__main__':

    api_url = 'http://jsonplaceholder.typicode.com'
    employees_url = '{}/users/'.format(api_url)
    employees = requests.get(employees_url).json()

    data = {}
    for user in employees:
        user_id = user.get('id')
        tasks_url = '{}/todos?userId={}'.format(api_url, user_id)
        tasks = requests.get(tasks_url).json()
        data[user_id] = []
        for task in tasks:
            data[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
