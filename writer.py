import os
import json

companies = [
    {
        "id": 1,
        "name": "Savor Symphony",
        "income": 0.4,
        "worth": 4,
        "improvements": [
            {
                "title": "Delivery OptionS",
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
        "income": 0.5,
        "worth": 5,
        "after": 21,
        "improvements": [
            {
                "title": "AI Coding Companions",
                "research_id": 22,
                "income": 0.3,
                "price": 5,
                "id": 1,
            },
            {
                "title": "Neural Affecting Energizers for Staff",
                "research_id": 23,
                "income": 0.1,
                "price": 4,
                "id": 2,
            },
            {
                "title": "Next-Gen Large Language Models",
                "research_id": 24,
                "income": 0.7,
                "price": 20,
                "id": 3,
            },
            {
                "title": "Development of AI Humans",
                "research_id": 26,
                "income": 50,
                "price": 2000,
                "id": 4,
            },
            {
                "title": "Development of Global Human Brain",
                "research_id": 78,
                "income": 300,
                "price": 20000,
                "id": 5,
            },
        ],
    },
    {
        "id": 3,
        "name": "GeneGenius Biotech",
        "income": 0.9,
        "worth": 22,
        "after": 30,
        "improvements": [
            {
                "title": "Designer Gene Therapies",
                "research_id": 31,
                "income": 0.7,
                "price": 40,
                "id": 1,
            },
            {
                "title": "Neural Affecting Energizers for Staff",
                "research_id": 23,
                "income": 0.1,
                "price": 10,
                "id": 2,
            },
            {
                "title": "Quantum-Enhanced Drug Design",
                "research_id": 33,
                "income": 1.5,
                "price": 60,
                "id": 3,
            },
            {
                "title": "AI-Assisted Cognitive Enhancement",
                "research_id": 34,
                "income": 1.5,
                "price": 120,
                "id": 4,
            },
            {
                "title": "Prosthetic Limbs with Sensory Feedback",
                "research_id": 35,
                "income": 1.5,
                "price": 100,
                "id": 5,
            },
        ],
    },
    {
        "id": 4,
        "name": "EcoSynth Solutions",
        "income": 0.4,
        "worth": 18,
        "after": 30,
        "improvements": [
            {
                "title": "Eco-Friendly Carbon Filters",
                "research_id": 32,
                "income": 0.3,
                "price": 8,
                "id": 1,
            },
            {
                "title": "Precise Weather Forecasting",
                "research_id": 301,
                "income": 1,
                "price": 100,
                "id": 2,
            },
            {
                "title": "Weather Control",
                "research_id": 301,
                "income": 40,
                "price": 1500,
                "id": 3,
            },
            {
                "title": "Atmosphere Improvement",
                "research_id": 303,
                "income": 200,
                "price": 10000,
                "id": 4,
            },
        ],
    },
    {
        "id": 5,
        "name": "QuantumLeap Computing",
        "income": 8,
        "worth": 300,
        "after": 40,
        "improvements": [
            {
                "title": "Unhackable Quantum Networks",
                "research_id": 41,
                "income": 2,
                "price": 104,
                "id": 1,
            },
            {
                "title": "AI-Quantum Hybrid Systems",
                "research_id": 42,
                "income": 4,
                "price": 250,
                "id": 2,
            },
            {
                "title": "Quantum Machine Learning Services",
                "research_id": 42,
                "income": 50,
                "price": 4000,
                "id": 20,
            },
            {
                "title": "Next-Gen Quantum Processors",
                "research_id": 43,
                "income": 10,
                "price": 400,
                "id": 3,
            },
            {
                "title": "Quantum Servers",
                "research_id": 43,
                "income": 20,
                "price": 1000,
                "id": 4,
            },
            {
                "title": "More Quantum Servers",
                "research_id": 43,
                "income": 20,
                "price": 1000,
                "id": 5,
            },
            {
                "title": "Quantum Simulations",
                "research_id": 44,
                "income": 120,
                "price": 2810,
                "id": 6,
            },
        ],
    },
    {
        "id": 6,
        "name": "NanoCraft Labs",
        "income": 8,
        "worth": 300,
        "after": 25,
        "improvements": [
            {
                "title": "Precision Nanobots",
                "research_id": 50,
                "income": 3.1,
                "price": 300,
                "id": 1,
            },
            {
                "title": "Efficient Drug Delivery Using Nano-bots",
                "research_id": 51,
                "income": 2.4,
                "price": 210,
                "id": 2,
            },
            {
                "title": "Ultra-Precision Nanobots",
                "research_id": 52,
                "income": 4,
                "price": 400,
                "id": 3,
            },
            {
                "title": "Implementation of Nano-Robotic Immune System",
                "research_id": 53,
                "income": 12,
                "price": 1200,
                "id": 4,
            },
            {
                "title": "Cyborg Humans",
                "research_id": 53,
                "income": 110,
                "price": 10000,
                "id": 5,
            },
        ],
    },
    {
        "id": 7,
        "name": "SkyBound Aerospace",
        "income": 8,
        "worth": 600,
        "after": 50,
        "improvements": [
            {
                "title": "Cost-Effective Space Missions",
                "research_id": 60,
                "income": 30,
                "price": 1000,
                "id": 1,
            },
            {
                "title": "Precision Interstellar Pathfinding",
                "research_id": 61,
                "income": 31,
                "price": 1200,
                "id": 2,
            },
            {
                "title": "Orbital Resource Harvesters",
                "research_id": 62,
                "income": 50,
                "price": 1800,
                "id": 3,
            },
            {
                "title": "Next-Get Internet Communication from Space",
                "research_id": 63,
                "income": 50,
                "price": 4000,
                "id": 3,
            },
            {
                "title": "Deplayment of AI Astronauts to Space",
                "research_id": 64,
                "income": 80,
                "price": 8000,
                "id": 4,
            },
            {
                "title": "AI Miners, More Natural Resources",
                "research_id": 64,
                "income": 160,
                "price": 10000,
                "id": 5,
            },
            {
                "title": "Creating Atmosphere on Planets",
                "research_id": 303,
                "income": 300,
                "price": 20000,
                "id": 6,
            },
        ],
    },
    {
        "id": 8,
        "name": "FacePhone Social",
        "income": 0.5,
        "worth": 20,
        "after": 70,
        "improvements": [
            {
                "title": "Pleasing UX/UI Design",  # Even a slightest misplace of some button on the interface can make a drastic difference.
                "research_id": 71,  # Easy to navigate interface is VERY important
                "income": 0.4,
                "price": 30,
                "id": 1,
            },
            {
                "title": "SmartFeed Algorithm",  # Revenue is ads. Users don't like ads. To keep the user on the platform, watching ads, they have to be provided good content
                "research_id": 72,  # The personalized feed is what made most of the social media platforms so powerful and rich
                "income": 1,
                "price": 100,
                "id": 2,
            },
            {
                "title": "Insightful Audience Engagement",
                "research_id": 73,
                "income": 1.2,
                "price": 220,
                "id": 3,
            },
            {
                "title": "Precision Ad Platform",  # Ads are the most valuable thing a social modia platform provides
                "research_id": 74,  # The better the conversion of an ad, the more revenue the platform will get, meaning the ad precision is very good investment for a social media company
                "income": 3,
                "price": 460,
                "id": 4,
            },
            {
                "title": "EngagePlay Features",
                "research_id": 75,
                "income": 2.8,
                "price": 300,
                "id": 5,
            },
            {
                "title": "SafeSpace Monitoring",  # Content moderation is cheap, but it will bring more people and more advertizers
                "research_id": 76,  # For example, Twitter, after Elon Musk took over, the moderation of the content drastically went down, leading to more than half of revenue loss
                "income": 5,
                "price": 200,
                "id": 6,
            },
            {
                "title": "Internationalization",
                "research_id": 78,
                "income": 60,
                "price": 1000,
                "id": 7,
            },
            {
                "title": "International Advertizing",
                "research_id": 78,
                "income": 60,
                "price": 5000,
                "id": 8,
            },
            {
                "title": "Interplanetary Social Media",
                "research_id": 78,
                "income": 100,
                "price": 8300,
                "id": 9,
            },
            {
                "title": "Implementation of VR/AR",
                "research_id": 79,
                "income": 300,
                "price": 20000,
                "id": 10,
            },
        ],
    },
]


file = open(os.path.dirname(__file__) + "/assets/companies.txt", "w")

file.write(json.dumps(companies))

file.close()

# 2.* - software engineering
# 3.* - biotech
# 4.* - quantum computing
# 5.* - nano technology
# 6.* - space
# 7.* - social media
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
        "price": 6,
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
    {
        "id": 26,
        "after": 52,
        "name": "AI Human",
        "price": 1200,
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
        "price": 10,
        "duration": 2,
    },
    {
        "id": 301,
        "after": 32,
        "name": "99.999% Weather Forecast",
        "price": 20,
        "duration": 4,
    },
    {
        "id": 302,
        "after": 301,
        "name": "Weather Control",
        "price": 400,
        "duration": 12,
    },
    {
        "id": 303,
        "after": 302,
        "name": "Atmosphere Creation",
        "price": 600,
        "duration": 12,
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
        "price": 88,
        "duration": 14,
    },
    {
        "id": 36,
        "after": 35,
        "name": "Implementation of AI in Human Brain",
        "price": 1000,
        "duration": 14,
    },
    #
    # Quantum
    #
    {
        "id": 40,
        "after": 21,
        "name": "Quantum Computing Technology",
        "price": 100,
        "duration": 20,
    },
    {
        "id": 41,
        "after": 40,
        "name": "Quantum Encryption Methods",
        "price": 120,
        "duration": 8,
    },
    {
        "id": 42,
        "after": 24,
        "name": "Quantum Machine Learning Integration",
        "price": 300,
        "duration": 13,
    },
    {
        "id": 43,
        "after": 25,
        "name": "Quantum Hardware Innovations",
        "price": 280,
        "duration": 14,
    },
    {
        "id": 44,
        "after": 43,
        "name": "Hyper-Realistic Quantum Simulator",
        "price": 900,
        "duration": 11,
    },
    #
    # Nano
    #
    {
        "id": 50,
        "after": 25,
        "name": "Molecular Assembly Techniques",
        "price": 100,
        "duration": 8,
    },
    {
        "id": 51,
        "after": 50,
        "name": "Nanoparticle Drug Delivery",
        "price": 165,
        "duration": 12,
    },
    {
        "id": 52,
        "after": 51,
        "name": "Nano-Robotics Control Systems",
        "price": 120,
        "duration": 6,
    },
    {
        "id": 53,
        "after": 52,
        "name": "Nano-Robotics Human Care",
        "price": 400,
        "duration": 8,
    },
    #
    # Space
    #
    {
        "id": 60,
        "after": 25,
        "name": "Reusable Rocket Designs",
        "price": 1000,
        "duration": 28,
    },
    {
        "id": 61,
        "after": 60,
        "name": "Quantum Navigation Algorithms",
        "price": 800,
        "duration": 8,
    },
    {
        "id": 62,
        "after": 61,
        "name": "Asteroid Mining Technologies",
        "price": 800,
        "duration": 8,
    },
    {
        "id": 63,
        "after": 61,
        "name": "Fast Space-Earth Communication Systems",
        "price": 800,
        "duration": 8,
    },
    {
        "id": 64,
        "after": 26,
        "name": "Very Capable AI Astronauts",
        "price": 800,
        "duration": 4,
    },
    #
    # Social Media
    #
    {"id": 70, "after": 21, "name": "Social Media Idea", "price": 1, "duration": 1},
    {"id": 71, "after": 70, "name": "Advanced UX Designing", "price": 1, "duration": 2},
    {
        "id": 72,
        "after": 24,
        "name": "AI-Driven Content Personalization",
        "price": 40,
        "duration": 5,
    },
    {
        "id": 73,
        "after": 72,
        "name": "Advanced Behavioral Analytics",
        "price": 80,
        "duration": 7,
    },
    {
        "id": 74,
        "after": 73,
        "name": "Next-Gen Ad Targeting Techniques",
        "price": 91,
        "duration": 5,
    },
    {
        "id": 75,
        "after": 73,
        "name": "Gamification of Social Interactions",
        "price": 20,
        "duration": 2,
    },
    {
        "id": 76,
        "after": 73,
        "name": "Innovative Content Moderation Systems",
        "price": 20,
        "duration": 4,
    },
    {
        "id": 77,
        "after": 76,
        "name": "Advanced User Engagement Strategies",
        "price": 100,
        "duration": 12,
    },
    {
        "id": 78,
        "after": 77,
        "name": "Internationalization",
        "price": 100,
        "duration": 4,
    },
    {
        "id": 79,
        "after": 78,
        "name": "Quick Virtual Reality Large-Usership Protocols",
        "price": 300,
        "duration": 6,
    },
]


file = open(os.path.dirname(__file__) + "/assets/research.txt", "w")

file.write(json.dumps(research))

file.close()
