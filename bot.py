import numpy as np 
import pyautogui
import discord
import os


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ss'):
        await message.channel.send('Wait a sec')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('image.png')
        with open('image.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith('quirks'):
        await message.channel.send('Wait a sec')
        with open('quirks.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith('vip'):
        await message.channel.send('https://www.roblox.com/share?code=2609359802715345bef34d5107d8116c&type=Server')
    


client.run('ODcwNTE2MDc1NTM4ODM3NjA0.G7oUSM.6m5dnpJjXmy-jpV54FZeOGpAFIfsoTRwvvERuw')
