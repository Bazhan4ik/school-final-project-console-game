import os
import json

companies = [
    {
        "id": 1,
        "name": "Savor Symphony",
        "income": 0.8,
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
    },
    {
        "id": 1,
        "name": "BioTeCh",
        "income": 3,
        "worth": 10,
        "improvements": [
            {
                "title": "Some improvement",
                "research_id": 11,
                "income": 0.05,
                "price": 0.5,
                "id": 1,
            }
        ],
    },
]


file = open(os.path.dirname(__file__) + "/assets/companies.txt", "w")

file.write(json.dumps(companies))
