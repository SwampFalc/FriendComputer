import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import diceroller

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    logging.info(f"{bot.user} has connected to Discord!")

bot.add_cog(diceroller.DiceRoller(bot))
bot.run(TOKEN)
