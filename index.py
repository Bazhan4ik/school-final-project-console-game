from utils.interface import Interface
from utils.game import Game


interface = Interface()
game = Game()


while True:
    interface.console.remove_lines()

    action = interface.main_menu(
        game.progress.companies,
        game.research[0:10],
        game.progress.balance,
        game.progress.income,
    )

    interface.console.remove_lines()

    if action == 1:
        secondary_action = interface.companies_interface(
            game.progress.companies, game.companies
        )

        interface.console.remove_lines()

        if secondary_action == 3:
            next_step = interface.buy_company(game.progress.balance, game.companies)

            if next_step == 1:
                continue
            elif next_step == 2:
                interface.console.remove_lines()

                result = interface.select_company(game.progress.balance, game.companies)

                if result == 0:
                    continue
        elif secondary_action == 1:
            continue
    elif action == 3:
        game.moveon()
