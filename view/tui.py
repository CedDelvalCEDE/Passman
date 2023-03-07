from colorama import Fore, Back, Style


class Tui:
    @staticmethod
    def print_msg(prompt: str):
        """custom print for simple message"""
        print(Fore.CYAN + Back.BLACK + Style.NORMAL + prompt)

    @staticmethod
    def print_error_msg(prompt: str):
        """custom print for error message"""
        print(Fore.RED + Back.BLACK + Style.NORMAL + prompt)

    @staticmethod
    def show_content(vault_dict: dict):
        """custom print for showing a dictionary"""
        str_converter = str(vault_dict)
        print(Fore.CYAN + Back.BLACK + Style.NORMAL + str_converter)

    @staticmethod
    def ask(prompt: str = '') -> str:
        """custom input"""
        answer = input(Fore.CYAN + Back.BLACK + Style.NORMAL + prompt)
        return answer

    def view_start_menu(self):
        """the start menu console message"""
        self.print_msg(" || PASSMAN || ")
        self.print_msg('1.register \n2.login \n3.exit')

    def view_main_menu(self):
        """the main menu console message for connected users"""
        self.print_msg(" || PASSMAN || ")
        self.print_msg('1.Show your vault\n2.add an account\n3.change an account\n4.suppress an account\n5.suppress '
                       'your account\nand your vault\n6.disconnect')

    def view_mod_menu(self):
        """the menu for change a part of the item targeted"""
        self.print_msg(" || PASSMAN || ")
        self.print_msg('1.Change the platform \n2.Change the username \n3.Change the password\n4.Change anything')
