from player import Player
from board import Board
from random import randint

class Monopoly():
    def __init__(self, num, names, symbol) -> None:
        self.turn = 0
        self.numPlayers = num-1
        self.board = Board()
        self.players = []
        for i in range(num):
            self.players.append(Player(names[i], symbol[i]))

    def doTurn(self):
        t = self.turn
        
        roll = self.rollDie()

        if self.turn == self.numPlayers:
            self.turn = 0
        else:
            self.turn +=1

        self.players[t].move(roll)
        loc = self.players[t].location
        if loc >= 40:
            self.players[t].location = loc - 40
            loc -= 40

        outString = f"It's player {self.players[t].name}'s turn and they roll a {roll}! They landed on {self.board.getLocation(loc)['name']}"
        return [outString, self.board.getLocation(loc)]
    
    def showPlayers(self):
        for i in self.players:
            print(f"{i.name} with the symbol of {i.symbol}")

    def rollDie(self) -> int:
        return randint(1, 12)
    
m = Monopoly(1, ["ibbi"], ["🦆"])
m.doTurn()