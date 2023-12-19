import os
import json

companies = [
    {
        "id": 1,
        "name": "Savor Symphony",
        "income": 0.1,
        "worth": 2,
        "improvements": [
            {
                "title": "Improved destribution",
                "research_id": 11,
                "income": 0.05,
                "price": 0.5,
                "id": 1,
            }
        ],
    }
]


file = open(os.path.dirname(__file__) + "/assets/companies.txt", "w")

file.write(json.dumps(companies))
