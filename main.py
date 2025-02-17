from discord.ext import commands
from discord import app_commands
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)

curses = {
    "yup":"<:curse1:1338598542570422406>",
    "huh":"<:curse5:1338599356726644837>",
    "mmm":"<:curse3:1338599372182523904>",
    "that sucks":"<:curse4:1338599388410286233>",
    "it happens":"<:curse5:1338599704333651968>",
    "help":"<:curse6:1341007178219262023>",
}


@bot.event
async def on_message(ctx):
    print(ctx.content)
    for curse, emoji in curses.items():
        if curse in ctx.content.lower():
            print("CURSE DETECTED!! " + curse)
            await ctx.add_reaction(emoji)

bot.run(os.environ.get("CURSEBOT_TOKEN"))
