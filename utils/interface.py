import sys
import time


class Interface:
    size = 150
    col_size = int(size / 3)
    col2_size = int(size / 2)

    def __init__(self):
        self.console = Console()
        self.tab_tracker = "Main menu >"

    def set_tab(self, setto):
        self.tab_tracker = setto

    def main_menu(self, companies, research, balance, income, month):
        self.console.print(self.tab_tracker)
        self.console.print("MAIN MENU ".ljust(self.size, "-"))
        self.console.print(
            "| Your Companies".ljust(self.col_size),
            "| Available Research".ljust(self.col_size),
            "| Stats".ljust(self.col_size),
        )

        i = 0
        while True:
            col1 = "|"
            if len(companies) > i:
                col1 = f"| - {companies[i].name} (${companies[i].income}/month)"
            col2 = "|"
            if len(research) > i:
                col2 = f"| - {research[i].name} (${research[i].price}M)"
            col3 = "|"
            if i == 0:
                col3 = f"| Balance - ${balance}M"
            elif i == 1:
                col3 = f"| Income - ${income}M"
            elif i == 2:
                col3 = f"| Months passed - {month}"

            self.console.print(
                col1.ljust(self.col_size),
                col2.ljust(self.col_size),
                col3.ljust(self.col_size),
            )
            i += 1
            if len(companies) <= i and len(research) <= i and i > 2:
                break

        action = self.console.actions(self.size, "Companies", "Research", "Next Month")

        return action

    def companies_interface(self, progress, companies):
        self.console.print(self.tab_tracker)
        self.console.print("COMPANIES ".ljust(self.size, "-"))
        self.console.print(
            "| Your Companies".ljust(self.col2_size),
            "| Available Companies".ljust(self.col2_size),
        )

        i = 0
        while True:
            col1 = "|"
            if len(progress) > i:
                col1 = f"| - {progress[i].name} (${progress[i].income}/month)"

            col2 = "|"
            if len(companies) > i:
                col2 = f"| - {companies[i].name} - ${companies[i].worth}M"

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
        if len(companies) == 0:
            self.console.print("")
            self.console.print("")
            self.console.print("-= NO COMPANIES TO BUY =-")
            time.sleep(2.5)

            return 1

        col1_size = int(self.size * 0.45)
        col2_size = int(self.size * 0.2)
        col3_size = int(self.size * 0.2)
        col4_size = int(self.size * 0.15)

        self.console.print(self.tab_tracker)
        self.console.print(f"MARKET ----- BALANCE: ${balance}M ".ljust(self.size, "-"))
        self.console.print(
            "| Name".ljust(col1_size),
            "| Worth".ljust(col2_size),
            "| ~Income".ljust(col3_size),
            "| ~Potential".ljust(col4_size),
        )

        for i, company in enumerate(companies):
            self.console.print(
                f"| {company.name}".ljust(col1_size),
                f"| ${company.worth}M".ljust(col2_size),
                f"| ${company.income}M/month".ljust(col3_size),
                f"| {company.income}".ljust(col4_size),
            )

        action = self.console.actions(self.size, "Main menu", "Select company")

        return action

    def select_company(self, balance, companies):
        col1_size = int(self.size * 0.45)
        col2_size = int(self.size * 0.2)
        col3_size = int(self.size * 0.2)
        col4_size = int(self.size * 0.15)

        self.console.print(self.tab_tracker)
        self.console.print(f"MARKET ----- BALANCE: ${balance}M ".ljust(self.size, "-"))
        self.console.print(
            "| Name".ljust(col1_size),
            "| Worth".ljust(col2_size),
            "| ~Income".ljust(col3_size),
            "| ~Potential".ljust(col4_size),
        )

        for i, company in enumerate(companies):
            self.console.print(
                f"| [{i + 1}] {company.name}".ljust(col1_size),
                f"| ${company.worth}M".ljust(col2_size),
                f"| ${company.income}M/month".ljust(col3_size),
                f"| {company.income}".ljust(col4_size),
            )

        while True:
            number = self.console.ask_number(self.size, "Company's number")

            if number == -1:
                return 0

            if number < 0 or number > len(companies):
                self.console.remove_many_lines(4)
                continue

            selected_company = companies[number - 1]

            if selected_company.worth > balance:
                self.console.remove_lines()
                self.console.print()
                self.console.print()
                self.console.print(
                    "-= NOT ENOUGH FUNDS (BALANCE) =-".center(int(self.size / 2))
                )
                time.sleep(2.5)
                self.console.remove_lines()

                return 0

            return selected_company

    def select_company__info(self, companies):
        self.console.print(self.tab_tracker)
        self.console.print(f"YOUR COMPANIES ".ljust(self.size, "-"))
        self.console.print("| Select your company")

        for i, company in enumerate(companies):
            self.console.print(f"| [{i + 1}] {company.name}")

        while True:
            number = self.console.ask_number(self.size, "Company's number")

            if number == -1:
                return 0

            if number < 0 or number > len(companies):
                self.console.remove_many_lines(4)
                continue

            selected_company = companies[number - 1]

            return selected_company

    def company_info(self, company, improvements):
        self.console.print(self.tab_tracker)
        self.console.print("COMPANY INFO ".ljust(self.size, "-"))

        col1 = int(self.size * 0.4)
        col2 = int(self.size * 0.6)

        self.console.print(f"| {company.name}".ljust(col1), "| Available improvements")

        i = -1
        while True:
            i += 1
            if i == 0:
                self.console.print(
                    f"| Income ${company.income}M/month".ljust(col1),
                    f"| - {company.improvements[0].title} (${company.improvements[0].price}M)",
                )
                continue
            elif i == 1:
                if len(company.improvements) > 1:
                    self.console.print(
                        f"| Worth ${company.worth}M".ljust(col1),
                        f"| - {company.improvements[1].title} (${company.improvements[1].price}M)".ljust(
                            col2
                        ),
                    )
                else:
                    self.console.print(
                        f"| Worth ${company.worth}M".ljust(col1),
                        f"| ".ljust(col2),
                    )

                break

        action = self.console.actions(self.size, "Main menu")

    def research_interface(
        self, balance, research, currently_researching, current_months
    ):
        if len(research) == 0:
            self.console.print("")
            self.console.print("")
            self.console.print("-= NO RESEARCH TO DO =-")
            time.sleep(2.5)

            return 1

        col1_size = int(self.size * 0.5)
        col2_size = int(self.size * 0.25)
        col3_size = int(self.size * 0.25)

        self.console.print(self.tab_tracker)
        self.console.print(
            f"STUDYING ----- BALANCE: ${balance}M ".ljust(self.size, "-")
        )
        self.console.print(
            "| Name".ljust(col1_size),
            "| Price".ljust(col2_size),
            "| Duration".ljust(col3_size),
        )

        for cr in currently_researching:
            self.console.print(
                f"| {cr.name}".ljust(col1_size),
                f"| ${cr.price}M".ljust(col2_size),
                f"| {cr.finish_by - current_months} months left".ljust(col3_size),
            )

        for i, research in enumerate(research):
            self.console.print(
                f"| {research.name}".ljust(col1_size),
                f"| ${research.price}M".ljust(col2_size),
                f"| {research.duration} months".ljust(col3_size),
            )

        action = self.console.actions(self.size, "Main menu", "Select research")

        return action

    def select_research(self, balance, research_list):
        col1_size = int(self.size * 0.45)
        col2_size = int(self.size * 0.2)
        col3_size = int(self.size * 0.2)

        self.console.print(self.tab_tracker)
        self.console.print(
            f"STUDYING ----- BALANCE: ${balance}M ".ljust(self.size, "-")
        )
        self.console.print(
            "| Name".ljust(col1_size),
            "| Price".ljust(col2_size),
            "| Duration".ljust(col3_size),
        )

        for i, research in enumerate(research_list):
            self.console.print(
                f"| [{i + 1}] {research.name}".ljust(col1_size),
                f"| ${research.price}M".ljust(col2_size),
                f"| {research.duration} months".ljust(col3_size),
            )

        while True:
            number = self.console.ask_number(self.size, "Research's number")

            if number == -1:
                return 0

            if number < 0 or number > len(research_list):
                self.console.remove_many_lines(4)
                continue

            selected_research = research_list[number - 1]

            if selected_research.price > balance:
                self.console.remove_lines()
                self.console.print()
                self.console.print()
                self.console.print(
                    "-= NOT ENOUGH FUNDS (BALANCE) =-".center(int(self.size / 2))
                )
                time.sleep(2.5)
                self.console.remove_lines()

                return 0

            return selected_research


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

    def remove_many_lines(self, lines):
        for _ in range(lines):
            sys.stdout.write("\033[F")  # Cursor up one line
            sys.stdout.write("\033[K")  # Clear line
        self.lines_tracker -= lines

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

    def ask_number(self, interface_size, label):
        self.print("".center(interface_size, "-"))
        self.print(f"[?] {label}")
        self.print(f"[?] '-1' to cancel")

        while True:
            try:
                option = self.input("[?] Enter the number: ")
                num = int(option)

                return num
            except ValueError:
                self.remove1_line()
                continue
