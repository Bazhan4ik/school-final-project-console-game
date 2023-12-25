from utils.interface import Interface
from utils.game import Game


interface = Interface()
game = Game()

for _ in range(50):
    print("\n")

while True:
    interface.console.remove_lines()
    interface.set_tab("Main menu >")

    action = interface.main_menu(
        game.progress.companies,
        game.available_research,
        game.progress.research,
        game.progress.balance,
        game.progress.assets,
        game.progress.income,
        game.progress.months,
    )

    interface.console.remove_lines()

    if action == 1:
        interface.set_tab("Main menu > Companies")

        secondary_action = interface.companies_interface(
            game.progress.companies, game.available_companies, game.progress.research
        )

        interface.console.remove_lines()

        if secondary_action == 3:
            interface.set_tab("Main menu > Companies > Buy")

            result = interface.select_company(
                game.progress.balance, game.available_companies
            )

            if result == 0:
                continue

            game.add_company(result)
        elif secondary_action == 2:
            interface.set_tab("Main menu > Companies > Company info")

            company = interface.select_company__info(game.progress.companies)

            if company == 0:
                continue

            interface.console.remove_lines()

            available_improvements = game.get_available_improvements(
                company.improvements, company.improved
            )

            next_step = interface.company_info(company, available_improvements)

            if next_step == 2:
                interface.console.remove_lines()

                interface.set_tab("Main menu > Companies > Company info > Improve")

                improvement = interface.improve_company(
                    game.progress.balance, available_improvements
                )

                if improvement == 0:
                    continue

                game.improve_company(company.id, improvement)
        elif secondary_action == 4:

            def has_available_improvements(el):
                for improvement in el.improvements:
                    for research in game.progress.research:
                        if (
                            improvement.id not in el.improved
                            and research.id == improvement.research_id
                            and research.completed
                        ):
                            return True
                return False

            company = interface.select_company__info(
                list(filter(has_available_improvements, game.progress.companies))
            )

            if company == 0:
                continue

            interface.console.remove_lines()

            interface.set_tab("Main menu > Companies > Company info > Improve")

            available_improvements = game.get_available_improvements(
                company.improvements, company.improved
            )

            improvement = interface.improve_company(
                game.progress.balance, available_improvements
            )

            if improvement == 0:
                continue

            game.improve_company(company.id, improvement)

        elif secondary_action == 1:
            continue
    elif action == 2:
        interface.set_tab("Main menu > Research")

        secondary_action = interface.research_interface(
            game.progress.balance,
            game.available_research,
            game.progress.currently_researching(),
            game.progress.months,
        )

        if secondary_action == 1:
            continue
        elif secondary_action == 2:
            interface.console.remove_lines()

            interface.set_tab("Main menu > Research > Buy")
            result = interface.select_research(
                game.progress.balance, game.available_research
            )

            if result == 0:
                continue

            game.add_research(result)

    elif action == 3:
        game.moveon()

        if game.progress.balance + game.progress.assets > 200000:
            break


interface.you_won(game.progress.balance, game.progress.assets, game.progress.months)
