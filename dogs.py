import random

from discord.ext import commands

FILENAME = "dogs.txt"

class Game:
    def __init__(self):
        self.players = {}

class DogsGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game = Game()

    @commands.command()
    async def dogs(self, ctx, *args):
        """
        """
        command = args[0]
        arguments = args[1:]

        if command == "add":
            try:
                count, size = map(int, command.split('d'))
            except Exception:
                await ctx.send('Usage: /dogs add NdN')
                return

            rolls = [str(random.randint(1, size)) for _ in range(count)]

            if ctx.author not in self.game.players:
                self.game.players[ctx.author] = rolls
            else:
                self.game.players[ctx.author].append(rolls)

            await ctx.send(f"@{ctx.author} {' '.join(self.game.players[ctx.author]}")
    
    @commands.command()
    async def d(self, ctx, *args):
        await self.dogs(ctx, *args)