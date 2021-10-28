import discord
import os

client = discord.Client()
my_secret = os.environ['TOKEN']


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!eminem'):
    await msg.channel.send('MOST UNDERRATED RAPPER')

client.run(my_secret)