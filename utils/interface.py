import sys
import time


class Interface:
    size = 100
    col_size = int(size / 3)
    col2_size = int(size / 2)

    def __init__(self):
        self.console = Console()

    def main_menu(self, companies, research, balance):
        self.console.print("")
        self.console.print("MAIN MENU ".ljust(self.size, "-"))
        self.console.print(
            "| Companies".ljust(self.col_size),
            "| Research".ljust(self.col_size),
            "| Balance".ljust(self.col_size),
        )

        i = 0
        while True:
            col1 = "|"
            if len(companies) > i:
                col1 = f"| - {companies[i].get('name')} ({companies[i].get('income')})"

            self.console.print(
                col1.ljust(self.col_size),
                f"| - {research[i] if len(research) > i else ''}".ljust(self.col_size),
                "|".ljust(self.col_size),
            )
            i += 1
            if len(companies) <= i and len(research) <= i:
                break

        action = self.console.actions(self.size, "Companies", "Research")

        return action

    def companies_interface(self, progress, companies):
        self.console.print("")
        self.console.print("COMPANIES ".ljust(self.size, "-"))
        self.console.print(
            "| Your Companies".ljust(self.col2_size),
            "| Available Companies".ljust(self.col2_size),
        )

        i = 0
        while True:
            col1 = "|"
            if len(progress) > i:
                col1 = f"{progress[i].get('name')} (${progress[i].get('income')}/month)"

            col2 = "|"
            if len(companies) > i:
                col2 = f"| - {companies[i].get('name')} - ${companies[i].get('worth')}M"

            self.console.print(
                col1.ljust(self.col2_size),
                col2.ljust(self.col2_size),
            )

            i += 1
            if len(companies) <= i and len(progress) <= i:
                break

        action = self.console.actions(
            self.size, "Main menu", "Select company", "Buy company"
        )

        return action

    def buy_company(self, balance, companies):
        col1_size = int(self.size * 0.45)
        col2_size = int(self.size * 0.2)
        col3_size = int(self.size * 0.2)
        col4_size = int(self.size * 0.15)

        self.console.print("")
        self.console.print("MARKET ".ljust(self.size, "-"))
        self.console.print(
            "| Name".ljust(col1_size),
            "| Worth".ljust(col2_size),
            "| ~Income".ljust(col3_size),
            "| ~Potential".ljust(col4_size),
        )

        for i, company in enumerate(companies):
            self.console.print(
                f"| {company.get('name')}".ljust(col1_size),
                f"| ${company.get('worth')}M".ljust(col2_size),
                f"| ${company.get('income')}M/month".ljust(col3_size),
                f"| {company.get('income')}".ljust(col4_size),
            )

        action = self.console.actions(
            self.size, "Main menu", "Select company", "Buy company"
        )

        return action


class Console:
    lines_tracker = 0

    def remove_lines(self):
        for _ in range(self.lines_tracker):
            sys.stdout.write("\033[F")  # Cursor up one line
            sys.stdout.write("\033[K")  # Clear line
        self.lines_tracker = 0

    def remove1_line(self):
        sys.stdout.write("\033[F")  # Cursor up one line
        sys.stdout.write("\033[K")  # Clear line
        self.lines_tracker -= 1

    def print(self, *str):
        print("".join(str))
        self.lines_tracker += 1

    def input(self, str):
        result = input(str)
        self.lines_tracker += 1
        return result

    def actions(self, interface_size, *options):
        self.print("".center(interface_size, "-"))
        self.print("[?] Choose action")

        for id, option in enumerate(options):
            self.print(
                f"    ({id + 1}) " + option.ljust(int(interface_size / len(options)))
            )

        while True:
            try:
                option = self.input("[?] Enter the number: ")
                num = int(option)

                return num
            except ValueError:
                self.remove1_line()
                continue
