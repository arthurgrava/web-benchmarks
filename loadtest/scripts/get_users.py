import json
from http import HTTPStatus

import fire
import requests


def get_total(host, index):
    url = f"{host}/{index}/_search?from=0&_source=false&size=0"
    res = requests.get(url)
    if res.status_code == HTTPStatus.OK.value:
        return res.json()["hits"]["total"]["value"]
    return 0


def get_paginated(host, index, offset, limit):
    url = f"{host}/{index}/_search?size={limit}&from={offset}"
    res = requests.get(url)
    if res.status_code == HTTPStatus.OK.value:
        return [
            ele["_source"] for ele in res.json()["hits"]["hits"]
        ]
    return []


def run(es_host, index, page_size=100):
    total = get_total(es_host, index)
    outfile, outfile_ids = "users.txt", "user_ids.txt"
    if total:
        with open(outfile, "w") as fw, open(outfile_ids, "w") as fwids:
            for i in range(0, total, page_size):
                print(f"Getting: {es_host}/{index} - from: {i} size: {page_size}")
                users = get_paginated(es_host, index, i, page_size)
                for user in users:
                    fw.write(json.dumps(user) + "\n")
                    fwids.write(user["user_id"] + "\n")
                fw.flush()
                fwids.flush()


if __name__ == "__main__":
    fire.Fire(run)
