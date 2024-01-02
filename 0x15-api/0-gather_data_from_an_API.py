#!/usr/bin/python3
"""Returns information about TO_DO list for a given employee_id"""

import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [task["title"] for task in todos if task("completed") is True]

    print("Employee {} is done with tasks({len(done)}/{len(todos)}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t{task}")
