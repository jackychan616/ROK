import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.utils import get
import json

intents = discord.Intents.all()
intents.members = True
bot = discord.Bot(intents=intents,debug_guilds=[1015223481643827221,1015223481643827221,1015241177307557988])
url = ["https://discord.com/api/webhooks/1015254665182593044/y6C72E_3paaWQx0MOFO6f42TvTX4znOJoPYIl_ZYS9tB9umxurMq3e_VB-j7kdDjF78x","https://discord.com/api/webhooks/1015232903560577115/i38-FAKXlHlFEyZb4Pq5N0Vkc08ybwaIeCflBR_4ydXFzjKoqQEyMbW3ZmJG-Bqw5kmK"]
@bot.command()
async def test(ctx):
    await ctx.channel.create_webhook(name="mywebhook")
    wlist = []
    for w in await ctx.guild.webhooks():
        wlist.append(f"{w.name} - {w.url}")
    content = "\n".join(wlist)
    print(content)
@bot.event
async def on_ready():
    print("bot is ready")
@bot.event
async def on_message(message):
    with open(r"C:\Users\jacky\Documents\discord\ROK\webhook\server.json", "r+") as fp:
        data = json.load(fp)
    author = message.author
    image = author.avatar.url
    if not message.author.bot:
        if message.content:      
            msg = message.content
        elif message.attachments: 
            msg = message.attachments[0].url

        path = [data[i] for i in data if str(message.guild.id) != i]
        webhook = DiscordWebhook(url=path,username=author.name,avatar_url=image,content=msg) 
        response = webhook.execute()    




bot.run("ODMzODk1NDI4OTM2MzAyNjYy.GCiTwQ.mefArrlKgdJThfK-TnZJRI3gDKZwBxGge-Crqw")