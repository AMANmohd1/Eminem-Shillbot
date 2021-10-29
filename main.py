import discord
import os
import requests
import json
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from random import randint
from keep_alive import keep_alive

client = discord.Client()
my_secret2 = os.environ['You_API']
my_secret = os.environ['TOKEN']
vids=["XbGs_qK2PQA","j5-yKhDd64s","r_0JjYUe5jo","8CdcCD5V-d8","1wYNFfgrXTI"]
orders = ["relevance","time","orderUnspecified"]
rand_order=orders[randint(0,2)]

youtube = build('youtube','v3',developerKey=my_secret2)

request = youtube.commentThreads().list(
  part="snippet",
  videoId=vids[randint(0,4)],
  order=rand_order
)

def get_com():
  response = request.execute()
  items = response["items"][randint(0,19)]
  item_info = items["snippet"]
  topLevelComment = item_info["topLevelComment"]
  comment_info = topLevelComment["snippet"]
  return(comment_info["textDisplay"])
  # for item in items:
  #  item_info = item["snippet"]
  #  topLevelComment = item_info["topLevelComment"]
  #  comment_info = topLevelComment["snippet"]
  #  return(comment_info["textDisplay"]) 


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!eminem'):
    await msg.channel.send('MOST UNDERRATED RAPPER')

  if msg.content.startswith('!comment'):
    comment = get_com()
    gfg = BeautifulSoup(comment,features="html5lib")
    res = gfg.get_text('\n')
    await msg.channel.send(res)

keep_alive()
client.run(my_secret)