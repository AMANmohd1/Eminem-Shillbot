import discord
import os
import requests
import json
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from random import randint
from keep_alive import keep_alive
import praw
#import bot
#from discord.ext import commands

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

#my_secret3 = os.environ['reddit_key']
my_secret3 = os.environ['red_key']
reddit = praw.Reddit(
  client_id = "SUTo8rPT0MwS2BIETuWQOQ",
  client_secret = my_secret3,
  password =  os.environ['reddit_pass'],
  username = "ArtoriasKEKW",
  user_agent = "<reddit_bot>",
)

subreddit = reddit.subreddit("copypasta")

def get_emote():
  response = requests.get("https://api.betterttv.net/2/emotes")
  json_data = response.json()
  emote = "https:" + json_data['urlTemplate'][:26]
  return emote

# bot = commands.Bot(command_prefix = '#')  
#bot = discord.Client()

# @bot.command()
# async def emote(ctx,arg):
#   await ctx.send(f'CHAKKA {arg}')

# @bot.command()
# async def ping(ctx):
# 	await ctx.channel.send("pong")

# bot.run(my_secret)


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
    # gfg = BeautifulSoup(comment,features="html5lib")
    # res = gfg.get_text('\n')

    embed = discord.Embed(title = '**'+comment+'**')
    embed.set_thumbnail(url = "https://c.tenor.com/cHlqDAcNK4AAAAAC/eminem-funny.gif")


    await msg.channel.send(embed = embed)

  if msg.content.startswith('!commands'):
    comment = '!comment - Get random Eminem video comment \n!copypasta - Get random Copypasta \n!eminem - Get info on Eminem \n!salman - Sallu bhai \n!chad - Get Chad \n!virgin - Get Virgin' 
    gfg = BeautifulSoup(comment,features="html5lib")
    res = gfg.get_text('\n')
    await msg.channel.send(res)

  if msg.content.startswith('!copypasta'):
    posts = []
    for post in subreddit.hot(limit = 25):
      posts.append(post)
    rand_post = posts[randint(0,24)]
    # final_post = '**'+rand_post.title+'**'+'\n'+'||'+rand_post.selftext+'||'
    # gfg = BeautifulSoup(final_post,features="html5lib")
    # res = gfg.get_text('\n')

    embed = discord.Embed(title = '**'+rand_post.title+'**',description = '||'+rand_post.selftext+'||')
    embed.set_thumbnail(url = "https://indiachan.com/.media/0fbe360148942114b6de94b58a410dc6d6fbb91751d9609b134cc694e3a1d8e0.png")
    

    await msg.channel.send(embed = embed)

  if msg.content.startswith('!salman'):
    await msg.channel.send('https://c.tenor.com/s4OGlEEUjr4AAAAM/salman-salman-khan.gif')

  if msg.content.startswith('!chad'):
    await msg.channel.send('https://c.tenor.com/epNMHGvRyHcAAAAd/gigachad-chad.gif')

  if msg.content.startswith('!virgin'):
    gifs = ['https://c.tenor.com/XKn8KJEUDzYAAAAC/wholesome-soyjak.gif','https://c.tenor.com/ZYPXJctKRwoAAAAM/soy-soyboy.gif','https://i.kym-cdn.com/photos/images/original/001/885/652/5d7.gif','https://c.tenor.com/xeZETjEU6LkAAAAC/soy-wojak.gif','https://c.tenor.com/cReKTEjjaOIAAAAd/soy-soyjak.gif']
    await msg.channel.send(gifs[randint(0,len(gifs)-1)])

  if msg.content.startswith('!garib'):
    gifs = ['https://c.tenor.com/-7ON2Lqx030AAAAM/mai-garib-hu.gif','https://c.tenor.com/zh7vqYkWZZYAAAAS/main-garib.gif']
    await msg.channel.send(gifs[randint(0,len(gifs)-1)])

  if msg.content.startswith('!kanye'):
    response = requests.get("https://api.kanye.rest")
    json_data = response.json()
    img = discord.File('kanye.png')
    post = '**'+json_data['quote']+'**'
    embed = discord.Embed(title = post)
    embed.set_thumbnail(url = "https://indiachan.com/.media/0fbe360148942114b6de94b58a410dc6d6fbb91751d9609b134cc694e3a1d8e0.png")
    embed.set_image(url="https://media.discordapp.net/attachments/900311173524783135/926863350284030002/kanye.png")
    await msg.channel.send(embed=embed)

keep_alive()
client.run(my_secret)