from nextcord import *
from nextcord.ext import commands
import os
import logging
import random

TOKEN = os.getenv("DISCORD_TOKEN")

tommy_media = ["https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612810474324058/20220307_184343.jpg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612810772152341/EM7Fl_mWsAIO76k.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811162218516/1500x500.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811703263252/FNQ5BW_XwAYgdsd.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811963326484/FNM5APGXsAskDXw.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612838496469002/FLDYs6ZX0AIZlmy.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612838836228106/FLlaIRlXMAQa5Jv.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840014823454/FLzK9HCXMAcKgIx.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840232935474/FMoa4L1XwAEbG2w.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840505573406/FMxrD_wXsAMAqF0.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840862076948/FMxrDffXsAUU4aS.jpeg"]

bot = commands.Bot(command_prefix="t!", description="Tommybot is a custom bot made for Tommylore and Sas, made by >>#0001.", owner_ids={889744885937225739,743340045628342324})

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def tommy(ctx):
    await ctx.send(random.choice(tommy_media))

@bot.command()
async def ogtommy(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG")

@bot.command()
async def jinx(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/947901923078586480/jinx.png")

@bot.command()
async def soggycat(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/950201643578822686/soggycat.png")

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction("<:tommythumbsup:946649096645664768>")
    await ctx.message.add_reaction("<:tommythumbsdown:947042965484896287>")

bot.run(TOKEN)