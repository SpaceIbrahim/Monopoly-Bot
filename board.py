import json
from imager import Imager

class Board:
    def __init__(self):
        with open('cards.json', 'r') as f:
            self.cards = json.load(f)
    
    def getLoc(self, n):
        for i in self.cards:
            if i['name'] == n:
                return i
    def getLocation(self, n):
        return self.cards[n]
    
    def addOwner(self, n, owner):
        self.cards[n]['owner'] = owner
    
    def rent(self, location, player):
        if location["attribute"] == "railroad":
            return location["rent"]*player.set["railroad"]
        elif location["attribute"] == "utility":
            return location["rent"][player.set["utility"]]
        else:
            return location["rent"][player.set[location["color"]] + player.house[location["color"]]]

    def createBoard(self, players):
        imager = Imager()
        imager.creatBoard(players)