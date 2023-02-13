
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, ’value’): # hasattr es para ver si existe el atributo value
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str)
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount

cuenta = Account("Cuenta", value=1000, type="Ahorro", currency="USD", bank="Banco de la Nación", number=123456789, owner="Juan Pérez", owner_id=12345678, owner_address="Av. Siempreviva 742", owner_phone="123456789", owner_email="")

class Bank(Object):
    def __init__(self):
        self._accounts = []

    def add(self, new_account):
        if not isinstance(new_account, Account):
            print("new_account debe ser de tipo Account")
            return False
        self._accounts.append(new_account)
        return True
    
    def transfer(self, origin, dest, amount):
        if not isinstance(origin, str):
            print("origin debe ser de tipo str")
            return False
        if not isinstance(dest, str):
            print("dest debe ser de tipo str")
            return False
        if not isinstance(amount, float):
            print("amount debe ser de tipo float")
            return False
        origin_account = self.fix_account(origin)
        dest_account = self.fix_account(dest)
        if origin_account is None:
            print("No existe la cuenta origen")
            return False
        if dest_account is None:
            print("No existe la cuenta destino")
            return False
        if origin_account.value < amount:
            print("No hay saldo suficiente en la cuenta origen")
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True


    
    def fix_account(self, name):
        for account in self._accounts:
            if account.name == name:
                return True
        return False

        




'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John Doe", 30)
print(p.__dict__)
#{'name': 'John Doe', 'age': 30}

'''









