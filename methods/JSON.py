import json
from tabulate import tabulate

def write_json(data):
    with open("data/users.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
    print(type(data))


def read_json():
    out = open("data/users.json")
    data = json.load(out)
    print(data)
    print(data.get(0))
    print(tabulate(data))