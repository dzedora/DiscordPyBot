import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


bot = commands.Bot(command_prefix = "!")
dickS = ["%s has a vagina..."]

@bot.event
async def on_ready():
    print("Bot is connected to discord homie!")
    print("I am running as " + bot.user.name)
    print ("With the ID: " + (bot.user.id))


@bot.command(pass_context=True)
async def size(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say("You didn't mention anyone...")
    if member.id == "256963559395819520" and member.id == ctx.message.author.id:
        await bot.say('Why you checking up on yourself?')
    elif member.id == "256963559395819520":
        await bot.say(ctx.message.author.mention + " has a big dick")
    elif member.id == "391328492006146059":
        await bot.say("I don't have a dick my dude.")
    else:
        await bot.say(ctx.message.author.mention + "has a vagina")

@bot.command(pass_context=True)
async def echo(ctx,*, echo: str = None):
    if echo == None:
        await bot.delete_message(ctx.message)
        await bot.say("You didn't give me anything to say")
    else:
        await bot.delete_message(ctx.message)
        await bot.say(echo)

#@bot.command(pass_context=True)
#async def size(self, ctx):
#    await bot.say("{} has a big dick".format(ctx.message.author.mention))

bot.run("MzkxMzI4NDkyMDA2MTQ2MDU5.DRXPZA.gI0RNj_dJA06Brn2sww07hXjkfg")
