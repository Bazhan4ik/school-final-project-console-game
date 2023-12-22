import json
import os


def get_research():
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/research.txt", "r"
    )
    content = file.read()
    parsed = json.loads(content)

    file.close()

    result = []
    for research in parsed:
        result.append(
            Research(
                research.get("name"),
                research.get("id"),
                research.get("price"),
                research.get("duration"),
                research.get("after"),
            )
        )

    return result


class Research:
    def __init__(self, name, id, price, duration, after, **other):
        self.name = name
        self.id = id
        self.price = price
        self.duration = duration
        self.after = after
        self.completed = False

        if other.get("finish_by"):
            self.finish_by = other.get("finish_by")
        if other.get("completed"):
            self.completed = other.get("completed")
