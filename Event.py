import discord
from discord.ext import commands,tasks
import time
import datetime
import asyncio
F=["00","12","03"]
async def tests(bot):
    channel=bot.get_channel(876349293043265537)
    await channel.send('hi')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.test.start()
    def cog_unload(self):
        self.printer.cancel()
    @commands.command()
    async def Alpha(self,ctx):
        await tests(self.bot) 
    @tasks.loop(minutes=1) 
    async def test(self): 
        t_h=datetime.datetime.utcnow().strftime('%H')
        t_m=datetime.datetime.utcnow().strftime('%M')
        if str(t_h) in F:
            if str(t_m) == "15":
                print("Guard start in 15 min")
                await tests(self.bot)
                
            else:
                print("Guard start in 30 min")
        print(datetime.datetime.utcnow().strftime('%H:%M:%S'))
        #946851259661574184,956017310206930944
        await tests(self.bot)
def setup(bot):
    bot.add_cog(Events(bot))




        
