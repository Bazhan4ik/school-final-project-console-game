from utils.interface import Interface
from utils.game import Game

# from utils.research import get_interfaces
# from utils.tracker import get_progress

interface = Interface()
game = Game()


while True:
    action = interface.main_menu(game.progress.get("companies"), ["research1"], 123)

    interface.console.remove_lines()

    if action == 1:
        secondary_action = interface.companies_interface(
            game.progress.get("companies"), game.companies
        )

        if secondary_action == 3:
            interface.buy_company(game.progress.get("balance"), game.companies)

    break
