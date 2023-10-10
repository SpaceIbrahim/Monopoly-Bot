import json
class Board:
    def __init__(self):
        with open('cards.json', 'r') as f:
            self.cards = json.load(f)
        
    def getLocation(self, n):
        return self.cards[n]

# board = Board()
# for i in board.cards:
#     if 'color' in i:
#         print(i['color'])