import discord
from discord.ext import commands
import random
from sakura_bot.core.bot import SakuraBot


class Game(commands.Cog):
    def __init__(self, bot: SakuraBot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx: commands.Context, a: int, b: int):
        result = random.choices(range(1, b + 1), k=a)
        return await ctx.send(
            f'{a}D{b}の結果は{sum(result)}です．\n内訳{result}'
        )

def setup(bot):
    return bot.add_cog(Game(bot))
