from board import Board
class Player:
    """
    A class representing a player in the Monopoly game.

    Attributes:
    - name (str): The name of the player.
    - symbol (str): The symbol representing the player on the board.
    - location (int): The current location of the player on the board.
    - properties (list): A list of properties owned by the player.
    - railroads (int): The number of railroads owned by the player.
    - utility (int): The number of utilities owned by the player.
    - inJail (bool): A flag indicating whether the player is in jail or not.
    - money (int): The amount of money the player has.

    Methods:
    - move(die_roll): Moves the player's location on the board by the specified die roll.
    - buy(property, price): Buys a property for the specified price if the player has enough money.
    - sell(property, price): Sells a property for the specified price if the player owns it.
    - trade(player, get, price_get, price_give, give): Trades properties and money between two players.
    """
    def __init__(self, name, symbol):
        self.cards = Board().cards
        self.name = name
        self.symbol = symbol
        self.location = 0
        self.properties = []
        self.railroads = 0
        self.utility = 0
        self.inJail = False
        self.money = 1500

    def move(self, die_roll):
        """
        Moves the player's location on the board by the specified die roll.

        Args:
        - die_roll (int): The number rolled on the dice.

        Returns:
        - The new location of the player on the board.
        """
        self.location += die_roll
        return self.location
    
    def buy(self, location):
        """
        Buys a property for the specified price if the player has enough money.

        Args:
        - property (str): The name of the property to buy.
        - price (int): The price of the property.

        Returns:
        - True if the property was bought successfully, False otherwise.
        """
        if(location['house_price'] > self.money):
            return False
        else:
            self.money -= location['house_price'] 
            self.properties.append(location['name'])
            return True
    
    def sell(self, property, price):
        """
        Sells a property for the specified price if the player owns it.

        Args:
        - property (str): The name of the property to sell.
        - price (int): The price to sell the property for.

        Returns:
        - True if the property was sold successfully, False otherwise.
        """
        if(property in self.properties):
            self.money += price
            self.properties.remove(property)
            return True
        else:
            return False 
        
    def trade(self, player,get, price_get,price_give, give):
        """
        Trades properties and money between two players.

        Args:
        - player (Player): The player to trade with.
        - get (list): A list of properties to get from the other player.
        - price_get (int): The amount of money to give to the other player for their properties.
        - price_give (int): The amount of money to receive from the other player for your properties.
        - give (list): A list of properties to give to the other player.

        Returns:
        - True if the trade was successful, False otherwise.
        """
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
    
    def playerInfo(self):
        return f"{self.name} with the symbol of {self.symbol} is at {self.cards[self.location]['name']} and has ${self.money}\n{self.properties} "
    