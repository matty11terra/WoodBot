import discord
import requests
import requests_cache
from discord.ext import commands
token="redacted"
key='redacted'
url="https://api.hypixel.net/skyblock/bazaar?"
bot= commands.Bot(command_prefix ="!")
@bot.command()
async def wood(ctx):
  items=["ENCHANTED_OAK_LOG","ENCHANTED_ACACIA_LOG","ENCHANTED_SPRUCE_LOG","ENCHANTED_DARK_OAK_LOG","ENCHANTED_BIRCH_LOG"]
  mapping={"ENCHANTED_OAK_LOG":"oak","ENCHANTED_ACACIA_LOG":"acacia","ENCHANTED_SPRUCE_LOG":"spruce","ENCHANTED_DARK_OAK_LOG":"dark oak","ENCHANTED_BIRCH_LOG":"birch"}
  max_price=0
  max_wood=""

  db=requests.get(f'{url}key={key}').json()['products']
  for item in items: 
      if(db[item]["sell_summary"][0]['pricePerUnit']>max_price):
        max_price=db[item]["sell_summary"][0]['pricePerUnit']
        max_wood=item
  embed=discord.Embed(title=f'The best wood ATM is {mapping.get(max_wood)} at {max_price} per enchanted',description="Like the bot? consider supporting me at https://ko-fi.com/dabot/",colour=discord.Colour.green())
  await ctx.send(embed=embed)

bot.run(token)