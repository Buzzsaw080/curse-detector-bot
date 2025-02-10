from discord.ext import commands
from discord import app_commands
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)

curses = {
    "yup":"😎",
    "huh":"😎",
    "mmm":"😎",
    "that sucks":"😎",
    "it happens":"😎",
}


@bot.event
async def on_message(ctx):
    print(ctx.content)
    for curse, emoji in curses.items():
        if curse in ctx.content.lower():
            print("CURSE DETECTED!! " + curse)
            await ctx.add_reaction(emoji)

bot.run(os.environ.get("CURSEBOT_TOKEN"))