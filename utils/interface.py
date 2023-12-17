import sys
import time


class Interface:
    size = 100
    grid = int(size / 3)

    def __init__(self):
        self.console = Console()

    def main_menu(self, balance):
        self.console.print("")
        self.console.print("MAIN MENU ".ljust(self.size, "-"))
        self.console.print(
            "| Companies".ljust(self.grid),
            "| Research".ljust(self.grid),
            "| Balance".ljust(self.grid),
        )

        action = self.console.actions(self.size, "Companies", "Research")

        self.console.remove_lines()


class Console:
    lines_tracker = 0

    def remove_lines(self):
        for _ in range(self.lines_tracker):
            sys.stdout.write("\033[F")  # Cursor up one line
            sys.stdout.write("\033[K")  # Clear line
        self.lines_tracker = 0

    def print(self, *str):
        print("".join(str))
        self.lines_tracker += 1

    def input(self, str):
        result = input(str)
        self.lines_tracker += 1
        return result

    def actions(self, interface_size, *options):
        output = ""
        self.print("")
        self.print("".center(interface_size, "-"))
        self.print("[?] Choose action")

        for id, option in enumerate(options):
            # output = output + (f"({id}) " + option).ljust(
            #     int(interface_size / len(options))
            # )
            self.print(
                f"    ({id + 1}) " + option.ljust(int(interface_size / len(options)))
            )

        option = self.input("[?] Enter the number: ")

        return option
