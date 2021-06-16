import json
import random

from discord.ext import commands

FILENAME = "dogs.json"


class Game:
    def __init__(self):
        self.players = {}
    
    def save(self):
        with open(FILENAME, 'w') as f:
            json.dump(self.players, f)

    def load(self):
        with open(FILENAME) as f:
            self.players = json.load(f)


class DogsGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game = Game()
        self.game.load()

    @commands.command()
    async def dogs(self, ctx, *args):
        """
        """
        # if args == []:
        #   print help

        player = ctx.author.display_name
        command = args[0]
        arguments = list(args[1:])

        if command == "new":
            self.game = Game()

        if command == "add":
            for dice in arguments:
                try:
                    count, size = map(int, dice.split('d'))
                except Exception:
                    await ctx.send('Usage: /dogs add NdN (NdN ...)')
                    return

                rolls = [str(random.randint(1, size)) for _ in range(count)]
                await ctx.send(f"{player} rolled {dice}: {', '.join(rolls)}")

                if player not in self.game.players:
                    self.game.players[player] = rolls
                else:
                    self.game.players[player].extend(rolls)

        if command == "use":
            if player not in self.game.players:
                await ctx.send('You have not joined the game yet')
                return

            for number in arguments:
                try:
                    self.game.players[player].remove(number)
                except ValueError:
                    await ctx.send(f'You have no {number} available')

        if command == "fix":
            if player not in self.game.players:
                await ctx.send('You have not joined the game yet')
                return

            for number in arguments:
                self.game.players[player].append(number)

        self.game.save()
        for player, numbers in self.game.players.items():
            await ctx.send(f"{player}: {' - '.join(sorted(numbers))}")
    
    @commands.command()
    async def d(self, ctx, *args):
        await self.dogs(ctx, *args)