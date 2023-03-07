

class VaultItem:
    def __init__(self, from_where: str, username: str, password: str):
        """constructor of the item"""
        self.dict: dict = {"from_where": from_where, "username": username, "password": password}

    def change_content(self, target: str, new_content: str):
        """change directly the part targeted of the item"""
        self.dict[target] = new_content


class Vault:
    def __init__(self):
        """constructor of the vault"""
        self.vaults = {}

    def add_item(self, from_where: str, username: str, password: str):
        """is the setup function for the vault's item"""
        new_vault_item = VaultItem(from_where, username, password)
        index = (len(self.vaults) + 1)
        self.vaults[index] = new_vault_item

    def del_item(self, from_where: str = None) -> bool:
        """is the tool of suppression for the vault's item"""
        for item_key in self.vaults.keys():
            item = self.vaults[item_key]
            if from_where == item.dict['from_where']:
                del self.vaults[item_key]
                return True
        return False

    def find_item(self, item_position: int = None, from_where: str = None) -> VaultItem or bool:
        """find a vault's item in the vault with the key 'from_where' or a positional argument"""
        if item_position is not None:
            if item_position in self.vaults.keys():
                item: VaultItem = self.vaults[item_position]
                return item
            else:
                return False
        if from_where is not None:
            for item in self.vaults.values():
                if from_where == item.dict['from_where']:
                    return item
                else:
                    return False
        else:
            return False

    def change_item_content(self, target: str, new_content: str, item_position: int = None,
                            from_where: str = None) -> bool:
        """change an item in the vault with find_item"""
        vault_item = self.find_item(item_position, from_where)
        if vault_item in self.vaults.values():
            vault_item.change_content(target, new_content)
            return True
        else:
            return False


class User:
    def __init__(self, username: str):
        """constructor of the user"""
        self.user = username
        self.password = "password"
        self.vault = Vault()

    def add_password(self, password: str):
        """add the password of the user"""
        self.password = password

    def rename_user(self, user: str):
        """change the username"""
        self.user = user

    def change_password(self, username: str, password: str, new_password):
        """change the password with a check"""
        if self.check(username, password):
            self.password = new_password

    def check(self, username: str, password: str) -> bool:
        """check if the user is the good one"""
        if username == self.user:
            if password == self.password:
                return True
            else:
                return False
        else:
            return False


class Link:
    def __init__(self):
        """constructor of the link, link regroup all users"""
        self.user = []

    def add_user(self, user: User):
        """add the user in the link list"""
        self.user.append(user)

    def del_user(self, user: User):
        """remove the user out of the list"""
        for item in self.user:
            if item == user:
                self.user.remove(item)
                return

    def find_user(self, username: str) -> User or bool:
        """find the user in the list"""
        for item in self.user:
            if item.user == username:
                return item
        return False
