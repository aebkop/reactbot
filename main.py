import logging
import discord
from discord.ext import commands
from tinydb import TinyDB, Query

logging.basicConfig(level=logging.INFO)
description = '''An example bot to showcase the discord.ext.commands extension '''
robo_thatcher = discord.Client(command_prefix='?')
db = TinyDB('database.json')
query_words = Query()
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def addreact(key_to_add: str, *text_to_add: str):
    print("this is to see if this even gets hit")
    db.insert({"key": key_to_add, "text": text_to_add})
    for index in db:
        print(index)


@bot.command()
async def delreact(key_to_remove: str):
    print("this is to see if this even gets hit")
    db.remove(query_words.key == key_to_remove)
    for index in db:
        print(index)


@bot.command()
async def test():
    print("this is to see if this even gets hit")


@bot.event
async def on_message(message):
    if message.author == robo_thatcher.user:
        await bot.process_commands(message)
        return
    response_words: list = db.search(query_words.key.exists())
    for item in response_words:
        if item["key"] in message.content.lower():
            print("found message")
            await bot.send_message(message.channel, item["text"])
            await bot.process_commands(message)
    await bot.process_commands(message)
    return


bot.run('NDQzOTA1MzA2Mzc3MDYwMzUy.DdUbYQ.zokQMbnOzT5npCBhS2VVOIB_42E')
