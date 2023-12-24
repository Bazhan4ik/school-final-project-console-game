import json
import os


class Company:
    def __init__(self, name, id, income, worth, after, improvements, **other):
        self.name = name
        self.id = id
        self.income = income
        self.worth = worth
        self.after = after
        self.improvements = parse_improvements(improvements)
        if other.get("improved"):
            self.improved = other.get("improved")  # array of improvements ids
        else:
            self.improved = []

    def set_improved(self, improved):
        self.improved = improved
        # for improvement in self.improvements:
        #     if improvement.id in improved:
        #         self.improvements.remove(improvement)

    def get_available_improvements(self, completed_research):
        amount = 0
        for improvement in self.improvements:
            if improvement.id in self.improved:
                continue
            for cr in completed_research:
                if cr.id == improvement.research_id and cr.completed:
                    amount += 1
                    break

        return amount


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
                company.get("after"),
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
