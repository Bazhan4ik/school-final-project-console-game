import json
import os


class Company:
    def __init__(self, name, id, income, worth, improvements, **other):
        self.name = name
        self.id = id
        self.income = income
        self.worth = worth
        self.improvements = parse_improvements(improvements)
        self.improved = other.get("improved")  # array of ids that


class Improvement:
    def __init__(self, title, research_id, income, price, id):
        self.title = title
        self.research_id = research_id
        self.income = income
        self.price = price
        self.id = id


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


def parse_improvements(improvements):
    result = []
    for i in improvements:
        result.append(
            Improvement(
                i.get("title"),
                i.get("research_id"),
                i.get("income"),
                i.get("price"),
                i.get("id"),
            )
        )
    return result
