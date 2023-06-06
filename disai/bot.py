import discord
from dotenv import load_dotenv
import os
from chatgpt import getanswer

load_dotenv()
my_secret = os.getenv("discord_key")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# DisAi

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author.id != 1109179784103215105 and message.channel.name == "chatgpt":
    await message.channel.send(getanswer(message.content))

  if message.content.startswith('who made you'):
    await message.channel.send('ur mom did')


client.run(my_secret)
