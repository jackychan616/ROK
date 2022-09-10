#!/usr/bin/python
# -*- coding: utf-8 -*-


import discord
from discord.ext import commands
import json
class w_main(discord.Cog):
    def __init(self, bot):
        self.bot = bot 
    @commands.slash_command(name="muti_chat",describe="Create a channel to use muti discord server function")
    async def _re(self, ctx:discord.ApplicationContext,channel_name:discord.Option(str,"Name of the channel"),kd: discord.Option(int,"Your kd code eg.1234 ,2345")):
        with open(r"C:\Users\jacky\Documents\discord\ROK\config\data\webhook.json","r+") as fp:
            data = json.load(fp)
            if str(ctx.guild.id ) in data:
                channel_id = data[str(ctx.guild.id)]["channel_id"]
                embed = discord.Embed(title="You already made a webhook",description=f"You can go to <#{channel_id}>")
                await ctx.respond(embed=embed)
            else:
                embed = discord.Embed(title=f"Created webhook at {channel_name}", description="Other kd")
                await ctx.respond(embed=embed)
                channel = await ctx.guild.create_text_channel(channel_name)
                await channel.create_webhook(name="ROKwebhook")
                webhooks = await ctx.guild.webhooks()
                for w in webhooks:
                    if w.name == "ROKwebhook":
                        with open(r"C:\Users\jacky\Documents\discord\ROK\config\data\webhook.json","r+") as fp:
                         data = json.load(fp)
                         data[str(ctx.guild.id)] = {"kd":kd,"url":str(w.url),"channel_name":str(channel.name),"channel_id":channel.id}
                         fp.seek(0)
                         json.dump(data ,fp, indent=4)
                         fp.truncate()
                         print(w.url)
def setup(bot):
    bot.add_cog(w_main(bot))    