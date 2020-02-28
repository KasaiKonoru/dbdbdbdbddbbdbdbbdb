from datetime import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t!')

botcolor = 0x00ffff

apikey = "0TQD507VHPOR"

lmt = 8

botlist = [547124033410564116, 598585171977043968]

invs = [632552703918342144, 624630159575613440, 647880816768188416,
        663692225699643392]

bad = ["discord.gg", "discordapp.com/invite"]


class auto(commands.Cog):
    def __init__(self, bot, ):
        self.bot = bot

    ####################################################################################################################
    @commands.Cog.listener()
    async def on_message(self, message):
        if "discord.gg" in message.content or "discordapp.com/invite" in message.content:
            if message.author.guild_permissions.administrator == False:
                if not "InviteChannel" in message.channel.topic:
                    try:
                        await message.delete()
                        embed2 = discord.Embed(
                            description='Einladungslinks sind **NICHT** erlaubt! \n Einladung wurde gesendet von {}.'.format(
                                message.author.mention),
                            color=botcolor)
                        await message.channel.send(embed=embed2)
                    except:
                        pass

    ####################################################################################################################
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            server = self.bot.get_guild(668231490005368840)
            try:
                inv = await server.invites()
            except:
                pass
            for invites in inv:
                if invites:
                    invite2 = invites.url
                    break
            else:
                invite2 = "https://discord.gg"
            self.counter = + 1
            channel = self.bot.get_channel(673949069789626418)
            await channel.send("*{}* behält einen Fehler ```{}```".format(ctx.message.content, error))
            embed = discord.Embed(title="Ops, da ist ein Fehler!",
                                  description="Fehlermeldung Nr. {}.".format(self.counter),
                                  color=botcolor)
            embed.add_field(name='Server:', value='{}'.format(ctx.message.guild), inline=True)
            embed.add_field(name='Befehl:', value='{}'.format(ctx.message.content), inline=False)
            embed.add_field(name='Error:', value="```python\n{}```".format(error), inline=False)
            embed.add_field(name='Probleme?',
                            value='Mach ein Foto und kontaktiere mich [hier]({}).'.format(invite2),
                            inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text='Fehlermeldung!', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)
            print(error)

####################################################################################################################


def setup(bot):
    bot.add_cog(auto(bot))
