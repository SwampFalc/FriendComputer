import random

from discord.ext import commands

class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, *args):
        """
        v1: xdy
        """
        command = args[0]
        comments = args[1:]

        try:
            count, size = map(int, command.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        rolls = [random.randint(1, size) for _ in range(count)]

        await ctx.send(f"{'+'.join(rolls)} = {sum(rolls)}")
    
    @commands.command()
    async def r(self, ctx, *args):
        await self.roll(ctx, *args)