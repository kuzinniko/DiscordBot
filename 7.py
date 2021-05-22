import discord
import os
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix='#')
bot.remove_command('help')
bad_words = ['nigga', 'niger','fag','faggot','negro','#bantestforbot']


@bot.event
async def on_ready():
    print("connected")
    # выставляем статус бота
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game('BATTLEFRONT 2'))

# + фильтр чата
@bot.event
async def on_message(message):
    await bot.process_commands(message)  # строчка, чтобы работали command
    for a in bad_words:
        if a in message.content.lower():
            await message.delete()
            # сообщаем в чат, что ругаются
            await message.channel.send(f"{message.author} IS RACIST!")
            await message.author.kick(reason='GTFO')
            return


@bot.command()
async def bye(ctx):
    nick = ctx.message.author  # .mention #.id
    await ctx.send(f"bye {nick}")


@bot.command()
async def help(ctx):
    await ctx.send("This bot can answer to #Hi and #Bye it also can ban you for using racial and gender slurs (if you mean it as a joke replace atleast one letter with (!) or you will get banned!!!) \
    it also can delete the amount of messages you write with the command (#clear [number of messages to delete]) but you need administrator rights to do this.")

@bot.command()
async def hi(ctx):
    nick = ctx.message.author  # .mention #.id
    await ctx.send(f"Hi {nick}")


@bot.command()
@commands.has_permissions(administrator=True)  # если есть права админа
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(administrator=True)  # если есть права админа
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


bot.run(str(os.environ.get('BOT_TOKEN')))