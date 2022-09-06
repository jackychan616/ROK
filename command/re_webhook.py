from secrets import choice
import discord
from discord.ext import commands
class w_main(discord.Cog):
    def __init(self, bot):
        self.bot = bot 
    @commands.slash_command(name="muti_chat",describe="Create a channel with muti discord server")
    async def _re(self, ctx:discord.ApplicationContext,categories:discord.Option(str, "test",choice=["idk","idk1"]),channel_name:discord.Option(str,"Name of the channel"),kd: discord.Option(int,"Your kd code eg.1234 ,2345")):
        embed = discord.Embed(title="Created webhook at {name}", description="Other kd")
        await ctx.respond(embed=embed)
        channel = await ctx.guild.create_text_channel(channel_name,category=discord.utils.get(ctx.guild.categories, name=categories))
def setup(bot):
    bot.add_cog(w_main(bot))