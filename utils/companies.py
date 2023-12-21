import json
import os


class Company:
    def __init__(self, name, id, income, worth, improvements, **other):
        self.name = name
        self.id = id
        self.income = income
        self.worth = worth
        self.improvements = improvements
        self.improved = other.get("improved")  # array of ids that


def get_companies():
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/companies.txt", "r"
    )
    content = file.read()
    parsed = json.loads(content)

    file.close()

    result = []

    for company in parsed:
        result.append(
            Company(
                company.get("name"),
                company.get("id"),
                company.get("income"),
                company.get("worth"),
                company.get("improvements"),
            )
        )

    return result
