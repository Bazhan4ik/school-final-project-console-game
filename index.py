from utils.interface import Interface
from utils.game import Game

# from utils.research import get_interfaces
# from utils.tracker import get_progress

interface = Interface()
game = Game()


while True:
    action = interface.main_menu(game.companies, ["research1"], 123)

    if action == "research":
        secondary_action = interface.research()

    break
