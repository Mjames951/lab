class Account:
    def __init__(self, name: str) -> None:
        '''
        creates Account class with default balance: 0
        :param name: name of the account
        '''
        self.__account_name: str = name
        self.__account_balance: int = 0

    def deposit(self, amount: int) -> bool:
        '''
        Deposits money into account
        :param amount: amount of money to be added into account
        :return: boolean indicating success/failure of deposit
        '''
        if amount<=0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: int) -> bool:
        '''
        withdraws money from the account
        :param amount: amount of money to be withdrawn from account
        :return: boolean indicating succuss/failure of withdrawal
        '''
        if amount<=0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        '''
        :return: balance of the account
        '''
        return self.__account_balance

    def get_name(self) -> int:
        '''
        :return: name of the account
        '''
        return self.__account_name
