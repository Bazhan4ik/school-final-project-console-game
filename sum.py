import os
import json

companies = [
    {
        "id": 1,
        "name": "Savor Symphony",
        "income": 0.4,
        "worth": 2,
        "improvements": [
            {
                "title": "Improved destribution",
                "research_id": 11,
                "income": 0.1,
                "price": 1,
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
    },
    {
        "id": 2,
        "name": "CraftByte",
        "income": 2,
        "worth": 5,
        "after": 21,
        "improvements": [
            {
                "title": "AI Coding Companions",
                "research_id": 22,
                "income": 0.5,
                "price": 3,
                "id": 1,
            },
            {
                "title": "Neural Affecting Energizers for Staff",
                "research_id": 23,
                "income": 0.2,
                "price": 4,
                "id": 2,
            },
            {
                "title": "Next-Gen Large Language Models",
                "research_id": 24,
                "income": 1,
                "price": 13,
                "id": 3,
            },
        ],
    },
    {
        "id": 3,
        "name": "GeneGenius Biotech",
        "income": 1.3,
        "worth": 22,
        "after": 30,
        "improvements": [
            {
                "title": "Designer Gene Therapies",
                "research_id": 31,
                "income": 0.7,
                "price": 1,
                "id": 1,
            },
            {
                "title": "Neural Affecting Energizers for Staff",
                "research_id": 23,
                "income": 0.5,
                "price": 8,
                "id": 2,
            },
            {
                "title": "Quantum-Enhanced Drug Design",
                "research_id": 33,
                "income": 1.5,
                "price": 8,
                "id": 3,
            },
            {
                "title": "AI-Assisted Cognitive Enhancement",
                "research_id": 34,
                "income": 1.5,
                "price": 20,
                "id": 4,
            },
            {
                "title": "Prosthetic Limbs with Sensory Feedback",
                "research_id": 35,
                "income": 1.5,
                "price": 23,
                "id": 5,
            },
        ],
    },
    {
        "id": 4,
        "name": "EcoSynth Solutions",
        "income": 0.5,
        "worth": 18,
        "after": 30,
        "improvements": [
            {
                "title": "Eco-Friendly Carbon Filters",
                "research_id": 32,
                "income": 1.5,
                "price": 8,
                "id": 1,
            }
        ],
    },
    {
        "id": 5,
        "name": "QuantumLeap Computing",
        "income": 8,
        "worth": 100,
        "after": 40,
        "improvements": [
            {
                "title": "Unhackable Quantum Networks",
                "research_id": 41,
                "income": 2,
                "price": 25,
                "id": 1,
            },
            {
                "title": "AI-Quantum Hybrid Systems",
                "research_id": 42,
                "income": 4,
                "price": 70,
                "id": 2,
            },
            {
                "title": "Next-Gen Quantum Processors",
                "research_id": 43,
                "income": 10,
                "price": 90,
                "id": 3,
            },
        ],
    },
    {
        "id": 6,
        "name": "SkyBound Aerospace",
        "income": 8,
        "worth": 300,
        "after": 40,
        "improvements": [
            {
                "title": "Unhackable Quantum Networks",
                "research_id": 41,
                "income": 2,
                "price": 25,
                "id": 1,
            },
        ],
    },
]


file = open(os.path.dirname(__file__) + "/assets/companies.txt", "w")

file.write(json.dumps(companies))

# 2.* - software engineering
# 3.* - biotech
# 4.* - quantum computing
research = [
    {"id": 11, "name": "Advanced Cooking Strategies", "price": 1, "duration": 3},
    {
        "id": 21,
        "after": 11,
        "name": "Software Engineering",
        "price": 0.5,
        "duration": 1,
    },
    {
        "id": 22,
        "after": 21,
        "name": "AI Code Generation",
        "price": 1.5,
        "duration": 4,
    },
    {"id": 23, "after": 31, "name": "ENERGY FOR STAFF", "price": 5, "duration": 10},
    {
        "id": 24,
        "after": 22,
        "name": "Advanced Machine Learning",
        "price": 10,
        "duration": 14,
    },
    {
        "id": 25,
        "after": 40,
        "name": "Hardware Innovations",
        "price": 20,
        "duration": 14,
    },
    #
    # Bio
    #
    {
        "id": 30,
        "after": 21,
        "name": "Bio Technology",
        "price": 3,
        "duration": 6,
    },
    {
        "id": 31,
        "after": 30,
        "name": "CRISPR Gene Editing",
        "price": 4,
        "duration": 5,
    },
    {
        "id": 32,
        "after": 30,
        "name": "Carbon Capture Algorithms",
        "price": 1,
        "duration": 2,
    },
    {
        "id": 33,
        "after": 40,
        "name": "Quantum Biology Exploration",
        "price": 60,
        "duration": 20,
    },
    {
        "id": 34,
        "after": 24,
        "name": "Artificial Intelligence Symbiosis",
        "price": 30,
        "duration": 14,
    },
    {
        "id": 35,
        "after": 25,
        "name": "Biomechatronics Development",
        "price": 28,
        "duration": 14,
    },
    #
    # Quantum
    #
    {
        "id": 40,
        "after": 21,
        "name": "Quantum Computing Technology",
        "price": 60,
        "duration": 20,
    },
    {
        "id": 41,
        "after": 40,
        "name": "Quantum Encryption Methods",
        "price": 70,
        "duration": 20,
    },
    {
        "id": 42,
        "after": 24,
        "name": "Quantum Machine Learning Integration",
        "price": 100,
        "duration": 20,
    },
    {
        "id": 43,
        "after": 25,
        "name": "Quantum Hardware Innovations",
        "price": 100,
        "duration": 14,
    },
    #
    # Space
    #
    {
        "id": 50,
        "after": 25,
        "name": "Rocket Science",
        "price": 100,
        "duration": 28,
    },
]


file = open(os.path.dirname(__file__) + "/assets/research.txt", "w")

file.write(json.dumps(research))
