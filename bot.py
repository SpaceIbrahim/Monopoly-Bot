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
playerName = []
playerSymbol = []
symbols = ["penguin", "alien", "robot", "unicorn"]
start = [False]
@client.event
async def on_ready():
    print(f"{client.user} is now running")

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def play(ctx):

    await ctx.send("Let's Play Monopoly!\nUpto 4 players can play at a time.\nType ``join symbol name` to join the game.\nThere are 4 symbols to choose from: `🐧 penguin` `👽 alien` `🤖 robot` `🦄 unicorn`\nType `start` to start the game.")

# @client.command()
# async def join(ctx):
#     await ctx.send(f"{ctx.author}")

@client.command(pass_context=True)
async def join(ctx):
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

@client.command()
async def players(ctx):
    for i in range(len(playerName)):
        await ctx.send(f"{playerName[i]} with the symbol of {playerSymbol[i]}")

@client.command(pass_context=True)
async def playerInfo(ctx):
    username = ctx.message.author.name
    if(username not in playerName):
        await ctx.send("Player not in game")
        return None
    await ctx.send(monopoly.players[playerName.index(username)].playerInfo())   

@client.command()
async def start(ctx):
    await ctx.send("Game has started")
    await ctx.send(f"It's {monopoly.players[0].name}'s turn. Enter ''turn' to roll the die.")

@client.command(pass_context=True)
async def turn(ctx):
    username = ctx.message.author.name

    # print(monopoly.turn)
    # if(username != monopoly.players[].name):
    #     await ctx.send(f"It's {monopoly.players[monopoly.turn].name}'s turn")
    #     return None
    
    await ctx.send(monopoly.doTurn()[0])
    await ctx.send(file=discord.File('images/out.png'))
    
# @client.command()
# async def epic(ctx):
#     await ctx.send(file=discord.File('out.png'))
client.run(TOKEN)