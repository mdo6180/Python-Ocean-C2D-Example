import json
import os
import sys


def line_counter(path):
    with open(path, "r") as file:
        data = json.load(file)
        print(len(data))


if __name__ == "__main__":
    print(f"counting up number of rows in {sys.argv[1]}")
    path = sys.argv[1]
    line_counter(path)

