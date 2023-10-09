import bot
import board
from player import Player

if __name__ == '__main__':
    # bot.run_discord_bot()
    player1 = Player("Ibbi", "PE")
    player2 = Player("Ibbi", "PE")
    player1.buy("BOBS HOUSE", 300)
    print(player1.properties)
    print(player1.money)

    a = player2.trade(player1, ["BOBS HOUSE"], 0, 350, [])
    print(a)

    print(player1.properties)
    print(player1.money)

    print(player2.properties)
    print(player2.money)
    print([1,2] == [2,1])


