import os

import discord
import random
import automation

from discord.ext import commands

TOKEN = 'MTAwMjc2MzM2ODE2OTQ4ODM4NA.GQ8Rda.x6HaHsFlLAHMZBLpj2Lmc-8_FiOJ0ZrXsCNhjo'

client = discord.Client()
bot = commands.Bot(command_prefix='s!')

@bot.event
async def on_ready():
    print(str(bot.user) + " has connected to Discord")

    for g in bot.guilds:
        print(str(bot.user) + " has connected to " + str(g.name))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #elif str(message.author) == 'porple#5831':
    #    await message.channel.send("agreed")

    elif "hi" in message.content.lower():
        print(str(message.author) + ": " + message.content)
        await message.channel.send("hi")

    elif "andrey" in message.content.lower():
        print(str(message.author) + ": " + message.content)
        await message.channel.send("andy")

    await bot.process_commands(message)


@bot.command(name='monke', help="monke")
async def monke(ctx):
    print(str(ctx.message.author) + ": " + ctx.message.content)
    await ctx.send("monke monke monke")

@bot.command(name='start', help="starting server")
async def startserver(ctx):
    print(str(ctx.message.author) + ": " + ctx.message.content)
    await automation.startserv(ctx)


bot.run(TOKEN)