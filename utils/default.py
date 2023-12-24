from utils.companies import Company


def get_starter_pack():
    company = Company(
        name="Savor Symphony",
        id=1,
        income=0.4,
        worth=2,
        after=0,
        improvements=[
            {
                "title": "Improved destribution",
                "research_id": 11,
                "income": 0.1,
                "price": 0.5,
                "id": 1,
            },
            {
                "title": "Neural Affecting Energizers for Staff",
                "research_id": 23,
                "income": 0.1,
                "price": 3,
                "id": 2,
            },
        ],
    )

    return {
        "company": company,
    }
