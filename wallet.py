from coins import Coin

class Wallet(Coin):
    def __init__(self):
        self.money = []
        self.fill_wallet() 


    def fill_wallet(self):
        """Method will fill wallet's money list with certain amount of each type of coin when called."""
        index1 = Coin(8)
        index2 = Coin(10)
        index3 = Coin(20)
        index4 = Coin(50)
        
        self.money.append(index1)
        self.money.append(index2)
        self.money.append(index3)
        self.money.append(index4)