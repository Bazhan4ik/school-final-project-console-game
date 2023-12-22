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

        self.available_research = self.research
        self.available_companies = self.companies

        self.progress = get_progress(self.companies, self.research)

        self.filter_companies()
        self.filter_research()

    def moveon(self):
        self.progress.balance += self.progress.income
        self.progress.months += 1
        self.progress.balance = round(self.progress.balance, 3)

        for research in self.progress.research:
            if research.completed:
                continue
            if research.finish_by == self.progress.months:
                research.completed = True

        self.progress.save()

    def filter_companies(self):
        for purchased_company in self.progress.companies:
            for company in self.available_companies:
                if purchased_company.id == company.id:
                    self.available_companies.remove(company)
                    break

    def filter_research(self):
        for completed_research in self.progress.research:
            for research in self.available_research:
                if completed_research.id == research.id:
                    self.available_research.remove(research)
                    break

    def add_company(self, new_company):
        self.companies.remove(new_company)
        self.progress.companies.append(new_company)
        self.progress.income += new_company.income
        self.progress.save()

    def add_research(self, new_research):
        new_research.finish_by = new_research.duration + self.progress.months
        self.progress.research.append(new_research)
        self.research.remove(new_research)
        self.progress.save()

    def get_available_improvements(self, improvements):
        result = []
        for improvement in improvements:
            for research in self.progress.research:
                if improvement.research_id == research.id and research.completed:
                    result.append(improvement)
                    break

        return result
