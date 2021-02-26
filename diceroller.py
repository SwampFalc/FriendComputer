import random

from discord.ext import commands

class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))