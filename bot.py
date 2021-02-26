import discord
from discord.ext import commands
from dotenv import load_dotenv

import diceroller

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

bot = commands.Bot(command_prefix='/')

@bot.command()
async def roll(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

bot.add_command(roll)

client.run(TOKEN)
