import json
import os
import sys


def line_counter(path):
    with open(path, "r") as file:
        data = json.load(file)
        line_count = len(data)
        return line_count


if __name__ == "__main__":
    print(f"counting up number of rows in {sys.argv[1]}")
    path = sys.argv[1]

    result = line_counter(path)
    output = {"line_counter_result":result}

    # Serializing json 
    json_object = json.dumps(output, indent = 4)
    with open("output.json", "w") as outfile:
        outfile.write(json_object)
