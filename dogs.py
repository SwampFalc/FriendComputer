import json
import random

from discord.ext import commands

FILENAME = "dogs.json"

DIGITS = {
    "1": "①",
    "2": "②",
    "3": "③",
    "4": "④",
    "5": "⑤",
    "6": "⑥",
    "7": "⑦",
    "8": "⑧",
    "9": "⑨",
    "10": "⑩",
    "11": "⑪",
    "12": "⑫",
}
 	 	 	 	 	 	 	 	 	 	 

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
        player = ctx.author.display_name
        command = args[0]
        arguments = list(args[1:])

        if command == "new":
            self.game = Game()

        if command == "add":
            dice = arguments.pop(0)
            try:
                count, size = map(int, dice.split('d'))
            except Exception:
                await ctx.send('Usage: /dogs add NdN')
                return

            rolls = [str(random.randint(1, size)) for _ in range(count)]
            await ctx.send(f"{player} rolled {' '.join(rolls)}")

            if player not in self.game.players:
                self.game.players[player] = rolls
            else:
                self.game.players[player].extend(rolls)

        self.game.save()
        for player, numbers in self.game.players.items():
            digits = [DIGITS[num] for num in sorted(numbers)]
            await ctx.send(f"{player}: {' '.join(digits)}")
    
    @commands.command()
    async def d(self, ctx, *args):
        await self.dogs(ctx, *args)