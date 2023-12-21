from utils.companies import Company


def get_starter_pack():
    company = Company(
        name="Savor Symphony",
        id=1,
        income=0.8,
        worth=2,
        improvements=[
            {
                "title": "Improved destribution",
                "research_id": 11,
                "income": 0.5,
                "price": 0.5,
                "id": 1,
            }
        ],
    )

    return {
        "company": company,
    }
