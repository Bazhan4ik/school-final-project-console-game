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
            },
            {
                "title": "Advanced destribution",
                "research_id": 12,
                "income": 0.1,
                "price": 1,
                "id": 2,
            },
        ],
    },
    {
        "id": 2,
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


# research = [
#     {"id": 11, "name": "Distribution Strategies", "price": 0.5, "duration": 3},
#     {
#         "id": 12,
#         "after": 11,
#         "name": "Advanced Distribution Strategies",
#         "price": 0.5,
#         "duration": 5,
#     },
# ]


# file = open(os.path.dirname(__file__) + "/assets/research.txt", "w")

# file.write(json.dumps(research))
