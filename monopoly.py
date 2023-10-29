from player import Player
from board import Board
from random import randint

class Monopoly():

    def __init__(self) -> None:
        self.turn = 0
        self.numPlayers = 0
        self.board = Board()
        self.players = []

    def addPlayers(self, name, symbol):
        self.players.append(Player(name, symbol))
        self.numPlayers += 1

    def endTrun(self):
        if self.turn == self.numPlayers -1:
            self.turn = 0
        else:
            self.turn +=1
    
    def doTurn(self):
        t = self.turn
        
        roll = self.rollDie()

        # print(t,"\n\n\n\n")
        self.players[t].move(roll)
        loc = self.players[t].location
        if loc >= 40:
            self.players[t].location = loc - 40
            loc -= 40
            # NEED TO ADD 200 TO PLAYER MONEY

        self.board.createBoard(self.players)
        outString = f"It's player {self.players[t].name}'s turn and they roll a {roll}! They landed on {self.board.getLocation(loc)['name']}"
        return [outString, self.board.getLocation(loc), self.players[t].name]
    
    def location_landed(self,location):
        if location['attribute'] == 'tax':
            str = f"landed on {location['name']} they must pay $200 in taxes to the IRS"
            return [location, 0, str]
        
        elif location['attribute'] == 'railroad':
            str = (f"landed on {location['name']} the price of this railroad is {location['house_price']}")
            return [location, 1, str]
        
        elif location['attribute'] == 'utility':
            str = (f"landed on {location['name']} the price of this utility is {location['house_price']}")
            return [location, 2, str]
        
        elif location['attribute'] == 'GO':
            str =(f"passed GO collect $200")
            return [location, 3, str]
        
        elif location['attribute'] == 'go jail':
            str =(f"landed on {location['name']} they are now in jail")
            return [location, 4, str]
        
        elif location['attribute'] == 'jail':
            str = (f"landed on {location['name']} they are just visiting")
            return [location, 5, str]
        
        elif location['attribute'] == 'Free Parking':
            str =(f"landed on {location['name']}, Nothing happens")
            return [location, 6, str]
        
        elif location['attribute'] == 'guess':
            str = (f"landed on {location['name']} are they lucky? or is luck there enemy?")
            return [location, 7, str]
        
        elif location['attribute'] == 'property':
            if location['owner'] == 'none':
                str =(f"landed on {location['name']} the price of this property is {location['house_price']}")
                return [location, 8, str]
            
            else:
                str = (f"landed on {location['name']} and is owned by {location['owner']}, they must pay {location['owner']} rent")
                return [location, 9, str]
            
        else:
            pass
    
    def buy(self, player, location):
        if self.players[player].buy(location):
            self.board.addOwner(location['position'], player)
            return "purchase successful"
        else:
            return "you are broke"
    def showPlayers(self):
        for i in self.players:
            print(f"{i.name} with the symbol of {i.symbol}")

    def rollDie(self) -> int:

        return randint(1, 12)
    

# mon = Monopoly()
# mon.addPlayers("John", "robot")
# for i in range(40):
#     mon.location_info(mon.board.getLocation(i))