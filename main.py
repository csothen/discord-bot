import os
import discord
from dotenv import load_dotenv
import utils

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        if utils.isAllowedChannel(message.channel):
            await utils.handle_message(message)
        else:
            await message.channel.send(
                'Bot commands are not allowed on this channel!', delete_after=2)
            await message.delete()


client.run(os.getenv('TOKEN'))
