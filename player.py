class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.location = 0
        self.properties = []
        self.railroads = 0
        self.utility = 0
        self.inJail = False
        self.money = 1500

    def move(self, die_roll):
        self.location += die_roll
        return self.location
    
    def buy(self, property, price):
        if(price > self.money):
            return False
        else:
            self.money -= price
            self.properties.append(property)
            return True
    
    def sell(self, property, price):
        if(property in self.properties):
            self.money += price
            self.properties.remove(property)
            return True
        else:
            return False
        
    def trade(self, player,get, price_get,price_give, give):
        for i in give:
            if i not in self.properties:
                return False
        for i in get:
            if i not in player.properties:
                return False
        
        # if the money player has is less than the difference between the money you give and get
        if self.money < price_get - price_give or player.money < price_give - price_get:
            return False
        
        for i in give:
            player.properties.append(i)
            self.properties.remove(i)
        for i in get:
            self.properties.append(i)
            player.properties.remove(i)

        self.money -= price_give
        self.money += price_get

        player.money -= price_get
        player.money += price_give
        
        return True
    