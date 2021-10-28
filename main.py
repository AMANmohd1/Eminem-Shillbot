import discord
import os
import requests
import json
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from random import randint

client = discord.Client()
my_secret2 = os.environ['You_API']
my_secret = os.environ['TOKEN']
video_id = "XbGs_qK2PQA" #rap god

youtube = build('youtube','v3',developerKey=my_secret2)

request = youtube.commentThreads().list(
  part="snippet",
  videoId=video_id,
  order="relevance"
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

client.run(my_secret)