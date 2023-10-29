import discord
import os
import dotenv
from discord.ext import commands

from monopoly import Monopoly

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='`', intents=intents)

monopoly = Monopoly()
symbols = ["penguin", "alien", "robot", "unicorn"]
global game_start, player_loc
playerName = []
playerSymbol = []
game_start = [False]
player_loc = {}


@client.event
async def on_ready():
    print(f"{client.user} is now running")

@client.command()
async def play(ctx):
    await ctx.send("Let's Play Monopoly!\nUpto 4 players can play at a time.\nType ``join symbol name` to join the game.\nThere are 4 symbols to choose from: `🐧 penguin` `👽 alien` `🤖 robot` `🦄 unicorn`\nType `start` to start the game.")


@client.command()
async def start(ctx):
    global game_start
    game_start = [True]
    if len(playerName) != 0:
        await ctx.send("Game has started")
        await ctx.send(f"It's {monopoly.players[0].name}'s turn. Enter ''turn' to roll the die.")
    else:
        await ctx.send("No players in game")


@client.command(pass_context=True)
async def join(ctx):
    if(game_start[0] == False):
        username = ctx.message.author.name
        content = ctx.message.content.split()
        if(monopoly.numPlayers == 4):
            await ctx.send("Game is full")
            return None
        if(content[1] in playerSymbol):
            await ctx.send("Symbol already taken")
            return None
        if(username in playerName):
            await ctx.send("Player already in game")
            return None
        if(content[1] in symbols):
            playerName.append(username)
            playerSymbol.append(content[1])
            monopoly.addPlayers(username, content[1])
            await ctx.send(f"{username} has joined the game with the symbol {content[1]}")
        else:
            await ctx.send("Invalid symbol, Player not added")
    else: 
        await ctx.send("Game has already started")

@client.command()
async def players(ctx):
    for i in range(len(playerName)):
        await ctx.send(f"{playerName[i]} is in the game with the symbol of {playerSymbol[i]}")

@client.command(pass_context=True)
async def playerinfo(ctx):
    username = ctx.message.author.name
    if(username not in playerName):
        await ctx.send("Player not in game")
        return None
    await ctx.send(monopoly.players[playerName.index(username)].playerInfo())   


@client.command(pass_context=True)
async def turn(ctx):
    if(game_start[0] == False):
        await ctx.send("Game has not started")
        return None
    username = ctx.message.author.name
    global player_loc
    if(username != monopoly.players[monopoly.turn].name):
        await ctx.send(f"It's {monopoly.players[monopoly.turn].name}'s turn")
        return None
    
    out = monopoly.doTurn()
    await ctx.send(out[0])
    await ctx.send(file=discord.File('images/out.png'))
    loc = out[1]
    output = monopoly.location_landed(loc)
    player_loc = output[0]

    match output[1]:
        case 0:
            await ctx.send(f"{out[2]} {output[2]}")

            await ctx.send(f"$200 has been removed from {out[2]}")
        case 1:
            await ctx.send(f"{out[2]} {output[2]}, ``buy` to buy or ``end` to end turn")
        case 2:
            await ctx.send(f"{out[2]} {output[2]}, ``buy` to buy or ``end` to end turn")
        case 3:
            await ctx.send(f"{out[2]} {output[2]}")
            # Collect $200
        case 4:
            await ctx.send(f"{out[2]} {output[2]}")
            # Go Jail
        case 5:
            await ctx.send(f"{out[2]} {output[2]}")
        case 6:
            await ctx.send(f"{out[2]} {output[2]}")
        case 7:
            await ctx.send(f"{out[2]} {output[2]}")
            # Random
        case 8:
            await ctx.send(f"{out[2]} {output[2]}, ``buy` to buy or ``end` to end turn")
        case 9:
            await ctx.send(f"{out[2]} {output[2]}")
        case _:
            pass

@client.command(pass_context=True)
async def buy(ctx):
    username = ctx.message.author.name
    if(username != monopoly.players[monopoly.turn].name):
        await ctx.send(f"It's {monopoly.players[monopoly.turn].name}'s turn")
        return None
    out = monopoly.buy(monopoly.turn, player_loc)
    await ctx.send(out)


@client.command(pass_context=True)
async def end(ctx):
    username = ctx.message.author.name
    if(username != monopoly.players[monopoly.turn].name):
        await ctx.send(f"It's {monopoly.players[monopoly.turn].name}'s turn")
        return None
    monopoly.endTrun()
    await ctx.send(f"It's {monopoly.players[monopoly.turn].name}'s turn. Enter ''turn' to roll the die.")
    
    
# @client.command()
# async def epic(ctx):
#     await ctx.send(file=discord.File('out.png'))
client.run(TOKEN)