import json

import fire
import requests


def create_random_user(api):
    url = f"{api}/v1/users/put-random-user"
    requests.get(url)


def create_user_from_dict(api, user):
    print(f"Putting {user}")
    url = f"{api}/v1/users"
    requests.put(url, json=user)


def read_users(filename):
    data = []
    with open(filename, 'r') as rr:
        for line in rr:
            data.append(json.loads(line.strip()))
    return data


def run(api, random=False, datafile="", amount=10):
    print(f"Config: {api} - {random} - {datafile} - {amount}")
    if datafile:
        users = read_users(datafile)
        for user in users:
            create_user_from_dict(api, user)
    elif random:
        for _ in range(amount):
            create_random_user(api)
    else:
        print((
            "--random --amount {amount}\nor\n"
            "--datafile {file}"
        ))


if __name__ == "__main__":
    fire.Fire(run)
