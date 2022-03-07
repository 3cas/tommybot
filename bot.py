from nextcord import *
from nextcord.ext import commands
import os
import logging

TOKEN = os.getenv("DISCORD_TOKEN")

tommy_media = "https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG"
jinx_media = "https://cdn.discordapp.com/attachments/935315804067594290/947901923078586480/jinx.png"
soggycat_media = "https://cdn.discordapp.com/attachments/935315804067594290/950201643578822686/soggycat.png"
emoji_up = "<:tommythumbsup:946649096645664768>"
emoji_down = "<:tommythumbsdown:947042965484896287>"

bot = commands.Bot(command_prefix="t!", description="Tommybot is a custom bot made for Tommylore and Sas, made by >>#0001.", owner_ids={889744885937225739,743340045628342324})

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def tommy(ctx):
    await ctx.send(tommy_media)

@bot.command()
async def jinx(ctx):
    await ctx.send(jinx_media)

@bot.command()
async def soggycat(ctx):
    await ctx.send(soggycat_media)

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction(emoji_up)
    await ctx.message.add_reaction(emoji_down)

bot.run(TOKEN)