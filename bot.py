import discord
from discord.ext import commands
import responses
import asyncio

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)

async def pomodoro(message):
    await message.channel.send(f"Your studying time has started for 45 minutes.")
    await asyncio.sleep(1500) # 1500 seconds = 25 minutes 
    await message.channel.send("Take a 15 minute break!")
    await asyncio.sleep(300) # 300 seconds = 5 minutes
    await message.channel.send("Break time ended. Use !pomodoro to continue your next session!")
    return

def run_discord_bot():
    TOKEN = 'MTA2MTM1NjEzMzcyNzYwNDc0Ng.GaUvMP.bha9R24oeFoH4Nw38X_zEAG9EuQ1zeZ1t1RRVA'
    intents = discord.Intents.default   ()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
       
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message == '!pomodoro':
            await pomodoro(message)
        elif user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message)

    client.run(TOKEN)