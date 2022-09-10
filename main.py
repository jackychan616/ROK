import os
from pydoc import describe
import discord
import asyncio
import json, time
import datetime
from dotenv import load_dotenv
import json
import discord
from discord.ext import bridge

intents = discord.Intents.all() 
intents.members = True
bot = discord.Bot(command_prefix="!", intents=intents,debug_guilds=[1015223481643827221,1015223481643827221,1015241177307557988])

@bot.slash_command(describe="test command")
async def test1(ctx):
    await ctx.respond(ctx.guild.id)

@bot.event
async def on_ready():
    print("bot is ready")   
@bot.event
async def on_member_join(member):
    with open(r"C:/Users/jacky/Documents/discord/ROK/config/data/guilds_data.json", "r+") as fp:
        data = json.load(fp)
        if str(member.guild.id) in data:
            data[str(member.guild.id)].updata({str(member):{}}) 
            fp.seek(0)
            json.dump(data, fp, indent=4)
            fp.truncate()


with open(r"C:\Users\jacky\Documents\discord\ROK\config\bot.json") as fp:
    token = json.load(fp)["token"]

bot.load_extension("command.verification")
bot.load_extension("command.members_profile")
bot.load_extension("command.re_webhook")
bot.run(token)


     







