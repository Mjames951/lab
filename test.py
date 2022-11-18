import pytest
from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('test1')
        self.account2 = Account('test2')

    def teardown_method(self):
        del self.account1
        del self.account2
    def test_init(self):
        assert self.account1.get_name() == 'test1'
        assert self.account2.get_name() == 'test2'
        assert self.account1.get_balance() == 0
        assert self.account2.get_balance() == 0
    def test_deposit(self):
        assert self.account1.deposit(10) == True
        assert self.account2.deposit(-10) == False
        assert self.account2.deposit(0) == False
        assert self.account1.get_balance() == 10
        assert self.account2.get_balance() == 0
    def test_withdraw(self):
        assert self.account1.deposit(10) == True
        assert self.account1.get_balance() == 10
        assert self.account1.withdraw(100) == False
        assert self.account1.withdraw(5) == True
        assert self.account2.withdraw(-5) == False
        assert self.account2.withdraw(0) == False
        assert self.account1.get_balance() == 5
        assert self.account2.get_balance() == 0

def main():
    T = Test
    T.setup_method()
    T.test_init()
    T.test_deposit()
    T.test_withdraw()
    T.teardown_method()


if __name__ == '__main__':
    main()

