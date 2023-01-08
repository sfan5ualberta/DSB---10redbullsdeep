import discord
import responses

review = False

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message, review)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2MTM1NjEzMzcyNzYwNDc0Ng.GaUvMP.bha9R24oeFoH4Nw38X_zEAG9EuQ1zeZ1t1RRVA'
    intents = discord.Intents.default   ()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        global review 
        review = False
        #file = open("{client.user}.txt", "w+") # create new text file to store user data
        #file.write("review = False\n") 
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)