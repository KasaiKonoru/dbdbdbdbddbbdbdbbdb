from datetime import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t!')

botcolor = 0x00ff06

bot.remove_command('help')

url = 'https://cdn.discordapp.com/attachments/673470817165639687/673943252637974538/Download.jpg'


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def help(self, ctx):
        if ctx.author.bot == False:
            id = str(ctx.author.id)
            embed = discord.Embed(
                color=ctx.author.color)
            embed.set_author(name='Tatsuka Help Menü! 🤍')
            embed.add_field(name='🎮', value='Öffne das Mitglieder Menü! 🤍', inline=False)
            embed.add_field(name='🔭', value='Öffne das Developer Menü! 🤍', inline=False)
            embed.add_field(name='⬅', value='Gehe zurück zum Start!', inline=False)
            embed.set_thumbnail(
                url=url)
            embed.set_footer(text='Hilfe Menü 🤍| Tatsuka')
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("🎮")
            await msg.add_reaction("🔭")
            await msg.add_reaction("⬅")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.author.id == self.bot.user.id:
            if user.bot == False:
                if reaction.emoji == "🎮":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Tatsuka Help Menü! 🤍')
                    embed.add_field(name='Memes',
                                    value='t!meme', inline=False)
                    embed.add_field(name='Avatar',
                                    value='t!avatar *member*', inline=False)
                    embed.add_field(name='Tenor',
                                    value='t!tenor *schlagwort*', inline=False)
                    embed.add_field(name='Custom Ping',
                                    value='t!customping *link*', inline=False)
                    embed.add_field(name='**⬅**', value='Gehe zurück zum Start!', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_author(name='Tatsuka Help Menü! 🤍')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🎮", user)
                if reaction.emoji == "🔭":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Tatsuka Help Menü! 🤍')
                    embed.add_field(name='Ban',
                                    value='t!ban *member*', inline=False)
                    embed.add_field(name='Kicken',
                                    value='t!kick *member*', inline=False)
                    embed.add_field(name='Set Online',
                                    value='t!set_online *channel id*', inline=False)
                    embed.add_field(name='Stop Online',
                                    value='t!stop_online', inline=False)
                    embed.add_field(name='Server Info',
                                    value='t!serverinfo', inline=False)
                    embed.add_field(name='Rollen Info',
                                    value='t!roleinfo', inline=False)
                    embed.add_field(name='Lösche Nachrichten',
                                    value='t!clear *nummer*', inline=False)
                    embed.add_field(name='Say',
                                    value='t!say *text*', inline=False)
                    embed.add_field(name='Info! ! !',
                                    value="Nur Tatsuka KasEI und Tatsuka Cleanuss können die Dev Cmds nutzen")
                    embed.add_field(name='**⬅**', value='Gehe zurück zum Start!', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_footer(text='Hilfe Menü 🤍| Tatsuka')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🔭", user)
                if reaction.emoji == "⬅":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Tatsuka Help Menü! 🤍')
                    embed.add_field(name='🎮', value='Öffne das Mitglieder Hilfemenü! 🤍', inline=False)
                    embed.add_field(name='🔭', value='Öffne das Developer Hilfemenü! 🤍', inline=False)
                    embed.add_field(name='⬅', value='Gehe zurück zum Start!', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_footer(text='Hilfe Menü 🤍| Tatsuka')
                    embed.timestamp = datetime.utcnow()
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("⬅", user)


def setup(bot):
    bot.add_cog(help(bot))
