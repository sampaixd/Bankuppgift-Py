#from user import User


class Account:    #accounts where you store money
    def __init__(self, saldo, accountid):
        self.saldo = saldo
        self.accountid = accountid
    
    def AccountID(self):
        return self.accountid

    def Saldo(self):
        return self.saldo
