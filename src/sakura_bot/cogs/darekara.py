from discord.ext import commands
import random
from sakura_bot.core.bot import SakuraBot


class Darelara(commands.Cog):
    def __init__(self, bot: SakuraBot):
        self.bot = bot

    @commands.command()
    async def darekara(self, ctx: commands.Context, *args: str):
        members = random.sample(list(args))
        send_message = "まぜまぜしたよ！ \n"
        for index, member in enumerate(members):
            send_message += f"{index * 1}番目は {member} さん\n"
        return await ctx.send(send_message)


def setup(bot):
    return bot.add_cog(Darelara(bot))
