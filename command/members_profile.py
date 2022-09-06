from pydoc import describe
from discord.ext import commands
import discord
import json

class main(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="test",describe="")
    async def _start_manage(self, ctx):

        with open(r"C:/Users/jacky/Documents/discord/ROK/config/data/guilds_data.json", "r+") as fp:
                    data = json.load(fp)
        guilds_id = ctx.guild.id
        await ctx.respond(f"Server id : `{guilds_id}`\nStart server member profile",ephemeral=True)
        if str(guilds_id) not in data:
            data[str(guilds_id)] = {}
            fp.seek(0)
            json.dump(data, fp , indent=4)
            fp.truncate()
            for members in ctx.guild.members:
                if members.bot:
                    continue
                print(members)
                data[str(guilds_id)].update({str(members):{}})
                fp.seek(0)
                json.dump(data, fp, indent=4)
                fp.truncate()

def setup(bot):
    bot.add_cog(main(bot))