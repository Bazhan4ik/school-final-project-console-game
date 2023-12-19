import json
import os


def get_research():
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/research.txt", "r"
    )
    content = file.read()
    parsed = json.loads(content)

    file.close()

    return parsed


# research = [
#     {
#         "id": 11,
#         "name": "Distribution Strategies",
#         "price": 0.5,
#     },
#     {
#         "id": 11,
#         "name": "Advanced Distribution Strategies",
#         "price": 0.5,
#     },
# ]


# file = open(os.path.dirname(os.path.dirname(__file__)) + "/assets/research.txt", "w")

# file.write(json.dumps(research))
