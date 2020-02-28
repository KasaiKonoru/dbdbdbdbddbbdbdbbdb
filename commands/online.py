import asyncio
import discord
from discord.ext import commands
from check import del_channel
from check import request_channel
from check import set_channel

bot = commands.Bot(command_prefix='t!')

botcolor = 0x000ffc

bot.remove_command('help')

count = 0


class online(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def set_online(self, ctx, channel: discord.VoiceChannel):
        if ctx.author.bot:
            return
        await ctx.send(set_channel(str(ctx.guild.id), str(channel.id)))
        while request_channel(str(ctx.guild.id)) != None:
            channelid = request_channel(str(ctx.guild.id))
            channel = self.bot.get_channel(int(channelid))
            global count
            guild = ctx.guild
            count = count - count
            for m in guild.members:
                if not str(m.status) == 'offline':
                    count = count + 1
            await channel.edit(name="🟢Online: {}".format(count))
            await asyncio.sleep(20)

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def stop_online(self, ctx):
        if ctx.author.bot:
            return
        await ctx.send(del_channel(str(ctx.guild.id)))


def setup(bot):
    bot.add_cog(online(bot))
