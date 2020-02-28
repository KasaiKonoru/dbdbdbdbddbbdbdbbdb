import asyncio

import discord
from discord.ext import commands

TOKEN = 'NjczOTYwMDUzNTA5OTgwMTYx.XjhoVw.orxdl3YcSliFxglHLB1tjSX54FQ'

bot = commands.Bot(command_prefix='t!')

botcolor = 0xffffff

bot.remove_command('help')
########################################################################################################################

extensions = ['commands.alles', 'commands.help', 'commands.auto', 'commands.partnerapply',
              'commands.online']


@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    bot.loop.create_task(status_task())


########################################################################################################################
async def status_task():
    while True:
        servers = list(bot.guilds)
        await bot.change_presence(activity=discord.Game('Tatsuka'), status=discord.Status.online)
        await asyncio.sleep(20)

        await bot.change_presence(activity=discord.Game('mit den Besten! | 🤍'), status=discord.Status.online)
        await asyncio.sleep(20)

    ########################################################################################################################


@bot.command()
@commands.is_owner()
async def bye(ctx):
    await ctx.channel.send("#Tatsuka")
    await bot.logout()


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print('{} wurde geladen.'.format(extension))
        embed = discord.Embed(
            title='{} wurde geladen.'.format(extension),
            color=botcolor
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=botcolor
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print('{} wurde deaktiviert.'.format(extension))
        embed = discord.Embed(
            title='{} wurde deaktiviert.'.format(extension),
            color=botcolor
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=botcolor
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.channel.send('{} wurde neu geladen.'.format(extension))
    except Exception as error:
        await ctx.channel.send('{} konnte nicht geladen werden. [{}]'.format(extension, error))


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

bot.run(TOKEN)
