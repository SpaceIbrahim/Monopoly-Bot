class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.location = 0
        self.properties = []
        self.money = 1500

    def move(self, die_roll):
        self.location += die_roll
        return self.location
    
    def buy(self, location, price):
        if(price > self.money):
            return False
        else:
            self.money -= price
            self.properties.append(location)
            return True
    
    def sell(self, property, amount):
        if(property in self.properties):
            self.money -= price
            self.properties.append(location)
            return True
        else:
            return False