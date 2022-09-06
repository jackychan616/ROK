from pydoc import describe
import discord
from discord.ext import commands


class Verify(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="verify" ,describe="verify new members")
    async def _verify(self, ctx):
        guild, channel = ctx.guild.id, ctx.channel.id
        await ctx.respond(channel)

def setup(bot):
    bot.add_cog(Verify(bot))