import json
import os


def get_companies():
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/companies.txt", "r"
    )
    content = file.read()
    parsed = json.loads(content)

    file.close()

    return parsed
