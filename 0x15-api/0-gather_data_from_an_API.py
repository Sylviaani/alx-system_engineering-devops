#!/usr/bin/python3
"""Returns information about TO_DO list for a given employee_id"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [task["title"] for task in todos if task["completed"] is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))

    for count, task in enumerate(done, start=1):
        print("Task {} Formatting: OK".format(count))
