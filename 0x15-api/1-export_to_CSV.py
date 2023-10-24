#!/usr/bin/python3
"""a python script that gets data from a REST API and writes it to csv"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    api_url = 'http://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(api_url, user_id)
    tasks_url = '{}/todos?userId={}'.format(api_url, user_id)
    employee = requests.get(employee_url).json()
    tasks = requests.get(tasks_url).json()

    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, employee.get('username'),
                             task.get('completed'), task.get('title')])
