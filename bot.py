import discord
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

async def send_message(message, user_message):
    try:
        await message.channel.send("AAAAAAAA")
    except Exception as e:
        print(e)

def run_discord_bot():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    

    @client.event
    async def on_message(message):
        
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} on {channel}")
        # await message.channel.send("AAAAAAAA")

        if user_message == "balls":
            await message.channels.send()

    
    client.run(TOKEN)

    