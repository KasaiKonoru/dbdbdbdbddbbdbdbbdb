import random
import aiohttp
import praw
import time
from check import is_vale
import requests
import asyncio
from datetime import datetime

import discord
from discord.ext import commands

apikey = "0TQD507VHPOR"

lmt = 8

pass_list = ['619518820045815809']

reddit = praw.Reddit(client_id='CFfgp9jESrgbLA',
                     client_secret='HZhSLIsgRMlgP379vA_7YNHQdaU',
                     user_agent='windows:com:Neko Public:reddit.3.22.0(by /u/<MuffinAmor88919>)')

bot = commands.Bot(command_prefix='t!')

botcolor = 0xffffff

bot.remove_command('help')


class alles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ################################################################################################################
    @commands.command()
    @is_vale()
    async def ban(self, ctx, member: discord.Member, reason):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send("Der User wurde gebannt!")

    ################################################################################################################
    @commands.command()
    @is_vale()
    async def kick(self, ctx, member: discord.Member, reason):
        await ctx.guild.kick(member, reason=reason)
        await ctx.send("Der User wurde gekickt!")

    ####################################################################################################################
    @commands.command()
    @is_vale()
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send("{} Nachrichten gelöscht!".format(len(deleted)))

    ####################################################################################################################
    @bot.command()
    @is_vale()
    async def say(self, ctx, *args):
        if ctx.author.bot == False:
            if "@everyone" in ctx.message.content:
                msg1 = await ctx.send("`@everyone` mentions about that function are not allowed.")
                await asyncio.sleep(10)
                await msg1.delete(msg1)
            elif "@here" in ctx.message.content:
                msg1 = await ctx.send("`@here` mentions about that function are not allowed.")
                await asyncio.sleep(10)
                await msg1.delete(msg1)
            else:
                msg = ' '.join(args)
                await ctx.send(msg)
                await asyncio.sleep(0.2)
                await ctx.message.delete()

    ####################################################################################################################
    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        if not ctx.author.bot:
            member = user or ctx.author
            embed = discord.Embed(color=ctx.author.color)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text="{}'s Avatar".format(member.name),
                             icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    ####################################################################################################################
    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def customping(self, ctx, *args):
        url = ''.join(args)
        start = time.time()
        async with self.session.get(url):
            duration = time.time() - start
        await ctx.send('Der Ping für **{}** beträgt **{}** ms.'.format(url, round(duration * 1000)))

    ####################################################################################################################
    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def ping(self, ctx):
        start = time.time()
        async with self.session.get("https://discordapp.com"):
            duration = time.time() - start
        async with self.session.get("https://www.youtube.com"):
            duration2 = time.time() - start
        await ctx.send(
            'Die Bot-Latenz beträgt **{}** ms.\n'
            'Der Ping zu Discord ist **{}** ms.\n'
            'Der Ping zu YouTube ist **{}** ms.'.format(
                round(self.bot.latency * 1000), round(duration * 1000), round(duration2 * 1000)))

    ####################################################################################################################
    @bot.command()
    @is_vale()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roleinfo(self, ctx, role: discord.Role):
        if ctx.message.author.bot == False:
            server = ctx.guild
            role_info1 = (datetime.utcnow() - role.created_at).days
            l = list(permi for permi, value in role.permissions if str(value) == 'True')
            i = '\n📍 '.join(l)
            embed = discord.Embed(color=role.color)
            embed.add_field(name='__Role Info__', value='** **', inline=False)
            embed.add_field(name='Rolename:', value='{0} | {1}'.format(role.name, role.mention), inline=False)
            embed.add_field(name='Role ID:', value='{0}'.format(role.id), inline=True)
            embed.add_field(name='Role color:', value='{0}'.format(role.color), inline=True)
            embed.add_field(name='Role shows seperat from online!t:', value='{0}'.format(role.hoist), inline=True)
            embed.add_field(name='Role position:', value='{0}'.format(role.position), inline=True)
            embed.add_field(name='Role mentionable:', value='{0}'.format(role.mentionable), inline=True)
            embed.add_field(name='Role permissions:', value='📍 {0}'.format(i), inline=False)
            embed.add_field(name='Created at:', value='{}'.format(
                "{} ({} days ago!)".format(role.created_at.strftime("%d. %b. %Y %H:%M"), role_info1)), inline=False)
            author = ctx.message.author
            embed.set_thumbnail(url="{0}".format(server.icon_url))
            embed.set_footer(text='Message was requested by {0}'.format(author),
                             icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    ####################################################################################################################
    @bot.command()
    @is_vale()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if ctx.message.author.bot == False:
            server = ctx.guild
            server_info1 = (datetime.utcnow() - server.created_at).days
            rl = list(role.mention for role in server.roles if not role.name == "@everyone")
            Bot = list(member.bot for member in server.members if member.bot is True)
            user = list(member.bot for member in server.members if member.bot is False)
            embed = discord.Embed(title="Server Info",
                                  color=ctx.message.author.color)
            embed.add_field(name='Name:', value='{}'.format(server.name), inline=True)
            embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
            embed.add_field(name='Region:', value='{}'.format(server.region), inline=True)
            embed.add_field(name='AFK Channel:',
                            value='{0} ({1} seconds)'.format(server.afk_channel, server.afk_timeout), inline=True)
            embed.add_field(name='Membercount:', value='{} members'.format(server.member_count), inline=True)
            embed.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True)
            embed.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
            embed.add_field(name='Large Server:', value='{} (250+ member)'.format(server.large), inline=True)
            embed.add_field(name='Serverowner:', value='{}'.format(server.owner), inline=True)
            embed.add_field(name='Verifylevel:', value='{} '.format(server.verification_level), inline=True)
            embed.add_field(name='Serverroles:', value=str(len(rl)), inline=True)
            embed.add_field(name='Created at:', value='{}'.format(
                "{} ({} days ago!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)),
                            inline=False)
            embed.set_thumbnail(url="{0}".format(server.icon_url))
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author),
                             icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg1 = await ctx.send(embed=embed)

    ####################################################################################################################
    @commands.command()
    async def meme(self, ctx):
        if not ctx.message.author.bot:
            memes_submissions = reddit.subreddit('meme').top()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            sub = submission.title
            sub2 = submission.url
            embed = discord.Embed(color=ctx.message.author.color)
            embed.add_field(name=sub,
                            value="[Es wird nicht angezeigt? Klick hier]({0})".format(sub2),
                            inline=False)
            embed.set_image(url=sub2)
            embed.set_footer(text='#Meme')
            await ctx.send(embed=embed)

    ################################################################################################################
    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def tenor(self, ctx, *args: str):
        search = ' '.join(args)
        search_term = search  # search for ...
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
        if r.status_code == 200:
            top_8gifs = r.json()
            post_to_pick = random.randint(1, len(top_8gifs["results"]))
            for i in range(1, post_to_pick):
                url = top_8gifs['results'][i]['media'][0]['gif']['url']
            try:
                embed = discord.Embed(color=ctx.author.color)
                embed.add_field(name="Tenor", value="[Es wir nicht gezeigt? Klick hier!]({0})".format(url),
                                inline=False)
                embed.set_image(url=url)
                embed.set_footer(text='Tenor wurde angefragt von {}'.format(ctx.author),
                                 icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)
            except ValueError:
                msg = await ctx.channel.send("Bitte wählen Sie einen anderen Titel. Ich habe nichts gefunden")
            except Exception as error:
                await ctx.channel.send(error)
        else:
            top_8gifs = None


########################################################################################################################

def setup(bot):
    bot.add_cog(alles(bot))
