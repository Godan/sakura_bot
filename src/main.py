#! /usr/bin/env python
from sakura_bot.core.bot import SakuraBot
import discord
import settings

print(settings.TOKEN)
client = discord.Client()
SakuraBot(settings.TOKEN).run()
