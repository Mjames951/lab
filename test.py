import pytest
from account import *

delta = 0.001

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

def main():
    T = Test
    T.setup_method()
    T.test_init()
    T.teardown_method()


if __name__ == '__main__':
    main()

