from utils.companies import get_companies
from utils.research import get_research
from utils.tracker import get_progress


class Game:
    def __init__(self):
        # company has improvements and improved
        # improvements is what has not been purchased yet
        # improved is something that has already been purchased
        self.companies = get_companies()
        self.research = get_research()

        self.progress = get_progress(self.companies, self.research)
