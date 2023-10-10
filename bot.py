import discord
import os
import dotenv
from discord.ext import commands

from monopoly import Monopoly

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    # client = discord.Client(intents=intents)
    monopoly = Monopoly(0, [], [])
    playerNum = 0
    client = commands.Bot(command_prefix='`', intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.command()
    async def test(ctx, arg):
        await ctx.send(arg)

    @client.command()
    async def play(ctx):
        await ctx.send("Let's Play Monopoly!\nfdsfdsfdsf")

    # @client.command()
    # async def join(ctx):
    #     await ctx.send(f"{ctx.author}")

    @client.command(pass_context=True)
    async def name(ctx):
        username = ctx.message.author.name
        print(username)
    
    client.run(TOKEN)


run_discord_bot()