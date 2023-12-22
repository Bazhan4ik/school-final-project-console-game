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
        game.available_research[0:10],
        game.progress.balance,
        game.progress.income,
        game.progress.months,
    )

    interface.console.remove_lines()

    if action == 1:
        interface.set_tab("Main menu > Companies")

        secondary_action = interface.companies_interface(
            game.progress.companies, game.available_companies
        )

        interface.console.remove_lines()

        if secondary_action == 3:
            interface.set_tab("Main menu > Companies > Buy")

            next_step = interface.buy_company(
                game.progress.balance, game.available_companies
            )

            if next_step == 1:
                continue
            elif next_step == 2:
                interface.console.remove_lines()

                interface.set_tab("Main menu > Companies > Buy > Almost there")
                result = interface.select_company(
                    game.progress.balance, game.available_companies
                )

                if result == 0:
                    continue

                game.add_company(result)
        elif secondary_action == 2:
            interface.set_tab("Main menu > Companies > Company info")

            result = interface.select_company__info(game.progress.companies)

            if result == 0:
                continue

            interface.console.remove_lines()

            interface.company_info(
                result, game.get_available_improvements(result.improvements)
            )

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
