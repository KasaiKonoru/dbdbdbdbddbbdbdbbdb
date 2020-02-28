import asyncio
import random
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t!')
botcolor = 0x000ffc
applylist = [673956476049686558]
answers = ["Ich mag das:", "Ich habe verstanden:", "Interessante Antwort.", ":eyes:.Gute Antwort.", "Großartig!", ""]
questions = ["Nett! Beginnen wir mit der nächsten Frage. ", " Uh Nice du bist bei einer Frage! ",
             "Huh? Wo bin ich? Oh heyo!", "Ich bin ein Bot. Beantworte die Frage :joy:"]


class partnerapply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.category.id in applylist:
            await channel.send(
                "Heyo! Ich bin {}, \n Ich werde dir heute bei deiner Bewerbung als Assistent dienen. \nMöchtest du denn Starten? \n Gebe t!startpartner ein.".format(
                    self.bot.user.name))

    @commands.command()
    @commands.cooldown(1, 800, commands.BucketType.channel)
    async def startpartner(self, ctx):
        if not ctx.channel.category.id in applylist:
            return

        def pred(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("Willkommen im Partnerprogramm! Bist du bereit? \n Bitte antworte mit **y** oder **n**.")
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht...')
                return
            if msg.content == "y":
                await ctx.send("Großartig!!! \n Beginnen wir mit wenigen Erläuterungen.")
                break
            elif msg.content == "n":
                await ctx.send("Oh ok. bis zum nächsten mal dann!")
                return
            else:
                await ctx.send("Ops, ungültige Eingabe!\nSchreibe **y** für Start und **n** für Ablehnung.")
                continue
        embed = discord.Embed(
            color=ctx.author.color)
        embed.set_author(name='Vielen Dank für deine Partner Bewerbung! Die erste Frage startet in 20 Sekunden.')
        embed.add_field(name='Regeln:',
                        value='Wenn du etwas geschrieben hast werde ich zur nächten Frage gehen.\n Bitte antworte wahrheitsgemäß und Ordentlich ',
                        inline=False)
        embed.add_field(name='Time:', value='Du hast für jede Frage 150 Sekunden Zeit, bevor die nächste beginnt.',
                        inline=False)
        embed.add_field(name='Überspringen und Beenden',
                        value='Du kannst Fragen überspringen mit **skip**\nWenn du abbrechen willst schreibe **end**',
                        inline=False)
        embed.set_thumbnail(
            url=self.bot.user.avatar_url)
        embed.set_footer(text='🤍Partner Bewerbungen🤍')
        await ctx.send(embed=embed)
        await asyncio.sleep(20)
        await ctx.send(
            "Ok, lass uns mit deiner ersten Frage beginnen! \n Wie alt ist dein Server?(Erstellungsdatum) 1/7")
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht...\nGehen wir zur nächsten Frage!')
                age = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                age = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                age = msg.content
                await ctx.send("Dein Server wurde also am **{}** erstellt. Cool 🤍".format(age))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nWie viele Member habt ihr? 2/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht ... \nWeiter mit der nächsten Frage!')
                reason = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                reason = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                reason = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), reason))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nWarum wollt ihr genau bei **uns** Partner werden? 3/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht ... \nWeiter mit der nächsten Frage!')
                mod = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                mod = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                mod = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), mod))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nWas hat euer Server so besonderes an sich? 4/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht ... \nWeiter mit der nächsten Frage!')
                skills = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                skills = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                skills = msg.content
                await ctx.send("Ihr habt erstaunliche besonderheiten!\n{} ".format(skills))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send(
            "{}\nWie viele Textchannel habt ihr? 5/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht ... \nWeiter mit der nächsten Frage!')
                langs = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                langs = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                langs = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), langs))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send(
            "{} {}.\nWie viele Voicechannel habt ihr? 6/7".format(random.choice(questions),
                                                                  ctx.author.name))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=150.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht ... \nWeiter mit der nächsten Frage!')
                offended = "Outtimed"
                break
            if "skip" == msg.content:
                offended = "skipped"
                await ctx.send("Ok, diese Frage wird übersprungen.")
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!.")
                return
            else:
                offended = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), offended))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nAus wie vielen Personen besteht euer Team? 7/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=140.0)
            except asyncio.TimeoutError:
                await ctx.send('Du hast zu lange gebraucht...\nWWir gehen jetzt zum Ende!')
                add = "Outtimed"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                add = "skipped"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde deine Partner Bewerbung löschen. Bis zum nächsten Mal!")
                return
            else:
                add = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), add))
                break
        await ctx.send(
            "Vielen Dank für Ihre Bewerbung. Ich habe es an die Entwickler geschickt und werde dich kontaktieren, wenn es etwas Neues gibt!")
        embed = discord.Embed(
            color=ctx.author.color)
        embed.set_author(name='Bewerbung von {}'.format(ctx.author, ))
        embed.add_field(name="Server:", value=ctx.guild, inline=False)
        embed.add_field(name="Warum bei uns?", value=mod, inline=False)
        embed.add_field(name="Alter des Servers:", value=age, inline=False)
        embed.add_field(name='Member:', value=reason, inline=False)
        embed.add_field(name='Textchannel:', value=langs, inline=False)
        embed.add_field(name='Besonderheiten am Server:', value=skills, inline=False)
        embed.add_field(name='Voicechannel:', value=offended, inline=False)
        embed.add_field(name='Mitglieder Anzahl:', value=add, inline=False)
        embed.set_thumbnail(
            url=self.bot.user.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='🤍Bewerbungen🤍')
        server = self.bot.get_guild(433980111558279185)
        for i in server.categories:
            if i.id == 653647415383162881:
                channel = await server.create_text_channel(name="{}s Partner Bewerbung".format(ctx.author.name),
                                                           category=i)
                await channel.send("@here",
                                   embed=embed)


def setup(bot):
    bot.add_cog(partnerapply(bot))
