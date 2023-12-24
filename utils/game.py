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

                self.filter_research()
                self.filter_companies()

        self.progress.save()

    def filter_companies(self):
        def ids_only(el):
            return el.id

        def research_completed(el):
            return el.completed

        purchased_companies_ids = list(map(ids_only, self.progress.companies))
        completed_research_ids = list(
            map(ids_only, list(filter(research_completed, self.progress.research)))
        )

        result = []

        for company in self.companies:
            company_purchased = company.id in purchased_companies_ids
            company_has_research = company.after in completed_research_ids

            if not company_purchased and company_has_research:
                result.append(company)

        self.available_companies = result

    def filter_research(self):
        def only_ids(el):
            return el.id

        def filter_research_completed(el):
            return el.completed

        # array of researches that are completed
        completed_research = list(
            filter(filter_research_completed, self.progress.research)
        )

        # ids of completed researches
        completed_research_ids = list(map(only_ids, completed_research))

        # ids of purchased, but not completed researches
        not_finished_research_ids = list(map(only_ids, self.progress.research))

        result = []

        for research in self.research:
            research_purchased = research.id in not_finished_research_ids
            research_after_completed = research.after in completed_research_ids
            research_has_after = research.after

            if (not research_purchased and research_after_completed) or (
                not research_has_after and not research_purchased
            ):
                result.append(research)

        self.available_research = result

    def add_company(self, new_company):
        self.companies.remove(new_company)
        self.progress.companies.append(new_company)
        self.progress.income += new_company.income
        self.progress.balance = round(self.progress.balance - new_company.worth, 2)
        self.filter_companies()
        self.progress.save()

    def improve_company(self, company_id, improvement):
        for company in self.progress.companies:
            if company.id == company_id:
                company.income += improvement.income
                self.progress.income += improvement.income
                if hasattr(company, "improved"):
                    company.improved.append(improvement.id)
                    break
                company.improved.append(improvement.id)

        self.progress.balance = round(self.progress.balance - improvement.price, 2)

        self.progress.save()

    def add_research(self, new_research):
        new_research.finish_by = new_research.duration + self.progress.months
        self.progress.research.append(new_research)
        self.available_research.remove(new_research)
        self.progress.balance = round(self.progress.balance - new_research.price, 2)
        self.progress.save()

    def get_available_improvements(self, improvements, improved):
        result = []
        for improvement in improvements:
            if improvement.id in improved:
                continue
            for research in self.progress.research:
                if improvement.research_id == research.id and research.completed:
                    result.append(improvement)
                    break

        return result
