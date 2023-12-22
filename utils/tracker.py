import os
import json
from utils.default import get_starter_pack


# research is an array of Research objects
# arr is an array of dictionaries like Research
def filter_research(research, arr):
    filtered = []
    for el in arr:
        for r in research:
            if el.get("id") == r.id:
                if el.get("completed"):
                    r.completed = True
                elif el.get("finish_by"):
                    r.completed = False
                    r.finish_by = el.get("finish_by")
                filtered.append(r)

    return filtered


def filter_improvements(available, purchased):
    result = []
    for i in available:
        if i.id in purchased:
            result.append(available)
    return result


# companies are Company object
# arr are dictionaries
def filter_companies(companies, arr):
    filtered = []
    for comp in arr:
        # comp is a dictionary
        id = comp.get("id")
        improved = comp.get("improved")
        for company in companies:
            # company is Company object
            if company.id == id:
                if improved:
                    company["improved"] = filter_improvements(
                        company.improvements, improved
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
        months=parsed.get("months"),
    )


class Progress:
    def __init__(self, companies, research, balance, months):
        self.companies = companies
        self.research = research
        self.balance = balance
        self.months = months

        self.income = calculate_income(companies)

    def save(self):
        file = open(
            os.path.dirname(os.path.dirname(__file__)) + "/assets/progress.txt", "w"
        )

        def c(obj):
            dict = obj.__dict__
            if hasattr(obj, "improvements"):
                dict["improvements"] = list(map(c, obj.improvements))
            return dict

        new_content = json.dumps(
            {
                "companies": list(map(c, self.companies)),
                "research": list(map(c, self.research)),
                "balance": self.balance,
                "months": self.months,
            }
        )

        file.write(new_content)
        file.close()

        return

    def currently_researching(self):
        result = []
        for research in self.research:
            if not research.completed:
                result.append(research)

        return result
