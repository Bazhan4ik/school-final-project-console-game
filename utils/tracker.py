import os
import json


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


def get_progress(companies, research):
    file = open(
        os.path.dirname(os.path.dirname(__file__)) + "/assets/progress.txt", "r"
    )

    content = file.read()

    if len(content) == 0:
        return {
            "companies": [],
            "research": [],
            "balance": 0,
        }

    parsed = json.loads(content)

    saved_companies = filter_companies(companies, parsed.get("companies"))
    saved_research = filter_research(research, parsed.get("research"))

    print(saved_companies)

    return {
        "companies": saved_companies,
        "research": saved_research,
        "balance": parsed.get("balance"),
    }
