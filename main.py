import discord
import os

client = discord.Client()
prefix = 'ted '

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        args = message.content.split(' ')[1:]

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        await member.move_to(None)

client.run(os.environ.get('DISCORD_TOKEN'))
