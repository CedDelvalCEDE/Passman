from model.model import VaultItem, User, Link
from view.tui import *


class MainApp:
    def __init__(self):
        """constructor of the main app"""
        self.data = Link()
        self.view = Tui()

    def start(self):
        """the start of the program"""
        self.view.view_start_menu()
        answer = self.view.ask('>>> ')
        match answer:
            case '1':
                user = self.register()
                if user is not bool:
                    self.main_menu(user)
            case '2':
                self.login()
            case '3':
                exit()
            case _:
                self.view.print_error_msg('You are not in case.')
        self.start()

    def register(self) -> bool or User:
        """used to register the users"""
        self.view.print_msg(' || CREATE ACCOUNT || ')
        username = self.view.ask("What is your username : ")
        if not self.data.find_user(username):
            user = User(username)
            password = self.view.ask("What is your password : ")
            user.add_password(password)
            self.data.add_user(user)
            return user
        else:
            self.view.print_error_msg('That username already exist. ')
            return False

    def login(self) -> bool:
        """used to log in the user"""
        self.view.print_msg(' || LOGIN ACCOUNT || ')
        username = self.view.ask("What is your username : ")
        if self.data.find_user(username) is not bool:
            # that condition is make like this because the function does not return True.
            user: User = self.data.find_user(username)
            password = self.view.ask("What is your password : ")
            if user.check(username, password):
                self.main_menu(user)
            else:
                self.view.print_error_msg('Your username or your password is/are false. ')
                return False
        else:
            self.view.print_error_msg('This username does not exist. ')
            return False

    def main_menu(self, user: User):
        """the main menu of a connected user"""
        self.view.view_main_menu()
        answer = self.view.ask('>>> ')
        match answer:
            case '1':
                self.show_the_vault(user)
            case '2':
                self.add_account(user)
            case '3':
                self.change_account(user)
            case '4':
                self.del_account(user)
            case '5':
                self.del_user_link(user)
            case '6':
                self.start()
            case _:
                self.view.print_error_msg('You are not in case.')
        self.main_menu(user)

    def show_the_vault(self, user: User):
        """list the user's vault"""
        for item in user.vault.vaults.values():
            item: VaultItem
            for content in item.dict.values():
                self.view.print_msg('-----------------------')
                self.view.show_content(content)

    def add_account(self, user: User):
        """setup a vault's item"""
        from_where = self.view.ask('platform :')
        username = self.view.ask('username :')
        password = self.view.ask('password :')
        user.vault.add_item(from_where, username, password)

    def change_account(self, user: User):
        """mod a vault's item"""
        from_where = self.view.ask('platform :')
        self.view.view_mod_menu()
        target = self.view.ask('>>> ')
        error: bool = True
        match target:
            case '1':
                new_content = self.view.ask('What will you write instead : ')
                error = user.vault.change_item_content('from_where', new_content, None, from_where)
            case '2':
                new_content = self.view.ask('What will you write instead : ')
                error = user.vault.change_item_content('username', new_content, None, from_where)
            case '3':
                new_content = self.view.ask('What will you write instead : ')
                error = user.vault.change_item_content('password', new_content, None, from_where)
            case '4':
                self.main_menu(user)
            case _:
                self.view.print_error_msg("You are not in case !!!")
                self.main_menu(user)
        if not error:
            self.view.print_error_msg("the change does not work. ")

    def del_account(self, user: User):
        """delete a vault's item"""
        from_where = self.view.ask('platform :')
        error = user.vault.del_item(from_where)
        if error:
            self.view.print_msg('the suppress is finished')
        else:
            self.view.print_error_msg("the suppress does not work. ")

    def del_user_link(self, user: User):
        """delete the connected user"""
        self.data.del_user(user)
        self.start()
