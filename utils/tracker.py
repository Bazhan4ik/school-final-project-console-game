import os
import json
from utils.default import get_starter_pack


def filter_research(arr, ids):
    filtered = []
    for el in arr:
        if el.get("id") in ids:
            filtered.append(el)
    return filtered


def filter_improvements(available, purchased):
    result = []
    for i in available:
        if i.get("id") in purchased:
            result.append(available)
    return result


def filter_companies(companies, arr):
    filtered = []
    for comp in arr:
        id = comp.get("id")
        improved = comp.get("improved")
        for company in companies:
            if company.get("id") == id:
                company["improved"] = filter_improvements(
                    company.get("improvements"), improved
                )
                filtered.append(company)
    return filtered


def calculate_income(companies):
    income = 0
    for company in companies:
        improvements_income = 0

        if company.improved:
            for improvement in company.improvements:
                if improvement.id in company.improved:
                    improvements_income += improvement.income

        company.income += improvements_income
        income += company.income

    return income


def get_progress(companies, research):
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/progress.txt", "r"
    )

    content = file.read()

    if len(content) == 0:
        starter = get_starter_pack()
        return Progress([starter.get("company")], [], balance=0, months=0)

    parsed = json.loads(content)

    saved_companies = filter_companies(companies, parsed.get("companies"))
    saved_research = filter_research(research, parsed.get("research"))

    return Progress(
        saved_companies,
        saved_research,
        balance=parsed.get("balance"),
        days=parsed.get("months"),
    )


class Progress:
    def __init__(self, companies, research, balance, months):
        self.companies = companies
        self.research = research
        self.balance = balance
        self.months = months

        self.income = calculate_income(companies)

    def save(self):
        return

    def currently_researching(self):
        result = []
        for research in self.research:
            if not research.completed:
                result.append(research)

        return result
