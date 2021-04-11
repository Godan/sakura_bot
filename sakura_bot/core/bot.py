import traceback

import discord
from discord.ext import commands


class SakuraBot(commands.Bot):
    def __init__(self, token):
        self.token = token
        super().__init__(command_prefix="$")
        self.load_cogs()

    def load_cogs(self):
        cogs = ["sakura_bot.cogs.game"]
        for cog in cogs:
            self.load_extension(cog)
            print(cog + "をロードしました")

    # 起動用の補助関数です
    def run(self):
        try:
            self.loop.run_until_complete(self.start(self.token))
        except discord.LoginFailure:
            print("Discord Tokenが不正です")
        except KeyboardInterrupt:
            print("終了します")
            self.loop.run_until_complete(self.logout())
        except BaseException:
            traceback.print_exc()
