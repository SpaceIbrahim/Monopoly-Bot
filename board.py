import json
from imager import Imager

class Board:
    def __init__(self):
        with open('cards.json', 'r') as f:
            self.cards = json.load(f)
        
    def getLocation(self, n):
        return self.cards[n]
    
    def addOwner(self, n, owner):
        self.cards[n]['owner'] = owner
        
    def createBoard(self, players):
        imager = Imager()
        imager.creatBoard(players)