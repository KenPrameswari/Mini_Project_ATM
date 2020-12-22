from atm_card import ATMCard
class Customer(ATMCard):
    def __init__(self, id, defaultPin, defaultBalance):
        super().__init__(defaultPin, defaultBalance)
        self.id = id

    def withdrawBalance(self, nominal):
        self.nominal = nominal
        return self.defaultBalance - self.nominal

    def depositBalance(self, nominal):
        self.nominal = nominal
        return self.defaultBalance + self.nominal

    def checkPin(self):
        return self.defaultPin

    def checkBalance(self):
        return self.defaultBalance
