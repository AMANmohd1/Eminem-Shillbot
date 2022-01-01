import os
import discord
from discord.ext import commands
my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix="#")

@bot.command()
async def lol(ctx,arg):
  await ctx.send(arg)


bot.run(my_secret)

